import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    # test for code
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("`code block` This is text with a `code block` word and `code block`", TextType.TEXT)
        output = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        expected_output = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word and ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(output, expected_output)
    
    # test for bold
    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold word** here", TextType.TEXT)
        node2 = TextNode("**bold text** This is text with **multiple bold** sections and **more bold**", TextType.TEXT)
        output = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        expected_output = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold word", TextType.BOLD),
        TextNode(" here", TextType.TEXT),
        TextNode("bold text", TextType.BOLD),
        TextNode(" This is text with ", TextType.TEXT),
        TextNode("multiple bold", TextType.BOLD),
        TextNode(" sections and ", TextType.TEXT),
        TextNode("more bold", TextType.BOLD),
        ]
        self.assertEqual(output, expected_output)
    
    # test for italic
    def test_split_nodes_italic(self):
        node = TextNode("This is text with an *italic word* here", TextType.TEXT)
        node2 = TextNode("*italic text* This is text with *multiple italic* sections and *more italic*", TextType.TEXT)
        output = split_nodes_delimiter([node, node2], "*", TextType.ITALIC)
        expected_output = [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic word", TextType.ITALIC),
        TextNode(" here", TextType.TEXT),
        TextNode("italic text", TextType.ITALIC),
        TextNode(" This is text with ", TextType.TEXT),
        TextNode("multiple italic", TextType.ITALIC),
        TextNode(" sections and ", TextType.TEXT),
        TextNode("more italic", TextType.ITALIC),
        ]
        self.assertEqual(output, expected_output)
    
    # test for invalid number of delimiters in text
    def test_invalid_delimiter_count(self):
        node = TextNode("This is text with an unclosed `code block", TextType.TEXT)
        node2 = TextNode("This has **unclosed bold formatting*", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)
        self.assertRaises(Exception, split_nodes_delimiter, [node2], "**", TextType.BOLD)
    
    # test with a node that is not text type
    def test_non_text_type(self):
        node = TextNode("_italic_", TextType.ITALIC)
        node2 = TextNode("This is text with a **bold word** here", TextType.TEXT)
        output = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        expected_output = [
        TextNode("_italic_", TextType.ITALIC),
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold word", TextType.BOLD),
        TextNode(" here", TextType.TEXT)
        ]
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()