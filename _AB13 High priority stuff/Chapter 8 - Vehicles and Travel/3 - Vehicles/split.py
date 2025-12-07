from pathlib import Path
import re

input_file = Path("Staging.md")
output_dir = Path("split")
output_dir.mkdir(exist_ok=True)

text = input_file.read_text(encoding="utf-8")

# Split on level-2 headings
sections = re.split(r'(?m)^## +', text)

for section in sections:
    if not section.strip():
        continue

    # First line becomes filename
    title, _, body = section.partition("\n")
    filename = re.sub(r'[^a-zA-Z0-9_-]+', "-", title.strip()).lower() + ".md"

    outpath = output_dir / filename
    outpath.write_text(f"## {title}\n{body}", encoding="utf-8")

print("Done! Files written to:", output_dir)
