from enum import Enum

#enums for all types of text nodes
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    #checks if two nodes have same properties
    def __eq__(self, text_node):
         return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
    
    #gives a string representation of the TextNode object
    def __repr__(self):
        return f'TextNode({self.text, self.text_type.value, self.url})'
