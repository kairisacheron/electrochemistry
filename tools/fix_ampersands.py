# -*- coding: utf-8 -*-
"""Fix bare & to \& in LaTeX titles and headings across question_bank/ and master_question_bank.tex."""
import glob
import re

for filepath in glob.glob("question_bank/*.tex") + ["master_question_bank.tex"]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace unescaped & with \&
    # match & not preceded by \
    fixed = re.sub(r'(?<!\\)&', r'\&', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fixed)
    print(f"Fixed {filepath}")

print("All bare ampersands escaped successfully.")
