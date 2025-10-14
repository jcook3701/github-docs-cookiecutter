import re
from pathlib import Path

def remove_raw_tags(file_path: Path):
    """Remove Jinja-style {% raw %} and {% endraw %} tags from the given file."""
    text = file_path.read_text(encoding="utf-8")
    cleaned = re.sub(r"{%\s*raw\s*%}", "", text)
    cleaned = re.sub(r"{%\s*endraw\s*%}", "", cleaned)
    file_path.write_text(cleaned, encoding="utf-8")

def main():
    index_path = Path("index.md")
    if index_path.exists():
        remove_raw_tags(index_path)

if __name__ == "__main__":
    main()
