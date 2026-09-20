import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the exact pC.map rendering code with surrounding context
idx = content.find('pC.map(r=>')
if idx == -1:
    print("ERROR: pC.map not found")
    exit(1)

# Get a chunk to see the full rendering call
chunk = content[idx:idx+1000]
print("RENDERING CODE:")
print(chunk)
print()

# Also show what the current pC looks like
match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    print("CURRENT pC DATA:")
    print(match.group(0)[:300])
