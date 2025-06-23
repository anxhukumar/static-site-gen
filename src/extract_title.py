def extract_title(markdown):
    for item in markdown.split("\n"):
        if item.startswith('# '):
            return item.split('#')[1].strip()
    raise Exception("H1 doesn't exist")