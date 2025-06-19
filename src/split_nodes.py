from textnode import TextNode, TextType

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