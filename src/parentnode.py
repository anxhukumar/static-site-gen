from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is missing")
        if not self.children:
            raise ValueError("Child is missing")
        
        if self.props:
            props = self.props_to_html()

        str = ""

        for c in self.children:
                str += f'{c.to_html()}'
        
        if self.props:
             return f'<{self.tag} {props}>{str}</{self.tag}>'
        else:
             return f'<{self.tag}>{str}</{self.tag}>'
        