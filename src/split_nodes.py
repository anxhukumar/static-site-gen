from textnode import TextNode, TextType
from extract_md_img_link import extract_markdown_images, extract_markdown_links

# function to split text type
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for node in old_nodes:
        # if node is not text type add as it is
        if node.text_type != TextType.TEXT:
            res.append(node)
        else:
            # show error if the number of delimiter is odd
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Closing or opening delimiter not found")
            split_node = node.text.split(delimiter)
            for i in range(len(split_node)):
                if i%2 != 0 and split_node[i]:
                    node = TextNode(split_node[i], text_type)
                    res.append(node)
                elif split_node[i]:
                    node = TextNode(split_node[i], TextType.TEXT)
                    res.append(node)
    return res

# function to split image type
def split_nodes_image(old_nodes):
    res = []
    for node in old_nodes:
        # Extract all image markdown tuples (alt text, URL) from the node's text
        image_tuple_array = extract_markdown_images(node.text)
        if image_tuple_array:
            node_text = node.text
            for image in image_tuple_array:
                # Split the text at the first occurrence of the image markdown
                split_node_text = node_text.split(f"![{image[0]}]({image[1]})", 1)
                # If there's text before the image, add it as a TEXT node
                if split_node_text[0]:
                    res.append(TextNode(split_node_text[0], node.text_type))
                # Add the image as an IMAGE node
                res.append(TextNode(image[0], TextType.IMAGE, image[1]))
                # Update the remaining text after the image
                node_text = split_node_text[1]
            # Add any remaining text after the last image
            if node_text:
                res.append(TextNode(node_text, node.text_type))
        else:
            # If no image markdown found, keep the node as is
            res.append(node)
    return res

# function to split link type
def split_nodes_link(old_nodes):
    res = []
    for node in old_nodes:
        # Extract all link markdown tuples (link text, URL) from the node's text
        link_tuple_array = extract_markdown_links(node.text)
        if link_tuple_array:
            node_text = node.text
            for link in link_tuple_array:
                # Split the text at the first occurrence of the link markdown
                split_node_text = node_text.split(f"[{link[0]}]({link[1]})", 1)
                # If there's text before the link, add it as a TEXT node
                if split_node_text[0]:
                    res.append(TextNode(split_node_text[0], node.text_type))
                # Add the link as a LINK node
                res.append(TextNode(link[0], TextType.LINK, link[1]))
                # Update the remaining text after the link
                node_text = split_node_text[1]
            # Add any remaining text after the last link
            if node_text:
                res.append(TextNode(node_text, node.text_type))
        else:
            # If no link markdown found, keep the node as is
            res.append(node)
    return res