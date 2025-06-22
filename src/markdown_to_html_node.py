from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    # array to store the main child node of div
    eldest_child_node = []
    # convert markdown to a list of blocks
    blocks = markdown_to_blocks(markdown)
    # loop for each block
    for b in blocks:
        # determine the type of block
        b_type = block_to_block_type(b)

        # based on the type of block create a new HTMLNode
        match b_type:
            case BlockType.PARAGRAPH:
               # array of each paragraph
                para = b.split("\n\n")
                for p in para:
                    # convert each paragraph to text node
                    text_node = text_to_textnodes(p)
                    # array to store the converted text_nodes to html_nodes
                    leafnodes = []
                    # conversion of text nodes to html nodes
                    for tn in text_node:
                        leafnodes.append(text_node_to_html_node(tn))
                    # adding the paragraph node to eldest child node
                    eldest_child_node.append(ParentNode("p", leafnodes))
            case BlockType.HEADING:
                for l in b.split("\n"):
                    count_hashtag = len(l.split(" ", 1)[0])
                    text = l.split(" ", 1)[1]
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    eldest_child_node.append(ParentNode(f"h{count_hashtag}", leafnodes))
            case BlockType.CODE:
                code = b.split("```")[1].lstrip()
                eldest_child_node.append(ParentNode("pre", [ParentNode("code", [LeafNode(code)])]))
            case BlockType.QUOTE:
                lines = b.split("\n")
                for l in lines:
                    text = l.split(">")[1].strip()
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    eldest_child_node.append(ParentNode("blockquote", leafnodes))
            case BlockType.UNORDERED_LIST:
                lines = b.split("\n")
                li_nodes = []
                for l in lines:
                    text = l.split("-")[1].strip()
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    li_nodes.append(ParentNode("li", leafnodes))
                eldest_child_node.append(ParentNode("ul", li_nodes))
            case BlockType.ORDERED_LIST:
                lines = b.split("\n")
                li_nodes = []
                for l in lines:
                    text = l.split('.')[1].strip()
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    li_nodes.append(ParentNode("li", leafnodes))
                eldest_child_node.append(ParentNode("ol", li_nodes))
                
    return ParentNode("div", eldest_child_node).to_html()
