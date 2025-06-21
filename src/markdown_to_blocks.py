
def markdown_to_blocks(markdown):
    md_blocks = markdown.split("\n\n")
    refined_blocks = []
    for b in md_blocks:
        b = b.strip()
        if b:
            refined_blocks.append(b)
    return refined_blocks