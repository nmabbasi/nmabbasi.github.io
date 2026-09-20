import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the React rendering to allow HTML (so we can use <br/><br/>)
content = content.replace('children:r.text', 'dangerouslySetInnerHTML:{__html:r.text}')

# 2. Update pC array to combine the Under review papers and correct others
old_pC = r'pC=\[\{status:"Under review",text:"Boccelari L, Gravelle P, Tosolini M, Abbasi N, Le Morvan V, et al\. Primary Cutaneous Diffuse Large B Cell Lymphoma, Leg Type, Induces Dynamic Transcriptional Reprogramming of Immunosuppressive Macrophages \| Cancer Immunology Research\."\},\{status:"Under review",text:"Abbasi N, et al\. Deciphering Sézary syndrome tumoral heterogeneity through a bioinformatic approach\. To be submitted online, end of 2026\."\},\{status:"In preparation",text:"Cherfan C, Deslande M, Prochazkova-Carlotti M, Abbasi N, Sharanek A, Pham-Ledard A, Poglio S, Gros A, Merlio J-P, Bresson-Bepoldin L, Beylot-Barry M, Chevret E\. Oxidative Phosphorylation: A Potential Achilles\' Heel of Sézary Cells\."\},\{status:"Published \| 2013",text:"Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, Abbasi N, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R\. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome \| Molecular Vision\. 2013;19:644-653\."\},\{status:"Published \| 2016",text:"Zangenah S, Abbasi N, Anders FA, Bergman P\. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans \| Scientific Reports\. 2016\."\},\{status:"Published \| 2017",text:"Zajitschek S, Herbert-Read JE, Abbasi N, Immler S\. Paternal personality and social status influence offspring personality \| BMC Evolutionary Biology\. 2017;17:157\."\}\];'

new_pC = 'pC=[{status:"Under review",text:"Boccelari L, Gravelle P, Tosolini M, Abbasi N, Le Morvan V, et al. Primary Cutaneous Diffuse Large B Cell Lymphoma, Leg Type, Induces Dynamic Transcriptional Reprogramming of Immunosuppressive Macrophages | Cancer Immunology Research.<br/><br/>Abbasi N, et al. Deciphering Sézary syndrome tumoral heterogeneity through a bioinformatic approach | To be submitted online, end of 2026."},{status:"In preparation",text:"Cherfan C, Deslande M, Prochazkova-Carlotti M, Abbasi N, Sharanek A, Pham-Ledard A, Poglio S, Gros A, Merlio J-P, Bresson-Bepoldin L, Beylot-Barry M, Chevret E. Oxidative Phosphorylation: A Potential Achilles\' Heel of Sézary Cells."},{status:"2013",text:"Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, Abbasi N, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome | Molecular Vision. 2013;19:644-653."},{status:"2016",text:"Zangenah S, Abbasi N, Anders FA, Bergman P. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans | Scientific Reports. 2016."},{status:"2017",text:"Zajitschek S, Herbert-Read JE, Abbasi N, Immler S. Paternal personality and social status influence offspring personality | BMC Evolutionary Biology. 2017;17:157."}];'

match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    content = content.replace(match.group(0), new_pC)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched.")
else:
    print("Could not find pC array")
