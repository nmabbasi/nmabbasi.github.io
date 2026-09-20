import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# 1. Correct the organisation string
old_org = 'organisation:"Spain, Sweden, Pakistan and clinical research teams"'
new_org = 'organisation:"Multiple Research Institutes"'
if old_org in content:
    content = content.replace(old_org, new_org)
    print("Fixed earlier roles organisation")
    changes += 1

# 2. Make Google Scholar links clearer
if ">[Link]<" in content:
    content = content.replace(">[Link]<", ">[Google Scholar]<")
    print("Clarified Google Scholar links")
    changes += 1

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
