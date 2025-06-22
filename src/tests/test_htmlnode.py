import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "I am hiking")
        node2 = HTMLNode("h1", "I am hiking")
        self.assertEqual(node, node2)
    
    def test_when_children_props_given(self):
        node = HTMLNode("h1", "I am hiking", HTMLNode("h2", "I am sleeping"), {"href": "www.google.com"})
        node2 = HTMLNode("h1", "I am hiking", HTMLNode("h2", "I am sleeping"), {"href": "www.google.com"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("h1", "I am hiking", HTMLNode("h2", "I am sleeping"), {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="www.google.com"')

if __name__ == "__main__":
    unittest.main()