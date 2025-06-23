import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    # test extract title from H1
    def test_extract_title_only_h1(self):
        md = """
# This is a heading
"""
        output = extract_title(md)
        self.assertEqual(output, "This is a heading")

    # test extract title from a group of headings
    def test_extract_title_from_group_of_heading(self):
        md = """
### This is not heading
##### This is not heading
# This is the only heading
## This is not heading
"""
        output = extract_title(md)
        self.assertEqual(output, "This is the only heading")

    # test extract title without H1 to check error
    def test_extract_title_without_h1(self):
        md = """
### This is not heading
##### This is not heading
## This is not heading
"""
        self.assertRaises(Exception, extract_title, md)
        


if __name__ == "__main__":
    unittest.main()