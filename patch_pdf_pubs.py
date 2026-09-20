import re
import sys

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update PDF links
old_pdf_link = "/assets/nasir-mahmood-abbasi-postdoctoral-cv.pdf"
new_pdf_link = "/assets/Nasir_Mahmood_Abbasi_CV.pdf"
content = content.replace(old_pdf_link, new_pdf_link)

# 2. Update pC array to match the new CV exactly
# Under Review
ur1 = "Boccelari L, Gravelle P, Tosolini M, Abbasi N, Le Morvan V, et al. Primary Cutaneous Diffuse Large B Cell Lymphoma, Leg Type, Induces Dynamic Transcriptional Reprogramming of Immunosuppressive Macrophages. Cancer Immunology Research. Under review"
ur2 = "Abbasi NM, Paz Del Socorro T, Gravelle P, Tosolini M, Prochazkova-Carlotti M, Pham Ledard A, Beylot-Barry M, Isnard A, Roussel A, Boccelari L, Guéry MA, Merlio JP, Poglio S, Laurent C, Karkar S, Gros A. Single-cell multi-omics of Sézary cell lines reveals transcriptomic heterogeneity and identifies gene as a potential therapeutic target. Biomarker Research. Under review"
# In Preparation
ip1 = "Cherfan C, Deslande M, Prochazkova-Carlotti M, Abbasi N, Sharanek A, Pham-Ledard A, Poglio S, Gros A, Merlio J-P, Bresson-Bepoldin L, Beylot-Barry M, Chevret E. Oxidative Phosphorylation: A Potential Achilles' Heel of Sézary Cells"
# Published
p1 = "Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, Abbasi N, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome. Molecular Vision. 2013;19:644-653"
p2 = "Zangenah S, Abbasi N, Anders FA, Bergman P. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans. Scientific Reports. 2016"
p3 = "Zajitschek S, Herbert-Read JE, Abbasi N, Immler S. Paternal personality and social status influence offspring personality in offsprings. BMC Evolutionary Biology. 2017;17:157"

new_pC = f'pC=[{{status:"Under Review",text:"{ur1}"}},{{status:"Under Review",text:"{ur2}"}},{{status:"In Preparation",text:"{ip1}"}},{{status:"Published",text:"{p1}"}},{{status:"Published",text:"{p2}"}},{{status:"Published",text:"{p3}"}}];'

match = re.search(r'pC=\[\{.*?\}\];', content)
if match:
    content = content.replace(match.group(0), new_pC)
    print("Replaced pC data.")
else:
    print("Could not find pC array")
    sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully patched.")
