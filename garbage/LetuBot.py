import requests
import vk_api
import re
import lxml.html
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

session = requests.Session()

with open("password.txt", "r") as file:
    login = file.readline()
    password = file.readline()

login = login.rstrip('\n')

vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

MyVkList = ['коля', 'коль','николай','николя','колька', 'инженер', 'привет', 'хай', 'ку'] #Список слов
attachments = []

tree = lxml.html.parse("http://animepicsx.net/random")
images = tree.xpath("//img/@src")


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        str = event.text.lower()
        if str == 'аниме': #Если написали заданную фразу
            upload = VkUpload(vk_session)
            tree = lxml.html.parse("http://animepicsx.net/random")
            images = tree.xpath("//img/@src")
            image_url = images[0]
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send( 
                user_id=event.user_id,
                attachment=','.join(attachments),
                random_id=get_random_id(),
                message=''
            ) #Отправляем картинку
            attachments.clear()
        for item in MyVkList:			
            if item == str: #Если попалось слово из списка
                profile = vk.users.get(user_ids = event.user_id)
                if event.from_user: #Если написали в ЛС
                    vk.messages.send( #Отправляем сообщение
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name']
		            )
                    break
                elif event.from_chat: #Если написали в Беседе
                    vk.messages.send( #Отправляем собщение
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name']
		            )
                    break
