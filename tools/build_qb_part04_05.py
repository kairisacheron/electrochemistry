# -*- coding: utf-8 -*-
"""Generate question_bank/part04_concentration_cells.tex and part05_equilibrium.tex."""
import os

part04 = r"""\chapter{Master Problem Bank: Concentration Cells & Liquid Junction Potential}
\label{chap:qb_concentration_cells}

\begin{tcolorbox}[enhanced,colback=subtleblue,colframe=primarynavy,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part IV Organization: Concentration Cells & Liquid Junction Potential}]
This part compiles all questions and quantitative problems on electrode concentration cells (gas & amalgam), electrolyte concentration cells without transference, concentration cells with transference, and the liquid junction potential ($E_{lj}$) from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 4.1: Electrode Concentration Cells (Gas & Amalgam)}

\begin{problembox}
\textbf{Q.4.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-I Q95 / GRB §12.24]}
\label{q:qb-c4-01}

Calculate the potential at $25^\circ\text{C}$ of the gas concentration cell:
\begin{equation*}
    \ce{Pt, H2}(P_1 = 10\,\text{atm}) \mid \ce{HCl}(0.1\,\text{M}) \mid \ce{H2}(P_2 = 1\,\text{atm})\ce{, Pt}
\end{equation*}
\begin{multicols}{4}
\begin{enumerate}[label=(\alph*)]
    \item $+0.0296\,\text{V}$
    \item $-0.0296\,\text{V}$
    \item $+0.0591\,\text{V}$
    \item $0.000\,\text{V}$
\end{enumerate}
\end{multicols}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-I Q90, p. 8]} For the gas cell $\ce{Pt, Cl2}(P_1) \mid \ce{NaCl}(1\,\text{M}) \mid \ce{Cl2}(P_2)\ce{, Pt}$, the cell reaction is spontaneous if: (a) $P_1 > P_2$ (b) $P_2 > P_1$ (c) $P_1 = P_2$ (d) independent of pressure.
    \item \textbf{[Variant v2: Narendra Avasthi Level-2 Q55, p. 30]} For a zinc amalgam concentration cell $\ce{Zn(Hg, } a_1\ce{)} \mid \ce{ZnSO4(aq)} \mid \ce{Zn(Hg, } a_2\ce{)}$, the EMF is given by: (a) $\frac{RT}{2F}\ln \frac{a_1}{a_2}$ (b) $\frac{RT}{2F}\ln \frac{a_2}{a_1}$ (c) $\frac{RT}{F}\ln \frac{a_1}{a_2}$ (d) zero.
    \item \textbf{[Variant v3: Cengage Theory p. 30]} In an amalgam concentration cell, why is $E^\circ_{\text{cell}} = 0.00\,\text{V}$ identically?
\end{itemize}
\end{problembox}

\section{Subtopic 4.2: Electrolyte Concentration Cells Without Transference}

\begin{problembox}
\textbf{Q.4.2} \hfill \textbf{[Primary Source: GRB Practice Problem 38, p. 49 / PRSN Ex-II Q22]}
\label{q:qb-c4-02}

The EMF of the concentration cell without transference:
\begin{equation*}
    \ce{Ag(s)} \mid \ce{AgNO3}(0.01\,\text{M}) \parallel \ce{AgNO3}(0.1\,\text{M}) \mid \ce{Ag(s)}
\end{equation*}
is $0.0575\,\text{V}$ at $25^\circ\text{C}$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the theoretical EMF assuming complete ionization and unit activity coefficients.
    \item If the mean activity coefficient of $0.01\,\text{M } \ce{AgNO3}$ is $\gamma_1 = 0.89$, determine the mean activity coefficient $\gamma_2$ of the $0.1\,\text{M}$ solution.
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-I Q98, p. 9]} The EMF of the cell $\ce{Zn} \mid \ce{Zn^2+}(0.001\,\text{M}) \parallel \ce{Zn^2+}(0.1\,\text{M}) \mid \ce{Zn}$ at $298\,\text{K}$ is: (a) $0.0591\,\text{V}$ (b) $0.0296\,\text{V}$ (c) $0.1182\,\text{V}$ (d) zero.
    \item \textbf{[Variant v2: Narendra Avasthi Level-1 Q135, p. 19]} If the concentration of both half-cells in an electrolyte concentration cell is doubled, the cell EMF will: (a) double (b) halve (c) remain unchanged (d) become zero.
    \item \textbf{[Variant v3: Cengage DPP 3.3 Q18, p. 6]} For a concentration cell reversible with respect to anions, $\ce{Ag, AgCl(s)} \mid \ce{KCl}(a_1) \parallel \ce{KCl}(a_2) \mid \ce{AgCl(s), Ag}$, the cell EMF is positive when: (a) $a_1 > a_2$ (b) $a_2 > a_1$ (c) $a_1 = a_2$ (d) always negative.
\end{itemize}
\end{problembox}

\section{Subtopic 4.3: Concentration Cells With Transference & Liquid Junction Potential ($E_{lj}$)}

\begin{problembox}
\textbf{Q.4.3} \hfill \textbf{[Primary Source: Atkins Topic 6C.2 / Neeraj Kumar Part 1 Ex-II Sec C Passage 1]}
\label{q:qb-c4-03}

For the cell with direct liquid junction:
\begin{equation*}
    \ce{Pt, H2}(1\,\text{atm}) \mid \ce{HCl}(a_1 = 0.01) : \ce{HCl}(a_2 = 0.1) \mid \ce{H2}(1\,\text{atm})\ce{, Pt}
\end{equation*}
The EMF with transference is measured to be $E_{wt} = 0.0955\,\text{V}$ at $25^\circ\text{C}$.
\begin{enumerate}[label=(\alph*)]
    \item Derive the expression $E_{wt} = 2t_- \frac{RT}{F}\ln \frac{a_2}{a_1}$.
    \item Calculate the transport number of the chloride ion $t_{\ce{Cl-}}$ and the proton $t_{\ce{H+}}$.
    \item Calculate the liquid junction potential $E_{lj}$ at the interface.
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-II Sec A Q52, p. 20]} The liquid junction potential for a $1:1$ electrolyte boundary between activities $a_1$ and $a_2$ is given by: (a) $(t_+ - t_-)\frac{RT}{F}\ln(a_2/a_1)$ (b) $(2t_- - 1)\frac{RT}{F}\ln(a_2/a_1)$ (c) $(1 - 2t_+)\frac{RT}{F}\ln(a_2/a_1)$ (d) All of these are equivalent.
    \item \textbf{[Variant v2: GRB §12.26 Solved Ex 42, p. 33]} Explain why the liquid junction potential is virtually eliminated when a saturated \ce{KCl} bridge is inserted between two solutions.
    \item \textbf{[Variant v3: Narendra Avasthi Level-3 Passage 2, p. 37]} In which case is the liquid junction potential negative for $a_2 > a_1$? (a) $t_+ > t_-$ (b) $t_- > t_+$ (c) $t_+ = t_-$ (d) always positive.
\end{itemize}
\end{problembox}
"""

part05 = r"""\chapter{Master Problem Bank: Advanced Equilibrium Applications of EMF}
\label{chap:qb_equilibrium}

\begin{tcolorbox}[enhanced,colback=subtlegreen,colframe=cengagegreen,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part V Organization: Equilibrium Applications, pH, $K_{sp}$, Latimer & Frost}]
This part compiles all questions and multi-step analytical problems on solubility products ($K_{sp}$), potentiometric pH determination (SHE, quinhydrone, glass electrode), complex ion formation constants, and Latimer/Frost oxidation state diagrams from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 5.1: Determination of Solubility Product ($K_{sp}$)}

\begin{problembox}
\textbf{Q.5.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-II Sec F Q8 / NA Level-1 Q128]}
\label{q:qb-c5-01}

Calculate the solubility product $K_{sp}$ of silver bromide (\ce{AgBr}) at $25^\circ\text{C}$ from the following standard reduction potentials:
\begin{align*}
    \ce{AgBr(s) + e^- -> Ag(s) + Br^-(aq)} \quad & E^\circ = +0.071\,\text{V} \\
    \ce{Ag+(aq) + e^- -> Ag(s)} \quad & E^\circ = +0.799\,\text{V}
\end{align*}
\begin{multicols}{4}
\begin{enumerate}[label=(\alph*)]
    \item $5.0 \times 10^{-13}$
    \item $2.5 \times 10^{-12}$
    \item $1.0 \times 10^{-10}$
    \item $7.2 \times 10^{-15}$
\end{enumerate}
\end{multicols}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: GRB Practice Problem 50, p. 50]} The EMF of the cell $\ce{Ag} \mid \ce{AgI(s)}, 0.05\,\text{M } \ce{KI} \parallel 0.05\,\text{M } \ce{AgNO3} \mid \ce{Ag}$ is $0.788\,\text{V}$ at $25^\circ\text{C}$. Calculate the solubility product of \ce{AgI}.
    \item \textbf{[Variant v2: Pearson Ex-II Sec E Q18, p. 38]} For the cell $\ce{Pb} \mid \ce{PbSO4(s)}, \ce{SO4^2-}(0.1\,\text{M}) \parallel \ce{Pb^2+}(0.1\,\text{M}) \mid \ce{Pb}$, the EMF is $0.236\,\text{V}$ at $298\,\text{K}$. Calculate $K_{sp}(\ce{PbSO4})$.
    \item \textbf{[Variant v3: Cengage Theory Concept App 5 Q2, p. 43]} How can the solubility product of calomel (\ce{Hg2Cl2}) be determined from standard electrode potentials?
\end{itemize}
\end{problembox}

\section{Subtopic 5.2: Potentiometric $\text{pH}$ Determination (SHE, Quinhydrone & Glass)}

\begin{problembox}
\textbf{Q.5.2} \hfill \textbf{[Primary Source: GRB §12.28 Solved Ex 48 / NA Level-2 Q36]}
\label{q:qb-c5-02}

A quinhydrone electrode is set up in an unknown acidic buffer solution at $25^\circ\text{C}$ and coupled with a saturated calomel electrode ($E_{\text{SCE}} = +0.242\,\text{V}$). The cell EMF is measured to be $0.180\,\text{V}$ with the quinhydrone electrode as the positive pole. Given $E^\circ(\ce{Q, 2H+/H2Q}) = +0.699\,\text{V}$:
\begin{enumerate}[label=(\alph*)]
    \item Calculate the $\text{pH}$ of the buffer solution.
    \item Why cannot the quinhydrone electrode be used accurately in solutions of $\text{pH} > 8.5$?
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-II Sec A Q28, p. 14]} The EMF of a cell consisting of a hydrogen electrode dipping in a solution of unknown pH coupled with SCE is $0.450\,\text{V}$. The pH is: (a) $3.52$ (b) $7.61$ (c) $4.25$ (d) $5.80$.
    \item \textbf{[Variant v2: Pearson Ex-II Sec A Q58, p. 21]} In alkaline solution ($\text{pH} > 9$), hydroquinone undergoes: (a) oxidation by dissolved oxygen (b) ionization of phenolic $-OH$ groups ($K_a \approx 10^{-10}$) disrupting the equimolar $[\ce{Q}] = [\ce{H2Q}]$ ratio (c) dimerization (d) precipitation.
    \item \textbf{[Variant v3: Cengage Theory p. 40]} Write the potential equation for a glass electrode and explain how it determines pH across the full range $1 \le \text{pH} \le 12$.
\end{itemize}
\end{problembox}

\section{Subtopic 5.3: Latimer & Frost Oxidation State Diagrams}

\begin{problembox}
\textbf{Q.5.3} \hfill \textbf{[Primary Source: Atkins Focus 6 / Neeraj Kumar Part 1 Ex-II Sec B Q14]}
\label{q:qb-c5-03}

The Latimer diagram for manganese species in $1\,\text{M}$ acid solution ($\text{pH} = 0$) is:
\begin{equation*}
    \ce{MnO4^-} \xrightarrow{+0.56\,\text{V}} \ce{MnO4^2-} \xrightarrow{+2.27\,\text{V}} \ce{MnO2} \xrightarrow{+0.95\,\text{V}} \ce{Mn^3+} \xrightarrow{+1.51\,\text{V}} \ce{Mn^2+} \xrightarrow{-1.18\,\text{V}} \ce{Mn}
\end{equation*}
\begin{enumerate}[label=(\alph*)]
    \item Calculate the standard potential $E^\circ$ for the direct 5-electron reduction $\ce{MnO4^- + 8H+ + 5e^- -> Mn^2+ + 4H2O}$.
    \item Will manganate ion ($\ce{MnO4^2-}$) undergo spontaneous disproportionation in acid solution? Justify thermodynamically by calculating $E^\circ_{\text{disp}}$.
    \item Will $\ce{Mn^3+}$ undergo spontaneous disproportionation into $\ce{MnO2}$ and $\ce{Mn^2+}$?
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-II Sec A Q68, p. 22]} On a Frost diagram ($N E^\circ$ vs $N$), a species that lies above the line connecting its two neighboring oxidation states is: (a) stable to disproportionation (b) prone to spontaneous disproportionation (c) a reducing agent only (d) in its ground electronic state.
    \item \textbf{[Variant v2: Narendra Avasthi Level-3 Passage 5, p. 39]} Given the standard reduction potentials: $\ce{Fe^3+ + e^- -> Fe^2+}$ ($E^\circ = 0.77\,\text{V}$) and $\ce{Fe^2+ + 2e^- -> Fe}$ ($E^\circ = -0.44\,\text{V}$), calculate $E^\circ$ for $\ce{Fe^3+ + 3e^- -> Fe}$.
    \item \textbf{[Variant v3: Cengage Theory p. 46]} In a Latimer diagram, comproportionation occurs spontaneously between two oxidation states when: $E^\circ_{\text{right}} < E^\circ_{\text{left}}$ for the intermediate state.
\end{itemize}
\end{problembox}
"""

with open("question_bank/part04_concentration_cells.tex", "w", encoding="utf-8") as f:
    f.write(part04)
with open("question_bank/part05_equilibrium.tex", "w", encoding="utf-8") as f:
    f.write(part05)

print("Generated question_bank/part04_concentration_cells.tex and part05_equilibrium.tex successfully")
