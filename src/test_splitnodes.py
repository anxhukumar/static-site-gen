import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    # test a node that contains image [split_nodes_image]
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). The End.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(". The End.", TextType.TEXT)
            ],
            new_nodes,
        )
    
    # test a node that contains only image and no text [split_nodes_image]
    def test_split_only_image(self):
        node = TextNode(
            "![only image](https://i.imgur.com/abcd123.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("only image", TextType.IMAGE, "https://i.imgur.com/abcd123.png"),
            ],
            new_nodes,
        )

    # test a node that contains only text and no image [split_nodes_image]
    def test_split_only_text(self):
        node = TextNode(
            "This is plain text with no images.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is plain text with no images.", TextType.TEXT),
            ],
            new_nodes,
        )

        # test a node that contains links [split_nodes_link]
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org). The End.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
                TextNode(". The End.", TextType.TEXT),
            ],
            new_nodes,
        )

    # test a node that contains only link and no text [split_nodes_link]
    def test_split_only_link(self):
        node = TextNode(
            "[only link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("only link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    # test a node that contains only text and no link [split_nodes_link]
    def test_split_only_text_link(self):
        node = TextNode(
            "This is plain text with no links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is plain text with no links.", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()