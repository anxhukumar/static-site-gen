from static_to_public import static_to_public
from generate_page import generate_pages_recursive
import shutil
import sys
import os


# delete all the contents of public directory
if os.path.exists("./public"):
        shutil.rmtree("./public")

# copying all the content of static and pasting to public
static_to_public("./static", "./public")

base_path = sys.argv[1]
if not base_path:
        base_path = "/"

# generate page
generate_pages_recursive("./content", "./template.html", "./docs", base_path)