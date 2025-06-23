from static_to_public import static_to_public
from generate_page import generate_page
import os
import shutil


# delete all the contents of public directory
if os.path.exists("./public"):
        shutil.rmtree("./public")

# copying all the content of static and pasting to public
static_to_public("./static", "./public")

# generate page
generate_page("./content/index.md", "./template.html", "./public/index.html")