# -*- coding: utf-8 -*-
"""Extract questions from Cengage Theory (ElectroChemistryTheory(Cng).pdf)."""
import fitz
import re
import os
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

def clean_latex(text):
    text = text.replace('\\', '/')
    replacements = [
        ('%', r'\%'),
        ('&', ' and '),
        ('#', r'\#'),
        ('_', r'\_'),
        ('^', ''),
        ('$', ''),
        ('\u2212', '-'),
        ('\u2013', '--'),
        ('\u2014', '---'),
        ('（', '('),
        ('）', ')'),
        ('［', '['),
        ('］', ']'),
        ('，', ', '),
        ('。', '. '),
        ('；', '; '),
        ('：', ': '),
        ('？', '?'),
        ('△', r'$\Delta$'),
        ('α', r'$\alpha$'),
        ('β', r'$\beta$'),
        ('λ', r'$\lambda$'),
        ('Ω', r'$\Omega$'),
        ('×', r'$\times$'),
        ('÷', r'$\div$'),
        ('°', r'$^\circ$'),
        ('→', r'$\to$'),
        ('←', r'$\leftarrow$'),
        ('⇌', r'$\rightleftharpoons$'),
    ]
    for orig, repl in replacements:
        text = text.replace(orig, repl)
    
    cleaned = [c for c in text if ord(c) < 128]
    return "".join(cleaned)

print("Running OCR on ElectroChemistryTheory(Cng).pdf (114 pages)...")
doc = fitz.open("ElectroChemistryTheory(Cng).pdf")

# Process exercise pages towards end of book and concept applications
# Concept App & exercises are dense in pages 50-114
full_text = ""
for p in range(len(doc)):
    pix = doc[p].get_pixmap(dpi=110)
    res, _ = ocr(pix.tobytes('png'))
    if res:
        p_txt = "\n".join([r[1] for r in res])
        full_text += f"\n--- PAGE {p+1} ---\n" + p_txt
    if (p + 1) % 15 == 0:
        print(f"  Processed {p+1}/{len(doc)} pages...")

raw_blocks = re.split(r'\n\s*(\d+)[\.\)]\s+', full_text)
cng_q = []
if len(raw_blocks) > 1:
    for i in range(1, len(raw_blocks), 2):
        q_num = raw_blocks[i]
        q_body = raw_blocks[i+1].strip()
        if len(q_body) > 25 and not "Answer" in q_body[:10]:
            cng_q.append({
                "source": f"Cengage Theory Chapter Exercises Q{q_num}",
                "num": q_num,
                "body": q_body
            })

print(f"Total Cengage Theory questions extracted: {len(cng_q)}")

with open("question_bank/extracted/cng_theory_all_questions.tex", "w", encoding="utf-8") as f:
    f.write(r"\chapter{Cengage Physical Chemistry: Comprehensive Chapter Exercises}" + "\n")
    f.write(r"\label{chap:cng_theory_all_questions}" + "\n\n")
    for idx, q in enumerate(cng_q, 1):
        clean_body = clean_latex(q['body'])
        f.write(r"\begin{problembox}" + "\n")
        f.write(r"\textbf{Problem " + str(idx) + r"} \hfill \textbf{[" + clean_latex(q['source']) + r"]}" + "\n")
        f.write(r"\label{q:ext-cng-th-" + str(idx) + r"}" + "\n\n")
        f.write(clean_body + "\n")
        f.write(r"\end{problembox}" + "\n\n")

print("Cengage Theory extraction completed!")
