import re

file_path = "/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# 1. Revert CLIC1 to gene
if "identifies CLIC1 as a potential" in content:
    content = content.replace("identifies CLIC1 as a potential", "identifies a novel gene as a potential")
    print("Reverted CLIC1 to 'a novel gene'")
    changes += 1
# Just in case they prefer just "gene" instead of "a novel gene", let's use exactly what was there before
# Actually, before it was "identifies gene as a potential". It's better to say "identifies a novel gene" or "identifies a target gene". Let's stick to "identifies a novel gene as a potential therapeutic target" or exactly what was there: "identifies gene as a potential"
# User said: "Dont add CLIC1 on website i hided it intentionally until paper is published". 
# Original text: "identifies gene as a potential therapeutic target"
# Let's use "identifies a novel gene" to make it grammatically correct, since "identifies gene" sounds broken. Actually, I will just put back exactly "identifies a gene" or "identifies gene". Let's use "identifies a target gene". 
# The user's exact words previously: "identifies gene as a potential". Let's replace with "identifies a specific gene as a potential" or just "identifies a novel gene".
content = content.replace("identifies CLIC1 as a potential", "identifies a target gene as a potential")

# Also fix it in the PhD experience summary if I added it there
if "identified CLIC1 as a novel" in content:
    content = content.replace("identified CLIC1 as a novel", "identified a specific gene as a novel")
    print("Reverted CLIC1 in PhD experience")
    changes += 1

# 2. Change "17 years of experience" to "extensive experience"
if "17 years of experience" in content:
    content = content.replace("17 years of experience", "extensive experience")
    print("Changed 17 years to extensive experience")
    changes += 1

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Total changes:", changes)
