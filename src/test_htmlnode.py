import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

    def test_leaf_node_to_html(self):
        node = LeafNode(tag='span', value='Leaf node', props={'class': 'leaf'})
        self.assertEqual(node.to_html(), '<span class="leaf">Leaf node</span>')

    def test_leaf_node_to_html_no_value(self):
        node = LeafNode(tag='span', value=None, props={'class': 'leaf'})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_to_html(self):
        child1 = LeafNode(tag='span', value='Child 1', props={'class': 'child'})
        child2 = LeafNode(tag='span', value='Child 2', props={'class': 'child'})
        node = ParentNode(tag='div', children=[child1, child2], props={'class': 'parent'})
        self.assertEqual(node.to_html(), '<div class="parent"><span class="child">Child 1</span><span class="child">Child 2</span></div>')

    def test_parent_node_to_html_no_tag(self):
        child = LeafNode(tag='span', value='Child', props={'class': 'child'})
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=[child], props={'class': 'parent'})
            node.to_html()

    def test_parent_node_to_html_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag='div', children=None, props={'class': 'parent'})
            node.to_html()

if __name__ == '__main__':
    unittest.main()