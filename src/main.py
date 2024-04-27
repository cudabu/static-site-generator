from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode

def main():
    node = TextNode("This is a test node", "bold", "https://www.cudabu.io")
    print(node)

    node = HTMLNode(tag='a', value='www.cudabu.io', children=[], props={'href': 'https://www.cudabu.io', 'target': '_blank'})
    print(node)

    node = LeafNode(tag='span', value='Leaf node', props={'class': 'leaf'})
    print(node)

    node = ParentNode(tag='div', children=[LeafNode(tag='span', value='Leaf node', props={'class': 'leaf'})], props={'class': 'parent'})
    print(node)

main()