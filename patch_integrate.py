import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Remove the ugly standalone section I added before
marker_start = 'S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:329",className:"academic-section",style:{paddingTop:"2rem"}'
marker_end = 'S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:332",id:"contact"'
idx_start = content.find(marker_start)
idx_end = content.find(marker_end)
if idx_start > -1 and idx_end > -1:
    content = content[:idx_start] + content[idx_end:]
    print("Step 1: Removed standalone section.")
else:
    print("Step 1: Already removed or not found.")

# Step 2: Insert conferences and languages cards into the academic-side div
# Find the exact insertion point: right before the academic-side children array closes
# The closing pattern after teaching-card is:
# ...lineNumber:324,columnNumber:15},this)]},void 0,!0,{fileName:"...lineNumber:313,columnNumber:13},this)
# The "]}" before lineNumber:313 closes academic-side's children array
# I need to insert before that "]}"

insertion_marker = 'lineNumber:324,columnNumber:15},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:313'

if insertion_marker not in content:
    print("ERROR: insertion marker not found")
    exit(1)

# Build new cards using the same pattern as education-card
# Conferences card
conf_card = ',S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:327",className:"education-card",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:327",className:"mini-label",children:"CONFERENCES & PRESENTATIONS"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"\\u201cSingle-cell dissection of S\\u00e9zary syndrome heterogeneity\\u201d \\u2014 Flash Talk & Poster, SBM Day, France (2024)"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"\\u201cTumor heterogeneity and regulatory programs in cutaneous lymphoma\\u201d \\u2014 Poster, SBM Day, France (2025)"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"Poster Presentation \\u2014 Doctoral School Day, Universit\\u00e9 de Bordeaux (2025)"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"gdec-bioinfo-workshop#2 \\u2014 Tidyverse / R Markdown for Genomics, France"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"The Hong Kong Epigenomics Project \\u2014 seminar series, Hong Kong"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:327",children:"The Mathematics of Deep Learning \\u2014 seminar, Hong Kong"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:17},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:327,columnNumber:15},this)'

# Languages card
lang_card = ',S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:328",className:"education-card",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:328",className:"mini-label",children:"LANGUAGES"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:328,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:328",children:"English: Fluent"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:328,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:328",children:"French: Basic"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:328,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:328",children:"Urdu: Native"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:328,columnNumber:17},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:328,columnNumber:15},this)'

# Insert right before the teaching-card's closing that leads to academic-side close
# The pattern: after teaching-card article closes (lineNumber:324), then academic-side children close
# I need to insert AFTER the teaching-card article close but BEFORE academic-side children close

# Replace the marker, inserting cards between teaching close and academic-side close
old_text = 'lineNumber:324,columnNumber:15},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:313'
new_text = 'lineNumber:324,columnNumber:15},this)' + conf_card + lang_card + ']},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:313'

content = content.replace(old_text, new_text)
print("Step 2: Inserted Conferences & Languages cards into academic-side.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("File saved.")
