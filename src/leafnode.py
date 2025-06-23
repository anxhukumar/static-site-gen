from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,  value, tag=None,props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value is missing")
        if self.tag:
            if self.props:
                props = self.props_to_html()
                if self.tag == "img":
                    return f'<{self.tag} {props}/>'
                return f'<{self.tag} {props}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return self.value