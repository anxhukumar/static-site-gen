import unittest
from leafnode import LeafNode

class TestLeaftNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_value_missing(self):
        node = LeafNode(None, tag="h1")
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_only_value(self):
        node = LeafNode(value="Hello world")
        self.assertEqual(node.to_html(), "Hello world")
    
    def test_to_html_props_given(self):
        node = LeafNode("Hello, world!", "p", {"href": "anxhukumar.com"})
        self.assertEqual(node.to_html(), '<p href="anxhukumar.com">Hello, world!</p>')
    
    def test_eq(self):
        node = LeafNode("I am hiking", "h1")
        node2 = LeafNode("I am hiking", "h1")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()