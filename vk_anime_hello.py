import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType, VkLongpollMode
from pprint import pprint
from threading import Thread
from time import sleep
from random import randint

anime_set = set(['в','Ской','ты','вам','бан','Хэйтер','аниме', 'анима', 'онеме', 'Ня', 'говно','Аниме','ОНЕМЕ','Алиса','Привет','Саня','дороу','привет','Здарова','Ты','Я','ты','не','мы'])

class VkLongPollThread(Thread):

    def __init__(self, api, period):
        Thread.__init__(self,target=self.event_handler)
        self.vk_met = api.get_api() 
        self.stop_flag = False
        self.longpoll = VkLongPoll(vk = api, mode = VkLongpollMode.GET_EXTENDED, preload_messages = True)
        self.period = period

    def event_handler(self):
        while(self.stop_flag == False):
            try:
                event_list = self.longpoll.check()
                for event in event_list:
                    if event.type == VkEventType.MESSAGE_NEW:
                        msg = event.message_data
                        user = self.vk_met.users.get(user_id = msg['from_id'])
                        print(user[0]['first_name'] + ' ' + user[0]['last_name'] + ': ' + msg['text'])
                        if msg['peer_id'] == 2000000182 and (anime_set.intersection(set(msg['text'].split())))!=set() and msg['from_id'] != 94734732:
                            self.vk_met.messages.send(peer_id = msg['peer_id'], message = 'Привет =)', random_id = randint(0, 0xFFFFFFFFFFFFFFFF))
            except:
                print('error occured')

            sleep(self.period)


    def stop(self):
        self.stop_flag = True
        


if __name__ == '__main__':
    access_file = open('access.json')
    access_dict = json.load(access_file)
    access_file.close()
    login = access_dict['access_list']['login']
    password = access_dict['access_list']['password']
    api = vk_api.VkApi(login = login, password = password)
    api.auth(token_only=True)
    vk = api.get_api()
    longpoll_th = VkLongPollThread(api = api, period = 0.02)
    longpoll_th.start()
   
    
    #pprint(vk.messages.search(q = 'аниме', peer_id = '2000000182'))