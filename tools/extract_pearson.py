# -*- coding: utf-8 -*-
"""Extract questions from Pearson (ElectroChemistryProblems(Prsn).pdf)."""
import fitz
import re
import os
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

def clean_latex(text):
    text = text.replace('\\', r'\textbackslash{}')
    replacements = [
        ('%', r'\%'),
        ('&', r'\&'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
        ('$', r'\$'),
        ('\u2212', '-'),
        ('\u2013', '--'),
        ('\u2014', '---'),
        ('\u2018', "'"),
        ('\u2019', "'"),
        ('\u201c', '"'),
        ('\u201d', '"'),
        ('\u2192', r'$\to$'),
        ('\u21cc', r'$\rightleftharpoons$'),
        ('\u00b0', r'$^\circ$'),
        ('²', r'$^2$'),
        ('³', r'$^3$'),
        ('⁺', r'$^+$'),
        ('⁻', r'$^-$'),
        ('ohm-1', r'$\Omega^{-1}$'),
        ('ohm', r'$\Omega$'),
    ]
    for orig, repl in replacements:
        text = text.replace(orig, repl)
    text = text.replace(r'\textbackslash{}', '\\')
    return text

print("Running OCR on ElectroChemistryProblems(Prsn).pdf (41 pages)...")
doc = fitz.open("ElectroChemistryProblems(Prsn).pdf")
full_text = ""
for p in range(len(doc)):
    pix = doc[p].get_pixmap(dpi=120)
    res, _ = ocr(pix.tobytes('png'))
    if res:
        full_text += f"\n--- PAGE {p+1} ---\n" + "\n".join([r[1] for r in res])
    if (p + 1) % 10 == 0:
        print(f"  Processed {p+1}/{len(doc)} pages...")

raw_blocks = re.split(r'\n\s*(\d+)[\.\)]\s+', full_text)
prsn_q = []
if len(raw_blocks) > 1:
    for i in range(1, len(raw_blocks), 2):
        q_num = raw_blocks[i]
        q_body = raw_blocks[i+1].strip()
        if len(q_body) > 20 and not "Answer" in q_body[:10]:
            prsn_q.append({
                "source": f"Pearson Advanced Electrochemistry Q{q_num}",
                "num": q_num,
                "body": q_body
            })

print(f"Total Pearson questions extracted: {len(prsn_q)}")

with open("question_bank/extracted/pearson_all_questions.tex", "w", encoding="utf-8") as f:
    f.write(r"\chapter{Pearson Advanced Electrochemistry: Complete Exercise Bank}" + "\n")
    f.write(r"\label{chap:pearson_all_questions}" + "\n\n")
    for idx, q in enumerate(prsn_q, 1):
        clean_body = clean_latex(q['body'])
        f.write(r"\begin{problembox}" + "\n")
        f.write(r"\textbf{Problem " + str(idx) + r"} \hfill \textbf{[" + clean_latex(q['source']) + r"]}" + "\n")
        f.write(r"\label{q:ext-pearson-" + str(idx) + r"}" + "\n\n")
        f.write(clean_body + "\n")
        f.write(r"\end{problembox}" + "\n\n")

print("Pearson Extraction Finished!")
