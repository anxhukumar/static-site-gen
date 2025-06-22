import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
        # test with a normal markdown
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        # test with a single line markdown
        def test_single_line_markdown(self):
            md = "Just a single line"
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["Just a single line"])

        # test with a markdown that has multiple spaces to test the elimination of empty blocks
        def test_multiple_spaces_and_empty_blocks(self):
            md = """

This is a paragraph


Another paragraph


"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a paragraph",
                    "Another paragraph",
                ],
            )

        # test with a markdown that has leading and trailing whitespaces
        def test_trailing_whitespaces(self):
            md = "  This has trailing spaces   \n\n  Another one with spaces   \n"
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This has trailing spaces",
                    "Another one with spaces",
                ],
            )

if __name__ == "__main__":
    unittest.main()