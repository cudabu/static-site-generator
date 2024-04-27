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
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag=None, value="This is a text node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a bold node", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag='b', value="This is a bold node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is an italic node", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag='i', value="This is an italic node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a code node", text_type_code)
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag='code', value="This is a code node")
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("This is a link node", text_type_link, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag='a', value="This is a link node", props={'href': 'https://www.example.com', 'target': '_blank'})
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is an image node", text_type_image, "https://www.example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        expected_html_node = LeafNode(tag='img', value=None, props={'src': 'https://www.example.com/image.jpg', 'alt': 'This is an image node'})
        self.assertEqual(html_node, expected_html_node)

    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("This is an invalid node", "invalid_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()