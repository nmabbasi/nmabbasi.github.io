import re
import urllib.parse

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# 1. Update "9+ years" to "17 years"
if "9+ years of experience" in content:
    content = content.replace("9+ years of experience", "17 years of experience")
    print("Fixed years of experience")
    changes += 1

# 2. "identifies gene as" -> "identifies CLIC1 as"
if "identifies gene as a potential" in content:
    content = content.replace("identifies gene as a potential", "identifies CLIC1 as a potential")
    print("Fixed gene name")
    changes += 1

# 3. Expand PhD experience
old_phd = 'detail:"Built a single-cell multi-omic pipeline across patient-derived Sézary syndrome models, integrating transcriptome, surface protein, TCR clonality, whole-exome sequencing, and optical genome mapping."'
new_phd = 'detail:"Built a single-cell multi-omic pipeline across patient-derived Sézary syndrome models (transcriptome, surface protein, TCR clonality). Combined whole-exome sequencing, BioNano optical mapping, and single-cell transcriptomics into one coherent model of tumor structure. Resolved phenotypic states via pseudotime trajectory analysis and identified CLIC1 as a novel membrane biomarker, validated via in vitro pharmacological inhibition."'
if old_phd in content:
    content = content.replace(old_phd, new_phd)
    print("Expanded PhD experience")
    changes += 1

# 4. Break out Earlier research roles
old_earlier = 'detail:"Contributed to marine prokaryotic genomics, behavioural genetics, bacterial genomics, rare disease exome sequencing, wet-lab support, and bioinformatics teaching."'
new_earlier = 'detail:"Marine prokaryotic genome analysis (Universidad Miguel Hernández). Behavioral genetics (Evolutionary Biology Centre). Bacterial genomics (Karolinska Hospital). Exome sequencing (COMSATS University)."'
if old_earlier in content:
    content = content.replace(old_earlier, new_earlier)
    print("Expanded Earlier roles")
    changes += 1

# 5. Add GitHub profile link
# The footer links section looks like: S.jsxDEV("a",{"data-loc":"client/src/pages/Home.tsx:350",className:"social-linkedin",href:"https://www.linkedin.com/in/nmabbasi/",target:"_blank",rel:"noreferrer","aria-label":"LinkedIn profile",children:[S.jsxDEV(TS,...
# Let's insert GitHub right before ORCID.
# I will use a simple text or the same TS icon if I can't find github. Let's just use text for the icon area if needed, or see what icons are available. Actually, I can just copy the LinkedIn structure but change classes and URL. Since I don't know the exact Lucide icon name, I'll just leave the icon out or use TS (it's better than nothing, or maybe no icon). Let's use TS for now.
# Actually, I can just use a span with text.
github_html = 'S.jsxDEV("a",{"data-loc":"client/src/pages/Home.tsx:350",className:"social-github",style:{display:"flex",alignItems:"center",gap:"0.5rem",color:"var(--color-text-muted)",textDecoration:"none"},href:"https://github.com/nmabbasi",target:"_blank",rel:"noreferrer","aria-label":"GitHub profile",children:S.jsxDEV("span",{"data-loc":"client/src/pages/Home.tsx:350",children:"GitHub"},void 0,!1,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:350,columnNumber:254},this)},void 0,!0,{fileName:"/home/ubuntu/nasir-cv-redesign/client/src/pages/Home.tsx",lineNumber:350,columnNumber:11},this),'

orcid_marker = 'S.jsxDEV("a",{"data-loc":"client/src/pages/Home.tsx:351",className:"social-orcid"'
if orcid_marker in content and "social-github" not in content:
    content = content.replace(orcid_marker, github_html + orcid_marker)
    print("Added GitHub link")
    changes += 1

# 6. Add Scholar Links to published papers
import urllib.parse
def add_link(title):
    global content
    if title in content:
        url = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(title)
        link = f' <a href=\\"{url}\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\" style=\\"text-decoration:underline;\\">[Link]</a>'
        # we have to be careful not to double add
        if link not in content:
            content = content.replace(title, title + link)
            print("Added link for:", title[:20])
            return 1
    return 0

t1 = "Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, <b>Abbasi N</b>, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome. Molecular Vision. 2013;19:644-653"
t2 = "Zangenah S, <b>Abbasi N</b>, Anders FA, Bergman P. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans. Scientific Reports. 2016"
t3 = "Zajitschek S, Herbert-Read JE, <b>Abbasi N</b>, Immler S. Paternal personality and social status influence offspring personality. BMC Evolutionary Biology. 2017;17:157"

changes += add_link(t1)
changes += add_link(t2)
changes += add_link(t3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
