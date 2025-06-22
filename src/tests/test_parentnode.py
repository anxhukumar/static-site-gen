import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    # test to_html with children
    def test_to_html_with_children(self):
        child_node = LeafNode( "child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    # test to_html with grandchildren
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode( "grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    # test to_html with props
    def test_to_html_with_props(self):
        grandchild_node = LeafNode( "grandchild", "b", {"href": "yahoo.com"})
        child_node = ParentNode("span", [grandchild_node], {"href": "google.com"})
        parent_node = ParentNode("div", [child_node], {"href": "anxhukumar.com"})
        self.assertEqual(
            parent_node.to_html(),
            '<div href="anxhukumar.com"><span href="google.com"><b href="yahoo.com">grandchild</b></span></div>',
        )
    # test to_html without tag to check value error
    def test_to_html_without_tag(self):
        grandchild_node = LeafNode( "grandchild", "b")
        child_node = ParentNode(None, [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
    
    # test to_html without children to check value error
    def test_to_html_without_children(self):
        grandchild_node = LeafNode( "grandchild", "b")
        child_node = ParentNode("b", None)
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_eq(self):
        node = ParentNode("div", [ParentNode("div", [LeafNode( "grandchild", "b")])])
        node2 = ParentNode("div", [ParentNode("div", [LeafNode( "grandchild", "b")])])
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()