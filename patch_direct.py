import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# The bad search URLs
url1 = "https://scholar.google.com/scholar?q=Exome%20sequencing%20identifies%20a%20novel%20and%20a%20recurrent%20BBS1%20mutation%20in%20Pakistani%20families%20with%20Bardet-Biedl%20syndrome"
url2 = "https://scholar.google.com/scholar?q=Whole%20Genome%20Sequencing%20Reveals%20Novel%20Species%20of%20genus%20Capnocytophaga%20Isolated%20From%20Dog%20and%20Cat%20Bite%20Wounds%20in%20Humans"
url3 = "https://scholar.google.com/scholar?q=Paternal%20personality%20and%20social%20status%20influence%20offspring%20personality"

# Direct Article URLs
direct1 = "https://pubmed.ncbi.nlm.nih.gov/23559846/"
direct2 = "https://www.nature.com/articles/srep20851"
direct3 = "https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-017-0994-x"

if url1 in content:
    content = content.replace(url1, direct1)
    changes += 1
if url2 in content:
    content = content.replace(url2, direct2)
    changes += 1
if url3 in content:
    content = content.replace(url3, direct3)
    changes += 1

# Change "Google Scholar" text to "View Article"
if "Google Scholar</span>" in content:
    content = content.replace("Google Scholar</span>", "View Article</span>")
    changes += 1

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
