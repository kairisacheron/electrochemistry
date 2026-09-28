# -*- coding: utf-8 -*-
"""Global cleaner for all extracted files: removes raw &, stray control characters, and unclosed $."""
import glob
import re

files = glob.glob("question_bank/extracted/*.tex")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove non-printable control characters (like \x1a / ^^Z)
    content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', content)

    # 2. Replace any bare or slashed & (/&, &/, &) with 'and'
    content = content.replace('/&', ' and ').replace('&/', ' and ').replace('&', ' and ')

    # 3. Balance stray unclosed dollar signs per problembox
    # If a line or block has an odd number of $, balance it
    blocks = content.split(r"\begin{problembox}")
    new_blocks = [blocks[0]]
    for b in blocks[1:]:
        parts = b.split(r"\end{problembox}")
        body = parts[0]
        rest = r"\end{problembox}".join(parts[1:])
        
        # Check odd number of $
        dollar_count = body.count('$')
        if dollar_count % 2 != 0:
            # remove all stray $ in raw text to avoid unclosed math mode
            body = body.replace('$', '')
            
        new_blocks.append(body + r"\end{problembox}" + rest)

    content = r"\begin{problembox}".join(new_blocks)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned {fpath}")

print("Global cleanup complete.")
