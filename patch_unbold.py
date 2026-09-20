import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    pc_data = match.group(0)
    
    # Revert to normal Abbasi N
    pc_data = pc_data.replace("<b>ABBASI N</b>", "Abbasi N")
    
    content = content.replace(match.group(0), pc_data)
    print("Reverted to normal text.")
else:
    print("Could not find pC array")
    sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully patched.")
