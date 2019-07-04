from django.shortcuts import render
import csv
import requests
from carpool.models import Pool, User


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
    with open('avtostop_kizhinga.csv', 'w') as file:
        a_pen = csv.writer(file)
        user1 = User.objects.get(pk=1)
        a_pen.writerow(('date', 'body', 'from_id'))
        for post in data:
            if post['from_id'] > 0:
                a_pen.writerow((post['date'], post['text'], post['from_id']))
                Pool.objects.create(user=user1, source='Кижинга', dest='Улан-Удэ', note=post['text'],
                                    )


def vk_refresh(request):
    all_posts = take_1000_posts()
    file_writer(all_posts)
    return render(request, 'index.html', context={})
