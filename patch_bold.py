import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the React rendering logic to use dangerouslySetInnerHTML
old_p_tag = 'S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:309",children:t}'
new_p_tag = 'S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:309",dangerouslySetInnerHTML:{__html:t}}'
if old_p_tag in content:
    content = content.replace(old_p_tag, new_p_tag)
    print("Replaced children:t with dangerouslySetInnerHTML")
else:
    # maybe it's already dangerouslySetInnerHTML?
    if new_p_tag in content:
        print("Already using dangerouslySetInnerHTML")
    else:
        print("Could not find old_p_tag")
        sys.exit(1)

# 2. Update pC array to bold ABBASI N
# Let's extract the current pC array string, replace 'Abbasi NM' and 'Abbasi N' with '<b>ABBASI N</b>',
# and write it back.

match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    pc_data = match.group(0)
    
    # Replace the specific cases
    pc_data = pc_data.replace("Abbasi NM", "<b>ABBASI N</b>")
    pc_data = pc_data.replace("Abbasi N", "<b>ABBASI N</b>")
    
    content = content.replace(match.group(0), pc_data)
    print("Replaced pC data with bolded names.")
else:
    print("Could not find pC array")
    sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully patched.")
