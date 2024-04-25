from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode


def main():
    node = TextNode("This is a test node", "bold", "https://www.cudabu.io")
    print(node)

    node = HTMLNode(tag='a', value='www.cudabu.io', children=[], props={'href': 'https://www.cudabu.io', 'target': '_blank'})
    print(node)

    node = LeafNode(tag='span', value='Leaf node', props={'class': 'leaf'})
    print(node)

main()