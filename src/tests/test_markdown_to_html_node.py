import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    # test paragraph block
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    # test code block
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    # test heading block with h1 to h6, including inline formatting
    def test_heading_blocks(self):
        md = """
# Heading One with **bold**

## Heading Two with _italic_

### Heading Three with `code`

#### Heading Four

##### Heading Five

###### Heading Six
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading One with <b>bold</b></h1><h2>Heading Two with <i>italic</i></h2><h3>Heading Three with <code>code</code></h3><h4>Heading Four</h4><h5>Heading Five</h5><h6>Heading Six</h6></div>",
        )

    # test quote block with inline markdown
    def test_quote_block(self):
        md = """
> This is a _quote_ with `inline code` and **bold text**
> Second line of the quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <i>quote</i> with <code>inline code</code> and <b>bold text</b></blockquote><blockquote>Second line of the quote</blockquote></div>",
        )

    # test unordered list block with inline markdown
    def test_unordered_list_block(self):
        md = """
- Item one with _italic_
- Item two with `code`
- Item three with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one with <i>italic</i></li><li>Item two with <code>code</code></li><li>Item three with <b>bold</b></li></ul></div>",
        )

    # test ordered list block with inline markdown
    def test_ordered_list_block(self):
        md = """
1. First item with _emphasis_
2. Second item with `inline code`
3. Third item with **strong text**
4. [link](https://www.google.com)
5. ![Description of image](url/of/image.jpg)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>First item with <i>emphasis</i></li><li>Second item with <code>inline code</code></li><li>Third item with <b>strong text</b></li><li><a href="https://www.google.com">link</a></li><li><img src="url/of/image.jpg" alt="Description of image"/></li></ol></div>',
        )


if __name__ == "__main__":
    unittest.main()