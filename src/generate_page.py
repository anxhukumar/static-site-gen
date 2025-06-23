from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown content from the source file
    with open(from_path, 'r') as f:
        md = f.read()
    
    # Read the HTML template from the template file
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Convert the markdown to HTML content
    content = markdown_to_html_node(md).to_html()
    # Extract the title from the markdown
    title = extract_title(md)

    # Split the template into lines for easier manipulation
    template_split = template.split("\n")

    # Iterate through each line of the template
    for i in range(len(template_split)):
        # If the line contains a <title> tag, insert the extracted title
        if "<title>" in template_split[i]:
            line_splitted = template_split[i].split("{{ Title }}")  # Split at the placeholder
            line_splitted.insert(1, f"{title}")  # Insert the title at the correct position
            line = "".join(line_splitted)  # Join the parts back into a single string
            template_split[i] = line  # Replace the original line with the updated one
        # If the line contains an <article> tag, insert the converted HTML content
        if "<article>" in template_split[i]:
            line_splitted = template_split[i].split("{{ Content }}")  # Split at the placeholder
            line_splitted.insert(1, f"{content}")  # Insert the content at the correct position
            line = "".join(line_splitted)  # Join the parts back into a single string
            template_split[i] = line  # Replace the original line with the updated one

    # Join the modified lines back into a full HTML string
    html = "\n".join(template_split)
    
    # Write the final HTML to the destination file
    with open(dest_path, "w") as f:
        f.write(html)