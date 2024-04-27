
class HTMLNode:
    """
    Represents an HTML node.
    """

    def __init__(self=None, tag=None, value=None, children=None, props=None):
        """
        Initializes an HTMLNode object.

        Args:
            tag (str): The HTML tag of the node.
            value (str): The value/content of the node.
            children (list): The list of child nodes.
            props (dict): The dictionary of node properties.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        """
        Converts the HTMLNode object to an HTML string.

        Returns:
            str: The HTML string representation of the node.
        """
        return NotImplemented

    def props_to_html(self):
        """
        Converts the node properties to HTML attribute string.

        Returns:
            str: The HTML attribute string.
        """
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        """
        Returns a string representation of the HTMLNode object.

        Returns:
            str: The string representation of the node.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """
    Represents a leaf node in the HTML tree.
    """

    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode object.

        Args:
            tag (str): The HTML tag of the node.
            value (str): The value/content of the node.
            props (dict): The dictionary of node properties.
        """
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        """
        Converts the LeafNode object to an HTML string.

        Returns:
            str: The HTML string representation of the node.
        """
        if self.value is None:
            raise ValueError("Leaf nodes require a value.")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        """
        Returns a string representation of the LeafNode object.

        Returns:
            str: The string representation of the node.
        """
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"


class ParentNode(HTMLNode):
    """
    Represents a parent node in the HTML tree.
    """

    def __init__(self, tag, children, props=None):
        """
        Initializes a ParentNode object.

        Args:
            tag (str): The HTML tag of the node.
            children (list): The list of child nodes.
            props (dict): The dictionary of node properties.
        """
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        """
        Converts the ParentNode object to an HTML string.

        Returns:
            str: The HTML string representation of the node.
        """
        if self.tag is None:
            raise ValueError("Parent nodes require a tag.")

        if self.children is None:
            raise ValueError("Parent nodes require children.")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        """
        Returns a string representation of the ParentNode object.

        Returns:
            str: The string representation of the node.
        """
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"
