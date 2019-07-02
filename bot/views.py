from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from carpool.models import Pool, User
import datetime
import telebot

TOKEN = '838851391:AAG73VUNILnNnQbhF-9U6nrUy1uVt_ILK8Y'
bot = telebot.TeleBot(TOKEN)


# For free PythonAnywhere accounts
# tbot = telebot.TeleBot(TOKEN, threaded=False)

@csrf_exempt
def tbot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':

        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])

        return HttpResponse("")

    else:
        raise PermissionDenied


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")

