import re
import urllib.parse

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# The three papers
t1 = "Ajmal M, Khan M, Neveling K, Tayyab A, Jaffar S, Sadeque A, Ayub H, <b>Abbasi N</b>, Riaz M, Micheal S, Gilissen C, Ali S, Azam M, Collin R, Cremers F, Qamar R. Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome. Molecular Vision. 2013;19:644-653"
t2 = "Zangenah S, <b>Abbasi N</b>, Anders FA, Bergman P. Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans. Scientific Reports. 2016"
t3 = "Zajitschek S, Herbert-Read JE, <b>Abbasi N</b>, Immler S. Paternal personality and social status influence offspring personality. BMC Evolutionary Biology. 2017;17:157"

# Clean titles for searching
title1 = "Exome sequencing identifies a novel and a recurrent BBS1 mutation in Pakistani families with Bardet-Biedl syndrome"
title2 = "Whole Genome Sequencing Reveals Novel Species of genus Capnocytophaga Isolated From Dog and Cat Bite Wounds in Humans"
title3 = "Paternal personality and social status influence offspring personality"

# Build the new URLs
url1 = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(title1)
url2 = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(title2)
url3 = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(title3)

# Function to replace the bad URL in a specific paper's HTML block
def fix_link(text_block, clean_url):
    global content, changes
    # Find the href inside this block in the file
    # The bad URL contains urlencoded <b> tags, e.g. %3Cb%3E
    
    # We can just use a regex to replace the href="..." for the specific links.
    # It's safer to just replace all scholar.google.com hrefs sequentially if we can isolate them,
    # or just regex replace the specific bad URLs.
    
    # Let's extract the bad URL we generated before:
    bad_url = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(text_block)
    if bad_url in content:
        content = content.replace(bad_url, clean_url)
        print("Fixed URL for:", clean_url[-20:])
        changes += 1

fix_link(t1, url1)
fix_link(t2, url2)
fix_link(t3, url3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
