import unittest
from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    # test heading block
    def test_heading_block_type(self):
        md_block = "# Heading"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.HEADING)

    # test heading block with six "#"
    def test_heading_six_hashes(self):
        md_block = "###### Heading 6"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.HEADING)

    # test heading block with more than six "#"
    def test_heading_more_than_six_hashes(self):
        md_block = "####### Not a heading"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    # test code blocks with opening and closing backticks
    def test_code_block_correct(self):
        md_block = "```python\nprint('Hello')\n```"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.CODE)

    # test code blocks with only opening backticks
    def test_code_block_only_opening_backticks(self):
        md_block = "```python\nprint('Hello')"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    # test quote markdown with multiple lines to check if it works properly
    def test_quote_block_multiple_lines(self):
        md_block = ">This is a quote\n> spanning multiple lines"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.QUOTE)

    # test quote markdown with a line without the >
    def test_quote_block_with_non_quote_line(self):
        md_block = "> This is a quote\nThis line breaks the quote"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    # test unordered list with multiple lines to check if it works properly
    def test_unordered_list_multiple_lines(self):
        md_block = "- Item 1\n- Item 2\n- Item 3"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    # test unordered list with a line without the -
    def test_unordered_list_with_non_dash_line(self):
        md_block = "- Item 1\nItem 2"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    # test ordered list with multiple lines and proper numbers to check if it works properly
    def test_ordered_list_correct_numbers(self):
        md_block = "1. First\n2. Second\n3. Third"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.ORDERED_LIST)

    # test ordered list with wrong numbers
    def test_ordered_list_wrong_numbers(self):
        md_block = "1. First\n3. Not Second\n2. Not Third"
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)

    # test a string without any characters to check if it returns a paragraph type
    def test_plain_paragraph(self):
        md_block = "This is just a simple paragraph without any formatting."
        output = block_to_block_type(md_block)
        self.assertEqual(output, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()