from enum import Enum
from leafnode import LeafNode

# enums for all types of text nodes
class TextType(Enum):
    TEXT = "normal"
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

    # checks if two nodes have same properties
    def __eq__(self, text_node):
         return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
    
    # gives a string representation of the TextNode object
    def __repr__(self):
        return f'TextNode({self.text, self.text_type.value, self.url})'
    
def text_node_to_html_node(text_node):
    type = text_node.text_type

    match type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINK:
            return LeafNode(text_node.text, "a", {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode(" ", "img", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
        case _:
            raise Exception("Invalid textnode type")