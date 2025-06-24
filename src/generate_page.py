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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Loop through all entries (files and directories) in the given content directory
    for f in os.listdir(path = dir_path_content):
        # Check if the entry is a file and ends with ".md" (i.e., a markdown file)
        if os.path.isfile(os.path.join(dir_path_content, f)) and os.path.join(dir_path_content, f).endswith(".md"):
            # Construct the full path to the markdown file
            new_dir_path = os.path.join(dir_path_content, f)
            # Create the corresponding output path with ".html" extension
            new_dest_path = os.path.join(dest_dir_path, f.replace(".md", ".html"))
            # Generate a single HTML page from the markdown file using the template
            generate_page(new_dir_path, template_path, new_dest_path)
        else:
            # Create the destination subdirectory if the entry is a directory
            os.makedirs(os.path.join(dest_dir_path, f))
            # Recursively process the contents of the subdirectory
            generate_pages_recursive(os.path.join(dir_path_content, f), template_path, os.path.join(dest_dir_path, f))
