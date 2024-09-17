import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        print(f"Processing directory: {root}")
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, dir_path_content)
                html_dir = os.path.join(dest_dir_path, relative_path)
                html_path = os.path.join(html_dir, file[:-3] + '.html')
                print(f"Markdown file: {md_path}")
                print(f"HTML file: {html_path}")
                os.makedirs(os.path.dirname(html_path), exist_ok=True)
                generate_page(md_path, template_path, html_path)
                print(f"Generated: {html_path}")

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")