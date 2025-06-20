import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    # test textnode with bold, italic, and code types
    def test_bold_italic_code_combination(self):
        text = "This has **bold**, _italic_, and `code` in one line."
        output = text_to_textnodes(text)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in one line.", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with only bold type
    def test_only_bold(self):
        text = "This is **just bold** text."
        output = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("just bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with only italic type
    def test_only_italic(self):
        text = "This is _just italic_ text."
        output = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("just italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with only code type
    def test_only_code(self):
        text = "This is `just code` text."
        output = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("just code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with image and link, without bold, italic, or code
    def test_image_and_link_only(self):
        text = "Here is a [link](https://example.com) and an ![image](https://example.com/image.png)."
        output = text_to_textnodes(text)
        expected = [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with image and link, and also bold, italic, and code
    def test_all_features(self):
        text = "**Bold**, _italic_, and `code`, with a [link](https://example.com) and an ![image](https://example.com/img.png)."
        output = text_to_textnodes(text)
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    # test textnode with image only
    def test_only_image(self):
        text = "![alt text](https://example.com/img.png)"
        output = text_to_textnodes(text)
        expected = [
            TextNode("alt text", TextType.IMAGE, "https://example.com/img.png"),
        ]
        self.assertEqual(output, expected)

    # test textnode with link only
    def test_only_link(self):
        text = "[click here](https://example.com)"
        output = text_to_textnodes(text)
        expected = [
            TextNode("click here", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()