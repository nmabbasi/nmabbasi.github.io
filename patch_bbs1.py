import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_url = "https://pubmed.ncbi.nlm.nih.gov/23559846/"
new_url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3605481/"

if old_url in content:
    content = content.replace(old_url, new_url)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced BBS1 link with PMC full text.")
else:
    print("Old URL not found.")
