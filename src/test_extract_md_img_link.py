import unittest
from extract_md_img_link import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImgLink(unittest.TestCase):
    def test_extract_multiple_markdown_images(self):
        text = (
            "Here is one ![first](https://i.imgur.com/first.png)"
            " and another ![second](https://i.imgur.com/second.png)"
            "![third](https://i.imgur.com/third.png)"
            " some text in between ![fourth image](https://i.imgur.com/fourth.png)."
            " Random text ![fifth](https://i.imgur.com/fifth.png)!"
        )

        expected = [
            ("first", "https://i.imgur.com/first.png"),
            ("second", "https://i.imgur.com/second.png"),
            ("third", "https://i.imgur.com/third.png"),
            ("fourth image", "https://i.imgur.com/fourth.png"),
            ("fifth", "https://i.imgur.com/fifth.png"),
        ]

        matches = extract_markdown_images(text)
        self.assertListEqual(expected, matches)

    def test_extract_multiple_markdown_links(self):
        text = (
            "This is a [Google](https://www.google.com) link."
            " Here's [OpenAI](https://openai.com)."
            " Some more text [GitHub](https://github.com) is here."
            " [Docs](https://docs.python.org/3/) and another [Example](http://example.com/page)."
        )

        expected = [
            ("Google", "https://www.google.com"),
            ("OpenAI", "https://openai.com"),
            ("GitHub", "https://github.com"),
            ("Docs", "https://docs.python.org/3/"),
            ("Example", "http://example.com/page"),
        ]

        matches = extract_markdown_links(text)
        self.assertListEqual(expected, matches)


if __name__ == "__main__":
    unittest.main()