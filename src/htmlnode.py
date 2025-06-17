
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    # returns a string that represents the HTML attributes
    def props_to_html(self):
        res = ""
        for key in self.props:
            res = res + f'{key}="{self.props[key]}" '
        return res.strip()
    
    # checks if two nodes have same properties
    def __eq__(self, html_node):
        return self.tag == html_node.tag and self.value == html_node.value and self.children == html_node.children and self.props == html_node.props

    #  gives a string representation of the TextNode object
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'