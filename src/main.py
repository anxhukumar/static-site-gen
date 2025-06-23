from static_to_public import static_to_public
import os
import shutil


# delete all the contents of public directory
if os.path.exists("./public"):
        shutil.rmtree("./public")

# copying all the content of static and pasting to public
static_to_public("./static", "./public")