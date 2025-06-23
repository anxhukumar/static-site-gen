from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        md = f.read()
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    content = markdown_to_html_node(md)
    print(content)
    title = extract_title(md)

    template_split = template.split("\n")

    for i in range(len(template_split)):
        if "<title>" in template_split[i]:
            line_splitted = template_split[i].split("{{ Title }}")
            line_splitted.insert(1, f"{title}")
            line = "".join(line_splitted)
            template_split[i] = line
        if "<article>" in template_split[i]:
            line_splitted = template_split[i].split("{{ Content }}")
            line_splitted.insert(1, f"{content}")
            line = "".join(line_splitted)
            template_split[i] = line

    template = "\n".join(template_split)

    print(template)


