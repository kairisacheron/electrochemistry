# -*- coding: utf-8 -*-
"""Fix stray curly braces and control sequences in OCR generated problem text."""
import glob
import re

files = glob.glob("question_bank/extracted/*.tex")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into lines
    lines = content.splitlines()
    cleaned_lines = []
    
    for l in lines:
        # Keep structural LaTeX lines intact
        if l.strip().startswith(("\\chapter", "\\section", "\\begin{problembox}", "\\end{problembox}", "\\label", "\\textbf{Problem", "\\tcbline")):
            cleaned_lines.append(l)
            continue
        
        # Replace stray braces { and } in raw question body with parentheses ( and )
        l_clean = l.replace("{", "(").replace("}", ")")
        
        # Fix stray backslashes followed by letters that are not valid latex commands
        # In question body, replace backslashes with /
        l_clean = l_clean.replace("\\", "/")
        
        cleaned_lines.append(l_clean)
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned_lines))
    print(f"Fixed braces and control sequences in {fpath}")

print("Braces sanitization complete.")
