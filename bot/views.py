from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot

TOKEN = '838851391:AAG73VUNILnNnQbhF-9U6nrUy1uVt_ILK8Y'
tbot = telebot.TeleBot(TOKEN)


# For free PythonAnywhere accounts
# tbot = telebot.TeleBot(TOKEN, threaded=False)
# https://api.telegram.org/bot838851391:AAG73VUNILnNnQbhF-9U6nrUy1uVt_ILK8Y/setWebhook?url=https://ee136798.ngrok.io/cbbf15d8-0421-4512-84d9-5e5d977e3aef/

@csrf_exempt
def bot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':

        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tbot.process_new_updates([update])

        return HttpResponse("")

    else:
        raise PermissionDenied


@tbot.message_handler(content_types=["text"])
def get_okn(message):
    tbot.send_message(message.chat.id, "Hello, bot!")
