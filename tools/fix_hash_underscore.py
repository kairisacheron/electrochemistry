# -*- coding: utf-8 -*-
"""Fix stray # and _ characters in question bodies that trigger LaTeX errors."""
import glob
import re

files = glob.glob("question_bank/extracted/*.tex")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    cleaned = []
    for l in lines:
        if l.strip().startswith(("\\chapter", "\\section", "\\begin{problembox}", "\\end{problembox}", "\\label", "\\textbf{Problem", "\\tcbline")):
            cleaned.append(l)
            continue
        
        # Replace stray # with \#
        l_fixed = l.replace("#", r"\#")
        # Replace stray _ with \_ (fill-in-the-blank blanks like /_/_/_/_/ -> \underline{\hspace{1cm}})
        l_fixed = re.sub(r'(/_)+', r'\\underline{\\hspace{1cm}}', l_fixed)
        l_fixed = l_fixed.replace("_", r"\_")
        
        cleaned.append(l_fixed)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))
    print(f"Fixed # and _ in {fpath}")

print("Hash and underscore sanitization complete.")
