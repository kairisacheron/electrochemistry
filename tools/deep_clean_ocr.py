# -*- coding: utf-8 -*-
"""Full Unicode sanitizer for OCR artifacts: Chinese/Fullwidth punctuation and math symbols."""
import glob
import re

full_map = {
    '（': '(',
    '）': ')',
    '［': '[',
    '］': ']',
    '｛': '{',
    '｝': '}',
    '：': ': ',
    '；': '; ',
    '，': ', ',
    '。': '. ',
    '？': '?',
    '！': '!',
    '、': ', ',
    '“': '"',
    '”': '"',
    '‘': "'",
    '’': "'",
    '△': r'$\Delta$',
    '▲': r'$\Delta$',
    '∝': r'$\propto$',
    '√': r'$\sqrt{}$',
    '°': r'$^\circ$',
    '℃': r'$^\circ\text{C}$',
    '·': r'$\cdot$',
    '×': r'$\times$',
    '÷': r'$\div$',
    '±': r'$\pm$',
    '≤': r'$\le$',
    '≥': r'$\ge$',
    '≠': r'$\ne$',
    '≈': r'$\approx$',
    '≡': r'$\equiv$',
    '→': r'$\to$',
    '←': r'$\leftarrow$',
    '⇌': r'$\rightleftharpoons$',
    '⇒': r'$\implies$',
    '•': r'$\bullet$',
    '–': '--',
    '—': '---',
}

files = glob.glob("question_bank/extracted/*.tex") + glob.glob("question_bank/*.tex")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for u_char, repl in full_map.items():
        content = content.replace(u_char, repl)
        
    # Also strip any stray non-ascii character that is not standard
    # Allow only ASCII characters (0-127) plus common latex
    cleaned_chars = []
    for ch in content:
        if ord(ch) < 128:
            cleaned_chars.append(ch)
        else:
            # Fallback for any unknown unicode
            cleaned_chars.append(' ')
    content = "".join(cleaned_chars)
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned {fpath}")

print("Comprehensive OCR unicode stripping complete.")
