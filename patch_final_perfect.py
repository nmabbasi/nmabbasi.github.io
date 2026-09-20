import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update pC array to only have correct items (2 under review, 1 in prep, 3 published with years)
old_pC = r'pC=\[\{status:"Under review",text:"Boccelari L, Gravelle P, Tosolini M, Abbasi N, Le Morvan V, et al\. Primary Cutaneous Diffuse Large B Cell Lymphoma, Leg Type, Induces Dynamic Transcriptional Reprogramming of Immunosuppressive Macrophages \| Cancer Immunology Research\."\},\{status:"Under review",text:"Abbasi N, et al\. Deciphering Sézary syndrome tumoral heterogeneity through a bioinformatic approach\. To be submitted online, end of 2026\."\},\{status:"In preparation",text:"Cherfan C, Deslande M, Prochazkova-Carlotti M, Abbasi N, Sharanek A, Pham-Ledard A, Poglio S, Gros A, Merlio J-P, Bresson-Bepoldin L, Beylot-Barry M, Chevret E\. Oxidative Phosphorylation: A Potential Achilles\' Heel of Sézary Cells\."\},\{status:"Published \| 2013",text:"Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, Abbasi N, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R\. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome \| Molecular Vision\. 2013;19:644-653\."\},\{status:"Published \| 2016",text:"Zangenah S, Abbasi N, Anders FA, Bergman P\. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans \| Scientific Reports\. 2016\."\},\{status:"Published \| 2017",text:"Zajitschek S, Herbert-Read JE, Abbasi N, Immler S\. Paternal personality and social status influence offspring personality \| BMC Evolutionary Biology\. 2017;17:157\."\}\];'

new_pC = 'pC=[{status:"Under review",text:"Boccelari L, Gravelle P, Tosolini M, Abbasi N, Le Morvan V, et al. Primary Cutaneous Diffuse Large B Cell Lymphoma, Leg Type, Induces Dynamic Transcriptional Reprogramming of Immunosuppressive Macrophages | Cancer Immunology Research."},{status:"Under review",text:"Abbasi N, et al. Deciphering Sézary syndrome tumoral heterogeneity through a bioinformatic approach | To be submitted online, end of 2026."},{status:"In preparation",text:"Cherfan C, Deslande M, Prochazkova-Carlotti M, Abbasi N, Sharanek A, Pham-Ledard A, Poglio S, Gros A, Merlio J-P, Bresson-Bepoldin L, Beylot-Barry M, Chevret E. Oxidative Phosphorylation: A Potential Achilles\' Heel of Sézary Cells."},{status:"2013",text:"Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, Abbasi N, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome | Molecular Vision. 2013;19:644-653."},{status:"2016",text:"Zangenah S, Abbasi N, Anders FA, Bergman P. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans | Scientific Reports. 2016."},{status:"2017",text:"Zajitschek S, Herbert-Read JE, Abbasi N, Immler S. Paternal personality and social status influence offspring personality | BMC Evolutionary Biology. 2017;17:157."}];'

match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    content = content.replace(match.group(0), new_pC)
    print("Replaced pC data.")
else:
    print("Could not find pC array")
    sys.exit(1)

# 2. Update the React rendering logic perfectly
old_render = 'pC.map(r=>S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:308",className:"publication-item",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:309",children:r.status},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:309,columnNumber:19},this),S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:309",children:r.text},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:309,columnNumber:93},this)]},r.status,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:308,columnNumber:17},this))'

new_render = '(function(){const groups=[];let last="";pC.forEach(r=>{if(r.status!==last){groups.push({status:r.status,texts:[r.text]});last=r.status;}else{groups[groups.length-1].texts.push(r.text);}});return groups.map((g,i)=>S.jsxDEV("article",{"data-loc":"client/src/pages/Home.tsx:308",className:"publication-item",children:[S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:309",children:g.status},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:309,columnNumber:19},this),g.texts.map((t,j)=>S.jsxDEV("p",{"data-loc":"client/src/pages/Home.tsx:309",children:t},j,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:309,columnNumber:93},this))]},g.status,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:308,columnNumber:17},this));})()'

if old_render in content:
    content = content.replace(old_render, new_render)
    print("Replaced rendering logic.")
else:
    print("Could not find old_render")
    sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully patched.")
