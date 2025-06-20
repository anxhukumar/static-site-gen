from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    if "**" in text:
        text_node = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    if "_" in text:
        text_node = split_nodes_delimiter(text_node, "_", TextType.ITALIC)
    if "`" in text:
        text_node = split_nodes_delimiter(text_node, "`", TextType.CODE)
    
    return split_nodes_image(split_nodes_link(text_node))