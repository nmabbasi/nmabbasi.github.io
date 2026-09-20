import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# ============================================================
# FIX 1: "in offsprings" → "" (remove it)
# ============================================================
old_text = "personality in offsprings"
new_text = "personality"
if old_text in content:
    content = content.replace(old_text, new_text)
    print("FIX 1: Fixed 'in offsprings' grammar error.")
    changes += 1
else:
    print("FIX 1: 'in offsprings' not found (already fixed?)")

# ============================================================
# FIX 2: Add Conferences & Languages section before Contact
# ============================================================
# Find the insertion point: right before the Contact section
contact_marker = 'S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:332",id:"contact"'
if contact_marker in content:
    # Build conferences & languages HTML section as a React JSX element
    conferences_section = '''S.jsxDEV("section",{"data-loc":"client/src/pages/Home.tsx:329",className:"academic-section",style:{paddingTop:"2rem"},children:[S.jsxDEV("div",{"data-loc":"client/src/pages/Home.tsx:329",className:"academic-heading",children:S.jsxDEV("div",{"data-loc":"client/src/pages/Home.tsx:329",children:[S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:329",className:"eyebrow",children:"CONFERENCES & LANGUAGES"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:13},this),S.jsxDEV("h2",{"data-loc":"client/src/pages/Home.tsx:329",children:"Presentations and spoken languages."},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:13},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:13},this)},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:11},this),S.jsxDEV("div",{"data-loc":"client/src/pages/Home.tsx:329",className:"academic-side",children:[S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:329",className:"education-card",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:329",className:"mini-label",children:"CONFERENCES & PRESENTATIONS"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:329",dangerouslySetInnerHTML:{__html:"\u2022 \\"Single-cell dissection of S\\u00e9zary syndrome heterogeneity\\" \\u2014 Flash Talk & Poster, SBM Day conference, France (September 2024)<br/>\u2022 \\"Tumor heterogeneity and regulatory programs in cutaneous lymphoma\\" \\u2014 Poster, SBM Day conference, France (September 2025)<br/>\u2022 Poster Presentation \\u2014 Doctoral School Day, Universit\\u00e9 de Bordeaux, France (2025)<br/>\u2022 gdec-bioinfo-workshop#2 \\u2014 Tidyverse / R Markdown for Genomics, training workshop, France<br/>\u2022 The Hong Kong Epigenomics Project \\u2014 seminar series, Hong Kong<br/>\u2022 The Mathematics of Deep Learning \\u2014 seminar, Hong Kong"}},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:17},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:15},this),S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:330",className:"education-card",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:330",className:"mini-label",children:"LANGUAGES"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:330,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:330",children:"English: Fluent"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:330,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:330",children:"French: Professional working proficiency"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:330,columnNumber:17},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:330",children:"Urdu: Native"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:330,columnNumber:17},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:330,columnNumber:15},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:13},this)]},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:329,columnNumber:9},this),'''
    
    content = content.replace(contact_marker, conferences_section + contact_marker)
    print("FIX 2: Added Conferences & Languages section before Contact.")
    changes += 1
else:
    print("FIX 2: Contact section marker not found.")

print(f"\nTotal changes: {changes}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("File saved.")
