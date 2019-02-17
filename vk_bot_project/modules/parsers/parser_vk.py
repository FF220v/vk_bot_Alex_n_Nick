#Uniform interface for all parser modules
from ..content import Content
import json
from parser_interface import Parser

class ParserVk(Parser):

    def __init__(self):
        self.content = Content()        

    def get_content(self) -> Content:
        return self.content
    
    #following methods are ment to be implemented

    def parse(self):
        raise NotImplementedError

    