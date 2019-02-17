#Uniform module which stores data
from pprint import pprint

class Content:

    default_dict = {
        'source_name':'',
        'source_id':'',
        'url':'',
        'attachments':'',
        'image':'',
        'comments':'',
        'likes':'',
        'dislikes':'',
        'rate':'',
        'time':'',
    }

    def __init__(self, default_dict = default_dict):
        self.content_table = [default_dict]

    def get_content_table(self) -> list:
        return self.content_table
    
    def get_element(self ,index):
        return self.content_table[index]

    def get_field(self,index,field):
        return self.content_table[index][field]

    def set_field(self,index:int,field:str,data:dict):
        if len(self.content_table)<=index:
            self._init_element(index)
        print(len(self.content_table))
        self.content_table[index][field] = data
    
    def _init_element(self, index):
        while index >= len(self.content_table):
            self.content_table.append(Content.default_dict)

    
cont = Content()
cont.set_field(0,'url','hello')
cont.set_field(1,'source_name','hello')
pprint(cont.get_content_table())

