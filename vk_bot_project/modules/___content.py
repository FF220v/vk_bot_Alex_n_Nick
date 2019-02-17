#Uniform module which stores data
from pprint import pprint

class Content:

    default_dict = {
        'order':'',
        'source_name':'',
        'id':'',
        'url':'',
        'text':'',
        'attachments':'',
        'image_url':'',
        'comments':'',
        'likes':'',
        'dislikes':'',
        'rate':'',
        'time':'',
    }

    def __init__(self):
        self.content_table = []
        self.index = 0

    def get_content_table(self) -> list:
        return self.content_table
    
    def get_element(self ,index):
        return self.content_table[index]

    def get_field(self,index,field):
        return self.content_table[index][field]

    def next(self):
        self.index+=1
        self.content_table.append(Content.default_dict)
        self.content_table[self.index]['order'] = self.index


    def set_field(self,field:str, data):
        self.content_table[self.index][field] = data
    
    def set_source_name(self, data):
        self.content_table[self.index]['source_name'] = data
    
    def set_id(self, data):
        self.content_table[self.index]['id'] = data

    def set_url(self, data):
        self.content_table[self.index]['url'] = data

    def set_text(self, data):
        self.content_table[self.index]['text'] = data
    
    def set_attachments(self, data):
        self.content_table[self.index]['attachments'] = data
    
    def set_image_url(self, data):
        self.content_table[self.index]['image_url'] = data
    
    def set_comments(self, data):
        self.content_table[self.index]['comments'] = data
    
    def set_likes(self, data):
        self.content_table[self.index]['likes'] = data
    
    def set_dislikes(self, data):
        self.content_table[self.index]['dislikes'] = data
    
    def set_rate(self, data):
        self.content_table[self.index]['rate'] = data

    def set_time(self, data):
        self.content_table[self.index]['time'] = data
    
 
