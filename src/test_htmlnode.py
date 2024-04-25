import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag='div', value='Hello', children=[], props={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'container'})

    def test_to_html(self):
        node = HTMLNode(tag='p', value='Lorem ipsum', children=[], props=None)
        self.assertEqual(node.to_html(), NotImplemented)

    def test_props_to_html(self):
        node = HTMLNode(tag='a', value='Click me', children=[], props={'href': 'https://example.com'})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

if __name__ == '__main__':
    unittest.main()