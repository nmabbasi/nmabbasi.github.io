import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the style attribute of these anchor tags
old_style = 'style=\\"text-decoration:none;font-weight:600;display:inline-block;margin-top:0.25rem;\\"'
new_style = 'style=\\"color:#2563eb;text-decoration:underline;text-underline-offset:4px;font-weight:600;display:inline-block;margin-top:0.25rem;cursor:pointer;\\"'

if old_style in content:
    content = content.replace(old_style, new_style)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed styling for links.")
else:
    print("Old style not found.")
