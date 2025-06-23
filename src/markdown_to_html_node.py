from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    # List to store the top-level child nodes of the resulting HTML div
    eldest_child_node = []
    
    # Convert the markdown string into a list of block strings
    blocks = markdown_to_blocks(markdown)
    
    # Iterate through each block to process it based on its type
    for b in blocks:
        # Determine the type of the block (e.g., paragraph, heading, list)
        b_type = block_to_block_type(b)

        # Use match-case to handle different block types
        match b_type:
            case BlockType.PARAGRAPH:
                # Join lines in the paragraph block into one string
                text = " ".join(b.split("\n"))
                # Convert text into a list of text nodes with inline formatting
                text_nodes = text_to_textnodes(text)
                leafnodes = []
                # Convert each text node to a corresponding HTML leaf node
                for tn in text_nodes:
                    leafnodes.append(text_node_to_html_node(tn))
                # Wrap the leaf nodes in a paragraph parent node and add to the list
                eldest_child_node.append(ParentNode("p", leafnodes))
            
            case BlockType.HEADING:
                for l in b.split("\n"):
                    # Count the number of '#' characters to determine heading level
                    count_hashtag = len(l.split(" ", 1)[0])
                    # Extract the actual heading text
                    text = l.split(" ", 1)[1]
                    # Convert heading text to text nodes with inline formatting
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    # Convert each text node to a corresponding HTML leaf node
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    # Wrap in appropriate heading tag (h1 to h6) and add to list
                    eldest_child_node.append(ParentNode(f"h{count_hashtag}", leafnodes))
            
            case BlockType.CODE:
                # Extract the code block content from between triple backticks
                code = b.split("```")[1].lstrip()
                # Wrap the code inside <code> and then inside <pre>, add to list
                eldest_child_node.append(ParentNode("pre", [ParentNode("code", [LeafNode(code)])]))
            
            case BlockType.QUOTE:
                # Split block into individual quote lines
                lines = b.split("\n")
                for l in lines:
                    # Remove the leading '>' and whitespace from each quote line
                    text = l.split(">")[1].strip()
                    # Convert quote text into text nodes
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    # Convert to HTML leaf nodes
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    # Wrap each line in a blockquote tag and add to list
                    eldest_child_node.append(ParentNode("blockquote", leafnodes))
            
            case BlockType.UNORDERED_LIST:
                # Split unordered list into lines
                lines = b.split("\n")
                li_nodes = []
                for l in lines:
                    # Remove the leading '-' and whitespace from each list item
                    text = l.split("-")[1].strip()
                    # Convert list item text into text nodes
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    # Convert to HTML leaf nodes
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    # Wrap in <li> and add to list
                    li_nodes.append(ParentNode("li", leafnodes))
                # Wrap all list items in a <ul> tag and add to main node list
                eldest_child_node.append(ParentNode("ul", li_nodes))
            
            case BlockType.ORDERED_LIST:
                # Split ordered list into lines
                lines = b.split("\n")
                li_nodes = []
                for l in lines:
                    # Remove the leading number and dot from each list item
                    text = l.split('.', 1)[1].strip()
                    # Convert list item text into text nodes
                    text_nodes = text_to_textnodes(text)
                    leafnodes = []
                    # Convert to HTML leaf nodes
                    for tn in text_nodes:
                        leafnodes.append(text_node_to_html_node(tn))
                    # Wrap in <li> and add to list
                    li_nodes.append(ParentNode("li", leafnodes))
                # Wrap all list items in an <ol> tag and add to main node list
                eldest_child_node.append(ParentNode("ol", li_nodes))
                
    # Return the top-level div node containing all child elements
    return ParentNode("div", eldest_child_node)