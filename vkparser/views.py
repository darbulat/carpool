import re

from django.shortcuts import render
import requests
from carpool.models import Pool, User
import time
import vk


def destination(text):
    if re.search('(?:\sдо\s+|в\s+)киж', text):
        return ['Улан-Удэ', 'Кижинга']
    if re.search('(?:\sдо\s+|в\s+)(?:улан|город|уу|у.у|у-у)', text):
        return ['Кижинга', 'Улан-Удэ']

    if re.search('(?:\sдо\s+|в\s+)хор', text):
        return ['', 'Хоринск']
    return ['не найдено']*2


def is_passenger(text):
    if re.search(r'возьму|возьм[её]м', text):
        return 'Водитель'
    if re.search(r'пассаж|посылк', text):
        return 'Пассажир'
    if re.search(r'есть|\bеду\b', text):
        return 'Водитель'
    if re.search('уед', text):
        return 'Пассажир'
    if re.search('нужна машина|поедем', text):
        return 'Пассажир'
    if re.search('машина', text):
        return 'Водитель'
    return '-'


def take_1000_posts():
    token = 'b5cf544db5cf544db5cf544d72b5a5a66cbb5cfb5cf544de939146f1998f95467f319ba'
    version = 5.95
    domain = 'avtostop_kizhinga'
    count = 10
    offset = 0
    all_posts = []

    while offset < 50:
        responce = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = responce.json()['response']['items']
        offset += 10
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    user1 = User.objects.get(pk=3)
    session = vk.Session()
    api = vk.API(session, v=5.101)
    token = 'b5cf544db5cf544db5cf544d72b5a5a66cbb5cfb5cf544de939146f1998f95467f319ba'
    for post in data:
        if post['from_id'] > 0:
            id = post['from_id']
            responce = api.users.get(access_token=token, user_ids=id)

            text = post['text']
            result = re.search(r'[\+\(]?[1-9][0-9 \-\(\)]{8,}[0-9]', text).group(0) if \
                re.search(r'[\+\(]?[1-9][0-9 \-\(\)]{8,}[0-9]', text) else 'не указан'

            passenger = is_passenger(text.lower())
            point = destination(text.lower())
            Pool.objects.create(user=user1, passenger=passenger, source=point[0], dest=point[1], note=text,
                                dateTime=time.strftime("%Y-%m-%d", time.localtime(post['date'])),
                                phone_number=result, first_name=responce[0]['first_name'],
                                last_name=responce[0]['last_name'], vk_id=id,
                                )


def vk_refresh(request):
    all_posts = take_1000_posts()
    file_writer(all_posts)
    return render(request, 'index.html', context={})
