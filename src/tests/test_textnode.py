import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_when_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_when_url_given(self):
        node = TextNode("This is a text node", TextType.LINK, "anxhukumar.com")
        node2 = TextNode("This is a text node", TextType.LINK, "anxhukumar.com")
        self.assertEqual(node, node2)
    
    def test_when_texttype_differ(self):
        node = TextNode("This is a text node", TextType.ITALIC, "anxhukumar.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "anxhukumar.com")
        self.assertNotEqual(node, node2)
    
    # test text_node_to_html_node functions:-

    # test text type
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    # test bold type
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("This is a text node", "b"))
    # test italic type
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("This is a text node", "i"))

    # test code type
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("This is a text node", "code"))

    # test link type
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("This is a text node", "a", {"href": "https://example.com"}))

    # test image type
    def test_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("", "img", {"alt": "This is alt text", "src": "https://example.com/image.jpg"}))

    # test invalid type
    def test_invalid(self):
        node = TextNode("This is alt text", None)
        self.assertRaises(Exception, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()