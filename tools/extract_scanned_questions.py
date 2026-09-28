# -*- coding: utf-8 -*-
"""
Phase 2 OCR Extractor: Cengage DPP, Narendra Avasthi, and Pearson.
Extracts questions from scanned pages using local RapidOCR.
"""
import fitz
import re
import os
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs("question_bank/extracted", exist_ok=True)
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

def ocr_pdf_to_questions(pdf_path, label_prefix, max_pages=None):
    doc = fitz.open(pdf_path)
    questions = []
    total = len(doc) if max_pages is None else min(len(doc), max_pages)
    print(f"Running OCR on {pdf_path} ({total} pages)...")
    
    full_text = ""
    for p in range(total):
        pix = doc[p].get_pixmap(dpi=120)
        res, _ = ocr(pix.tobytes('png'))
        if res:
            page_text = "\n".join([r[1] for r in res])
            full_text += f"\n--- PAGE {p+1} ---\n" + page_text
        if (p + 1) % 5 == 0:
            print(f"  Processed {p+1}/{total} pages...")
            
    # Split into questions by number at start of lines
    raw_blocks = re.split(r'\n\s*(\d+)[\.\)]\s+', full_text)
    if len(raw_blocks) > 1:
        for i in range(1, len(raw_blocks), 2):
            q_num = raw_blocks[i]
            q_body = raw_blocks[i+1].strip()
            if len(q_body) > 20 and not "Answer" in q_body[:10]:
                questions.append({
                    "source": f"{label_prefix} Q{q_num}",
                    "num": q_num,
                    "body": q_body
                })
    return questions

def format_to_latex(questions, filename, title):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r"\chapter{" + clean_latex(title) + r"}" + "\n")
        f.write(r"\label{chap:" + os.path.basename(filename).replace(".tex", "") + r"}" + "\n\n")
        
        for idx, q in enumerate(questions, 1):
            clean_body = clean_latex(q['body'])
            f.write(r"\begin{problembox}" + "\n")
            f.write(r"\textbf{Problem " + str(idx) + r"} \hfill \textbf{[" + clean_latex(q['source']) + r"]}" + "\n")
            f.write(r"\label{q:ext-" + os.path.basename(filename).replace(".tex", "") + f"-{idx}" + r"}" + "\n\n")
            f.write(clean_body + "\n")
            f.write(r"\end{problembox}" + "\n\n")

# Run on Cengage DPP (all 14 pages)
dpp_q = ocr_pdf_to_questions("ElectroChemistryDPP(cng).pdf", "Cengage DPP", max_pages=14)
print(f"Total Cengage DPP questions: {len(dpp_q)}")
format_to_latex(dpp_q, "question_bank/extracted/cng_dpp_all_questions.tex", "Cengage DPP (3.1 to 3.5): Complete Question Bank")

# Run on Narendra Avasthi (all 43 pages)
na_q = ocr_pdf_to_questions("ElectroChemistry(Nrndr).pdf", "Narendra Avasthi", max_pages=43)
print(f"Total Narendra Avasthi questions: {len(na_q)}")
format_to_latex(na_q, "question_bank/extracted/narendra_avasthi_all_questions.tex", "Narendra Avasthi: Complete Graded Problem Bank (Levels 1, 2 & 3)")

print("Phase 2 OCR Extraction Finished!")
