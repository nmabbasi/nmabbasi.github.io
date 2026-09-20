import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

old_text = '>[Google Scholar]<'
svg_icon = '<span style=\\"display:inline-flex;align-items:center;gap:4px;\\"><svg viewBox=\\"0 0 24 24\\" width=\\"14\\" height=\\"14\\" fill=\\"currentColor\\"><path d=\\"M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z\\"/></svg>Google Scholar</span>'
new_text = '>' + svg_icon + '<'

# Remove underline from the anchor tag and add some clean styling
if old_text in content:
    content = content.replace(old_text, new_text)
    
    # Let's also remove the underline styling from the anchor itself so the icon looks cleaner
    content = content.replace('style=\\"text-decoration:underline;\\"', 'style=\\"text-decoration:none;font-weight:600;display:inline-block;margin-top:0.25rem;\\"')
    
    print("Added Google Scholar SVG icons")
    changes += 1

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
