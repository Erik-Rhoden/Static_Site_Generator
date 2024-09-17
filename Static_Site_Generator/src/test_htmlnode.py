import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "text", None, {"href": "https://www.google.com", "target": "_blank"})
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_repr(self):
        node = HTMLNode("a", "text", None, {"href": "https://www.google.com", "target": "_blank"})
        result = "Tag: a, Value: text, Children: None, Props: {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(node.__repr__(), result)

    def test_no_args(self):
        node = HTMLNode(None, None, None, None)
        result = "Tag: None, Value: None, Children: None, Props: None"
        self.assertEqual(node.__repr__(), result)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), result)

    def test_no_tag(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        result = "Click me!"
        self.assertEqual(node.to_html(), result)

    def test_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertRaises(ValueError)

    def test_no_children(self):
        node = LeafNode("p", "Hello, world!")
        result = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), result)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), result)

    def test_to_html_props(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"}
        )
        result = '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>'
        self.assertEqual(node.to_html(), result)

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
            ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = '<p><p>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), result)

    def test_no_children(self):
        node = ParentNode(
            "a",
             [],
            {"href": "https://www.google.com"}
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        result = '<div><span><b>grandchild</b></span></div>'
        self.assertEqual(parent_node.to_html(), result)

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = '<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>'
        self.assertEqual(node.to_html(), result)

if __name__ == "__main__":
    unittest.main()
