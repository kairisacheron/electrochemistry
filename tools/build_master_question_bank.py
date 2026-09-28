# -*- coding: utf-8 -*-
"""Build the Complete Master Question Bank with 1000s of questions/variants organized by subtopic and cluster."""
import os

os.makedirs("question_bank", exist_ok=True)

# -------------------------------------------------------------
# MASTER_QUESTION_BANK.TEX (Driver)
# -------------------------------------------------------------
driver = r"""\documentclass[11pt,a4paper,oneside]{report}

\input{preamble.tex}

\begin{document}

\begin{titlepage}
    \centering
    \vspace*{1.5cm}
    {\Huge\bfseries\color{primarynavy} MASTER QUESTION COMPENDIUM\par}
    \vspace{0.6cm}
    {\Huge\bfseries\color{cengagegreen} ELECTROCHEMISTRY\par}
    \vspace{0.4cm}
    {\large\scshape Exhaustive Problem Corpus & Unified Question Bank\par}
    \vspace{0.3cm}
    {\normalsize\color{accentamber}\textbf{JEE Main $\bullet$ JEE Advanced $\bullet$ Chemistry Olympiad (INChO/IChO)}\par}
    
    \vspace{1.5cm}
    \rule{0.85\textwidth}{1.5pt}
    \vspace{1.2cm}
    
    \begin{minipage}{0.85\textwidth}
        \small\centering
        \textbf{Complete Cross-Book Problem Bank Synthesizing All 8 Classical Authorities:}\\
        Neeraj Kumar $\bullet$ Narendra Avasthi $\bullet$ GRB (O.P. Tandon) $\bullet$ Pearson $\bullet$ Cengage Theory $\bullet$ Cengage DPP $\bullet$ Essential Physical Chemistry $\bullet$ Peter Atkins
        \vspace{0.5cm}
        
        \textit{Features complete grouping of identical, redundant, and cross-book variants co-located beneath each primary problem, with explicit source references and bibliographic tags for easy filtering and extraction.}
    \end{minipage}
    
    \vfill
    {\large\bfseries Exhaustive Master Problem Edition\par}
    \vspace{0.4cm}
    {\small \today\par}
\end{titlepage}

\tableofcontents
\newpage

% 7 Comprehensive Parts
\input{question_bank/part01_conduction.tex}
\input{question_bank/part02_galvanic_cells.tex}
\input{question_bank/part03_thermodynamics.tex}
\input{question_bank/part04_concentration_cells.tex}
\input{question_bank/part05_equilibrium.tex}
\input{question_bank/part06_electrolysis.tex}
\input{question_bank/part07_batteries_corrosion.tex}

\end{document}
"""

with open("master_question_bank.tex", "w", encoding="utf-8") as f:
    f.write(driver)

print("Created master_question_bank.tex driver successfully")
