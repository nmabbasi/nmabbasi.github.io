import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Remove the ugly standalone Conferences & Languages section
marker_start = 'S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:329",className:"academic-section",style:{paddingTop:"2rem"}'
marker_end = 'S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:332",id:"contact"'

idx_start = content.find(marker_start)
idx_end = content.find(marker_end)

if idx_start > -1 and idx_end > -1:
    content = content[:idx_start] + content[idx_end:]
    print("Removed standalone Conferences & Languages section.")
else:
    print("ERROR: Could not find section to remove")
    exit(1)

# Step 2: Add conferences and languages inside the existing academic-side div,
# right after the teaching-card, using the same card patterns (education-card style)
# Find the teaching card end marker - it closes the academic-side div
teaching_end = 'Teaching Assistant at Universit\\xe9 de Bordeaux and Instructor of Bioinformatics at the Virtual University of Pakistan.'
idx_teaching = content.find('Teaching Assistant at Universit')
if idx_teaching == -1:
    print("ERROR: Could not find teaching text")
    exit(1)

# Find the closing of the teaching-card article after this text
# Pattern: after the teaching text, there are closing brackets for the article
# We need to find where teaching-card article closes and add our new cards after it

# The teaching card structure ends with these closing tags (3 levels)
# Let's find the exact spot by looking for the pattern after teaching text
search_from = idx_teaching
# Find the first },this) sequence that closes the teaching-card article
# Looking for: ]},void 0,!0,...},this)] - end of teaching-card children
# Then another ]},void 0,!0,...},this)] - end of academic-side children

# Let me find the education-rule and teaching-card patterns to understand the structure
# The academic-side has: education-card, teaching-card, then closes
# I need to add new cards between the teaching-card close and the academic-side close

# Find: teaching-card close followed by academic-side close
# teaching card pattern ends with:
teaching_card_end = 'className:"teaching-card"'
idx_tc = content.find(teaching_card_end)
if idx_tc == -1:
    print("ERROR: Could not find teaching-card")
    exit(1)

# From teaching-card, find where it closes (the article element)
# Count opening/closing to find the right spot
# Actually, let me find the specific pattern: the academic-side div closes after teaching-card
# Look for the sequence after teaching text that ends the academic-side

# The structure is:
# academic-side div > [education-card article, teaching-card article] > close academic-side
# I need to find where academic-side's children array closes

# Find the text that uniquely identifies the end of teaching card content
tc_text = 'Teaching Assistant at Universit'
idx_tc_text = content.find(tc_text)

# After this text, find the pattern that closes teaching-card and academic-side
# It will be something like: ...},this)]},void 0,!0,...},this)]},void 0,!0,...},this)
# Let's search for the specific closing sequence

# Find academic-side div closing - it's the ]}, that closes the children array of academic-side
# After teaching card, look for the sequence that ends with the academic-section close
# Match: ...lineNumber:313,columnNumber:13},this)]},void 0,!0,...lineNumber:304
search_area = content[idx_tc_text:idx_tc_text+2000]

# Find 'lineNumber:313' which closes academic-side  
ln313 = search_area.find('lineNumber:313')
if ln313 == -1:
    # Try finding the closing pattern differently
    # Look for the close of academic-side children array
    ln313 = search_area.find('lineNumber:304')
    if ln313 == -1:
        print("ERROR: Could not find section closing markers")
        # Let's just print what we see
        print(search_area[:1000])
        exit(1)

# Find the insertion point - right before the ]}, that closes academic-side's children
# Look backwards from lineNumber:313 for the ]}, pattern
insert_area = content[idx_tc_text:idx_tc_text+ln313]
# The last ]}, before lineNumber:313 is where teaching-card article closes
# We want to insert after that

# Actually, let me take a simpler approach: 
# Find the exact string that marks the end of the academic-side children array
# and insert before it

# The teaching-card is the last child of academic-side. After it closes, academic-side closes.
# Pattern: ...},this)]},void 0,!0,{...,lineNumber:313,...},this)]
# The ]}, right before lineNumber:313 closes the academic-side's children array

# Let me find "columnNumber:13},this)]},void 0,!0,{fileName" near lineNumber:313
close_pattern = 'lineNumber:313,columnNumber:13},this)]'
idx_close = content.find(close_pattern)
if idx_close == -1:
    print("Looking for alternative close pattern...")
    # Try finding the academic-side close differently
    # Look for the end of academic section: lineNumber:304 (the academic-grid close)
    # or lineNumber:299 (the academic-section close)
    for ln in ['324', '326', '313', '314']:
        pat = f'lineNumber:{ln},columnNumber'
        idx_try = content.find(pat, idx_tc_text)
        if idx_try > -1:
            print(f'Found lineNumber:{ln} at {idx_try}')
            ctx = content[idx_try-100:idx_try+200]
            print(ctx[:300])
            print()

# Let me try a completely different approach - find the exact string between
# teaching card and the close of academic-side, and replace it
print()
print("=== Looking for exact insertion point ===")
# After teaching text, show the next 800 chars to see the closing structure
print(content[idx_tc_text+100:idx_tc_text+800])
