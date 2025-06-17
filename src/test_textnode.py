import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()