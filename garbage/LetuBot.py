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

    vk_api.Error

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

MyVkList = ['коля','коль','николай','николя','колька','инженер','привет','хай','ку','прет','здорово','салам'] #Список слов
attachments = []

tree = lxml.html.parse("http://animepicsx.net/random")
images = tree.xpath("//img/@src")

paramList = ['','']

def sendMessage(user_id,chat_id,attachment,random_id,message):
   	vk.messages.send( 	user_id = user_id,
						chat_id = chat_id,
                        attachment = attachment,
                        random_id = random_id,
                        message = message     )

def captcha_handler(url):

    """ При возникновении капчи вызывается эта функция и ей передается объект

        капчи. Через метод get_url можно получить ссылку на изображение.

        Через метод try_again можно попытаться отправить запрос с кодом капчи

    """

    key = input("Enter captcha code {0}: ".format(url)).strip()
       
    # Пробуем снова отправить запрос с капчей

    return e.try_again(key)
while 1:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
           #Слушаем longpoll, если пришло сообщение то:
                str = event.text.lower()
                str = str.rstrip()
                #if str == 'команды' or str == 'помощь':
                #    vk.message.send(user_id = event.user_id, random_id = get_random_id(), message = '', keyboard = {"buttons":[],"one_time":true})
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
                    if event.from_user: #Если написали в ЛС
                        sendMessage(user_id=event.user_id,chat_id=None,attachment=','.join(attachments),random_id=get_random_id(),message='')
                    elif event.from_chat: #Если написали в Беседе
                        sendMessage(user_id=None,chat_id=event.chat_id,attachment=','.join(attachments),random_id=get_random_id(),message='')
                    attachments.clear()
                elif str == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Введите Факультет, Курс, Номер группы в формате:\nФЭА45491')
                    paramList[0] = 'расписание'
                elif str == 'фэа45491':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Какой день недели?')
                    paramList[1] = 'фэа45491'
                elif str == 'понедельник' and paramList[1] == 'фэа45491' and paramList[0] == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='''ПСУвLabVIEW лабораторная\nБельский\n1подгруппа\n8205\n9:50\n\n
                                                                                                                            МодСУ лекция\nМирошников\n1245\n11:40\n\n
                                                                                                                            МодСУ практика\nВетчинкин\n8216\n13:45\n\n
                                                                                                                            МодСУ лабораторная.\nВетчинкин\n8216\n15:35''')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='МодСУ лекция\nМирошников\n1245\n11:40')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='МодСУ практика\nВетчинкин\n8216\n13:45')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='МодСУ лабораторная.\nВетчинкин\n8216\n15:35')
                elif str == 'вторник' and paramList[1] == 'фэа45491' and paramList[0] == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='''Основы мат.теории устойчивости лекция\nВторов\n6201\n11:40\n\n
                                                                                                                            Основы мат.теории устойчивости лекция\nВторов\n6201\n13:45\n\n
                                                                                                                            Основы мат.теории устойчивости практика\nВторов\n6201\n15:35\n\n
                                                                                                                            Основы мат.теории устойчивости практика\nВторов\n6201\nс 17:25 до 18.10''')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Основы мат.теории устойчивости лекция\nВторов\n6201\n13:45')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Основы мат.теории устойчивости практика\nВторов\n6201\n15:35')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Основы мат.теории устойчивости практика\nВторов\n6201\nс 17:25 до 18.10')
                elif str == 'среда' and paramList[1] == 'фэа45491' and paramList[0] == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='''ПСУвLabVIEW лабораторная\nБельский\n2подгруппа\n8205\n11:40\n\n
                                                                                                                            Проектирование СУ в ПММ NI LabVIEW лекция\nСтоцкая\n5143\n13:45\n\n
                                                                                                                            ПСУвLabVIEW практика\nСтоцкая\n8203-1\n15:35\n\n
                                                                                                                            ПСУвLabVIEW практика\nСтоцкая\n8203-1\nПо 1ой неделе\n17:25''')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Проектирование СУ в ПММ NI LabVIEW лекция\nСтоцкая\n5143\n13:45')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='ПСУвLabVIEW практика\nСтоцкая\n8203-1\n15:35')
                    #sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='ПСУвLabVIEW практика\nСтоцкая\n8203-1\nПо 1ой неделе\n17:25')
                elif str == 'четверг' or str == 'суббота' or str == 'воскресенье' and paramList[1] == 'фэа45491' and paramList[0] == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='Пар нету!')
                elif str == 'пятница' and paramList[1] == 'фэа45491' and paramList[0] == 'расписание':
                    sendMessage(user_id = event.user_id, chat_id=None,attachment=None,random_id=get_random_id(),message='ВМП с 9.50 до 15.35')
                else:        
                    for item in MyVkList:			
                        if item == str: #Если попалось слово из списка
                            profile = vk.users.get(user_ids = event.user_id)
                            if event.from_user: #Если написали в ЛС
                                sendMessage(user_id=event.user_id,chat_id=None,attachment=None,random_id=get_random_id(),message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name'])
                          #      vk.messages.send( #Отправляем сообщение
                          #          user_id=event.user_id,
                          #          random_id=get_random_id(),
                          #          message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name']
		                        #)
                                break
                            elif event.from_chat: #Если написали в Беседе
                                sendMessage(user_id=None,chat_id=event.chat_id,attachment=None,random_id=get_random_id(),message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name'])
                          #      vk.messages.send( #Отправляем собщение
                          #          chat_id=event.chat_id,
                          #          random_id=get_random_id(),
                          #          message='Привет, ' + profile[0]['first_name'] + ' ' + profile[0]['last_name']
		                        #)
                                break

    except vk_api.Captcha as e:
        captcha_handler(e.url)