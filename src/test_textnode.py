import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a bold node", text_type_bold)
        self.assertNotEqual(node, node2)


    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a bold node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.cudabu.io")
        node2 = TextNode("This is a text node", text_type_italic, "https://www.cudabu.io")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode("This is a text node", text_type_italic)
        node2 = TextNode("This is a text node", text_type_italic, "https://www.cudabu.io")
        self.assertNotEqual(node, node2)

    def test_report(self):
        node = TextNode("This is a text node", text_type_text, "https://www.cudabu.io")
        self.assertEqual("TextNode(This is a text node, text, https://www.cudabu.io)", repr(node))

if __name__ == "__main__":
    unittest.main()
