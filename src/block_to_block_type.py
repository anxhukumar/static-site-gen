from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # Check for heading: look for # symbols at the start of the first word
    if "#" in block.split(" ", 1)[0] and len(block.split(" ", 1))>1:
        if len(block.strip().split("\n")) == 1:
            count = 0
            # Count the number of consecutive # symbols
            for c in block.split(" ", 1)[0]:
                if c=="#":
                    count += 1
            # Valid markdown headings have 1-6 # symbols
            if 1 <= count <= 6: 
                return BlockType.HEADING
    
    # Check for code block: must start and end with triple backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote block: all non-empty lines must start with >
    if ">" in block.split(" ", 1)[0]:
        res = False
        # Verify every non-empty line starts with >
        for line in block.split("\n"):
            if len(line) > 0:
                if line.startswith(">"):
                    res = True
                else:
                    # If any line doesn't start with >, it's not a quote block
                    res = False
                    break
        if res:
            return BlockType.QUOTE
    
    # Check for unordered list: all non-empty lines must start with "- "
    if "-" in block.split(" ", 1)[0]:
        res = False
        # Verify every non-empty line starts with "- "
        for line in block.split("\n"):
            if len(line) > 0:
                if line.startswith("- "):
                    res = True
                else:
                    # If any line doesn't start with "- ", it's not an unordered list
                    res = False
                    break
        if res:
            return BlockType.UNORDERED_LIST
    
    # Check for ordered list: must start with a number followed by ". "
    if block.split(". ", 1)[0].strip().isdigit():
            res = False
            num = 0
            # Verify each line follows the pattern "1. ", "2. ", "3. ", etc.
            for line in block.split("\n"):
                if len(line) > 0:
                    num += 1
                    # Check if line starts with the expected sequential number
                    if line.startswith(f"{str(num)}. "):
                        res = True
                    else:
                        # If numbering is not sequential, it's not an ordered list
                        res = False
                        break
            if res:
                return BlockType.ORDERED_LIST
    
    # Default case: if none of the above patterns match, it's a paragraph
    return BlockType.PARAGRAPH