import unittest

from textnode import (
    TextNode, 
    text_type_bold, 
    text_type_italic,
    text_type_text,
    text_type_link,
    text_type_image,
    text_type_code,
    text_node_to_html_node
)
from split_delimiter import *



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_italic)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.google.com")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", text_type_bold, None)
        node2 = TextNode("This is a text node", text_type_bold, None)
        self.assertEqual(node, node2)

    def test_text_conversion(self):
        text_node = TextNode("sample text", text_type_text)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "sample text")

    def test_bold_conversion(self):
        text_node = TextNode("bold text", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_link_conversion(self):
        text_node = TextNode("link text", text_type_link, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link text")

    def test_img_conversion(self):
        text_node = TextNode("img text", text_type_image, url="http://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

    def test_italic_conversion(self):
        text_node = TextNode("italic text", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")

    def test_code_conversion(self):
        text_node = TextNode("code text", text_type_code)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code text")
        

if __name__ == "__main__":
    unittest.main()