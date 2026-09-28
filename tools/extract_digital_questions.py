# -*- coding: utf-8 -*-
"""
Phase 1 Extractor: Neeraj Kumar (NRJ), GRB (O.P. Tandon), and Essential Physical Chemistry.
Extracts questions locally directly from text streams, cleans math and options, and writes structured LaTeX.
"""
import fitz
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs("question_bank/extracted", exist_ok=True)

def clean_latex(text):
    """Sanitize raw text for LaTeX compilation."""
    text = text.replace('\\', r'\textbackslash{}')
    # Standard LaTeX replacements
    replacements = [
        ('%', r'\%'),
        ('&', r'\&'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
        ('$', r'\$'),
        ('\u2212', '-'),  # minus sign
        ('\u2013', '--'), # en-dash
        ('\u2014', '---'),# em-dash
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
    # Restore textbackslash
    text = text.replace(r'\textbackslash{}', '\\')
    return text

# -------------------------------------------------------------
# 1. EXTRACT NEERAJ KUMAR (NRJ)
# -------------------------------------------------------------
print("Parsing Neeraj Kumar [NRJ]...")
nrj_doc = fitz.open("ElectroChemistryProblems(nrj).pdf")
nrj_questions = []

current_section = "Electrochemistry"
for page_num in range(len(nrj_doc)):
    page_text = nrj_doc[page_num].get_text()
    
    # Check headers
    for line in page_text.splitlines():
        if "EXERCISE" in line.upper():
            current_section = line.strip()
    
    # Extract questions matching: number. text
    # Split by number at start of line
    raw_blocks = re.split(r'\n\s*(\d+)\.\s+', '\n' + page_text)
    if len(raw_blocks) > 1:
        for i in range(1, len(raw_blocks), 2):
            q_num = raw_blocks[i]
            q_body = raw_blocks[i+1].strip()
            
            # Stop if reached answer key
            if "Answer Keys" in q_body or "ANSWERS" in q_body:
                q_body = q_body.split("Answer Keys")[0].split("ANSWERS")[0].strip()
            
            if len(q_body) > 15:
                nrj_questions.append({
                    "source": f"Neeraj Kumar [NRJ] {current_section} Q{q_num}",
                    "page": page_num + 1,
                    "num": q_num,
                    "body": q_body
                })

print(f"Total NRJ questions extracted: {len(nrj_questions)}")

# -------------------------------------------------------------
# 2. EXTRACT GRB (O.P. TANDON)
# -------------------------------------------------------------
print("Parsing GRB / O.P. Tandon...")
grb_doc = fitz.open("ElectroChemistry(GRB).pdf")
grb_questions = []

# Objective and Practice questions start around page 45
for page_num in range(45, len(grb_doc)):
    page_text = grb_doc[page_num].get_text()
    raw_blocks = re.split(r'\n\s*(\d+)\.\s+', '\n' + page_text)
    if len(raw_blocks) > 1:
        for i in range(1, len(raw_blocks), 2):
            q_num = raw_blocks[i]
            q_body = raw_blocks[i+1].strip()
            if len(q_body) > 20 and not q_body.startswith("Page"):
                grb_questions.append({
                    "source": f"GRB (O.P. Tandon) p.{page_num+1} Q{q_num}",
                    "page": page_num + 1,
                    "num": q_num,
                    "body": q_body
                })

print(f"Total GRB questions extracted: {len(grb_questions)}")

# -------------------------------------------------------------
# 3. EXTRACT ESSENTIAL PHYSICAL CHEMISTRY
# -------------------------------------------------------------
print("Parsing Essential Physical Chemistry...")
ess_doc = fitz.open("ElectroChemistryTheory(essential).pdf")
ess_questions = []

for page_num in range(40, len(ess_doc)):
    page_text = ess_doc[page_num].get_text()
    raw_blocks = re.split(r'\n\s*(\d+)\.\s+', '\n' + page_text)
    if len(raw_blocks) > 1:
        for i in range(1, len(raw_blocks), 2):
            q_num = raw_blocks[i]
            q_body = raw_blocks[i+1].strip()
            if len(q_body) > 20:
                ess_questions.append({
                    "source": f"Essential Physical Chemistry p.{page_num+1} Q{q_num}",
                    "page": page_num + 1,
                    "num": q_num,
                    "body": q_body
                })

print(f"Total Essential questions extracted: {len(ess_questions)}")

# -------------------------------------------------------------
# FORMAT AND WRITE OUT TO LATEX
# -------------------------------------------------------------
def format_to_latex(questions, filename, title):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r"\chapter{" + clean_latex(title) + r"}" + "\n")
        f.write(r"\label{chap:" + os.path.basename(filename).replace(".tex", "") + r"}" + "\n\n")
        
        for idx, q in enumerate(questions, 1):
            clean_body = clean_latex(q['body'])
            # Format options (a), (b), (c), (d) cleanly if present
            # Replace inline (a) ... (b) ... with structured list
            f.write(r"\begin{problembox}" + "\n")
            f.write(r"\textbf{Problem " + str(idx) + r"} \hfill \textbf{[" + clean_latex(q['source']) + r"]}" + "\n")
            f.write(r"\label{q:ext-" + os.path.basename(filename).replace(".tex", "") + f"-{idx}" + r"}" + "\n\n")
            f.write(clean_body + "\n")
            f.write(r"\end{problembox}" + "\n\n")

print("Writing LaTeX files...")
format_to_latex(nrj_questions, "question_bank/extracted/nrj_all_questions.tex", "Neeraj Kumar [NRJ]: Complete Exercise Question Bank")
format_to_latex(grb_questions, "question_bank/extracted/grb_all_questions.tex", "GRB (O.P. Tandon): Complete Practice & Objective Bank")
format_to_latex(ess_questions, "question_bank/extracted/essential_all_questions.tex", "Essential Physical Chemistry: Complete Numerical Bank")

print("Phase 1 Extraction Complete! Total questions compiled:", len(nrj_questions) + len(grb_questions) + len(ess_questions))
