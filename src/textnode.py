text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode(tag='code', value=text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url, 'target': '_blank'})
    elif text_node.text_type == text_type_image:
        return LeafNode(tag='img', value=None, props={'src': text_node.url, 'alt': text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            new_nodes.extend(
                TextNode(text, text_type_text)
                for text in node.text.split(delimiter)
            )
        else:
            new_nodes.append(node)
