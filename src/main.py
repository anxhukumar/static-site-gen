from static_to_public import static_to_public
from generate_page import generate_pages_recursive
import shutil
import sys
import os

if len(sys.argv) > 1:
        base_path = sys.argv[1]
else:
        base_path = "/"

# delete all the contents of public directory
if os.path.exists("./docs"):
        shutil.rmtree("./docs")

# copying all the content of static and pasting to public
static_to_public("./static", "./docs")

# generate page
generate_pages_recursive("./content", "./template.html", "./docs", base_path)