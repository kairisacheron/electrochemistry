# -*- coding: utf-8 -*-
"""Generate question_bank/part02_galvanic_cells.tex and part03_thermodynamics.tex."""
import os

part02 = r"""\chapter{Master Problem Bank: Galvanic Cells, Electrodes & Electrochemical Series}
\label{chap:qb_galvanic_cells}

\begin{tcolorbox}[enhanced,colback=subtleblue,colframe=primarynavy,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part II Organization: Galvanic Cells, Reference Electrodes & EC Series}]
This part compiles all questions and quantitative problems on electrode potentials, standard hydrogen electrode (SHE), calomel, silver-silver chloride, Daniell cell construction, salt bridge mechanics, and the electrochemical series from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 2.1: Electrode Potential & Electrical Double Layer}

\begin{problembox}
\textbf{Q.2.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-I Q1 / GRB §12.11]}
\label{q:qb-c2-01}

A metal rod is dipped in a solution of its own ions. Its single electrode potential is independent of:
\begin{enumerate}[label=(\alph*)]
    \item Temperature of the solution
    \item Concentration of the metal ions in solution
    \item Surface area of the metal rod exposed to the solution
    \item Nature of the metal and solvent
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-I Q1, p. 1]} The electrode potential of a metal does not depend on: (a) area of electrode (b) concentration of ions (c) temperature (d) pressure in case of gas electrodes.
    \item \textbf{[Variant v2: Narendra Avasthi Level-1 Q76, p. 12]} An intensive property among the following is: (a) electrode potential $E$ (b) resistance $R$ (c) Gibbs free energy change $\Delta G$ (d) heat capacity.
    \item \textbf{[Variant v3: Cengage Theory p. 3]} Explain the origin of the potential difference at a metal-solution interface using the concept of Helmholtz electrical double layer and Stern's compact/diffuse model.
\end{itemize}
\end{problembox}

\begin{problembox}
\textbf{Q.2.2} \hfill \textbf{[Primary Source: Atkins Topic 6C.1 / GRB §12.16]}
\label{q:qb-c2-02}

Why is the potential of the Standard Hydrogen Electrode (SHE) defined as zero at all temperatures, whereas the standard reduction potential of the saturated calomel electrode (SCE) has a non-zero temperature coefficient ($\partial E/\partial T \approx -0.65\,\text{mV\,K}^{-1}$)?

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-I Q7, p. 1]} A standard hydrogen electrode has zero electrode potential because: (a) hydrogen is easiest to oxidize (b) this electrode potential is adopted as zero by international thermodynamic convention (c) hydrogen has one electron (d) hydrogen is the lightest element.
    \item \textbf{[Variant v2: Narendra Avasthi Level-1 Q82, p. 13]} The calomel electrode is reversible with respect to: (a) $\ce{Hg2^2+}$ (b) $\ce{Hg^2+}$ (c) $\ce{Cl-}$ (d) $\ce{H+}$.
    \item \textbf{[Variant v3: Pearson Ex-I Q15, p. 2]} What is the composition and standard potential of the saturated calomel electrode at $25^\circ\text{C}$? (a) $+0.2422\,\text{V}$ (b) $+0.2800\,\text{V}$ (c) $+0.3338\,\text{V}$ (d) $0.0000\,\text{V}$.
\end{itemize}
\end{problembox}

\section{Subtopic 2.2: Daniell Cell & Salt Bridge Dynamics}

\begin{problembox}
\textbf{Q.2.3} \hfill \textbf{[Primary Source: GRB §12.13 Solved Ex 33 / NA Level-1 Q88]}
\label{q:qb-c2-03}

For the Daniell cell $\ce{Zn(s)} \mid \ce{ZnSO4(aq, } 1\,\text{M}\ce{)} \parallel \ce{CuSO4(aq, } 1\,\text{M}\ce{)} \mid \ce{Cu(s)}$:
\begin{enumerate}[label=(\alph*)]
    \item Write the anode half-reaction, cathode half-reaction, and overall cell reaction.
    \item What is the function of the salt bridge, and why does current stop flowing if the salt bridge is removed?
    \item Why cannot \ce{KCl} be used in a salt bridge if the cell contains $\ce{Ag+}$ or $\ce{Pb^2+}$ ions?
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-I Q22, p. 2]} A salt bridge contains \ce{KNO3} in agar-agar gel because: (a) \ce{K+} and \ce{NO3-} have almost equal ionic velocities ($t_+ \approx t_- \approx 0.5$) (b) agar-agar conducts current (c) it prevents mixing of solutions (d) all of these.
    \item \textbf{[Variant v2: Pearson Ex-I Q12, p. 2]} What happens when a Daniell cell operates for a long period? (a) mass of Zn rod increases (b) concentration of $\ce{Cu^2+}$ increases (c) mass of Cu rod increases and $[\ce{Zn^2+}]$ increases (d) cell potential increases.
    \item \textbf{[Variant v3: Cengage DPP 3.2 Q5, p. 3]} In which of the following electrochemical cells is a salt bridge NOT required? (a) Lead-acid storage battery (b) Daniell cell (c) Standard cadmium cell (d) Concentration cell without transference.
\end{itemize}
\end{problembox}

\section{Subtopic 2.3: Electrochemical Series & Feasibility of Reactions}

\begin{problembox}
\textbf{Q.2.4} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-I Q3 / PRSN Ex-I Q8]}
\label{q:qb-c2-04}

The standard reduction potentials are given as:
$E^\circ(\ce{Mg^2+/Mg}) = -2.37\,\text{V}$,
$E^\circ(\ce{Al^3+/Al}) = -1.66\,\text{V}$,
$E^\circ(\ce{Zn^2+/Zn}) = -0.76\,\text{V}$,
$E^\circ(\ce{Fe^2+/Fe}) = -0.44\,\text{V}$,
$E^\circ(\ce{Cu^2+/Cu}) = +0.34\,\text{V}$,
$E^\circ(\ce{Ag+/Ag}) = +0.80\,\text{V}$.
Which of the following processes will occur spontaneously under standard conditions?
\begin{enumerate}[label=(\alph*)]
    \item Storing aqueous \ce{CuSO4} in a zinc container
    \item Stirring an \ce{Al(NO3)3} solution with a copper spoon
    \item Precipitation of silver from \ce{AgNO3} solution upon adding copper turnings
    \item Evolution of \ce{H2} gas upon adding copper to dilute \ce{HCl}
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: GRB Objective Set-1 Q45, p. 70]} Which metal will displace hydrogen from dilute \ce{H2SO4}? (a) Ag (b) Cu (c) Fe (d) Au.
    \item \textbf{[Variant v2: Narendra Avasthi Level-1 Q92, p. 14]} Given $E^\circ(\ce{Cr^3+/Cr}) = -0.74\,\text{V}$, $E^\circ(\ce{MnO4-/Mn^2+}) = +1.51\,\text{V}$, $E^\circ(\ce{Cr2O7^2-/Cr^3+}) = +1.33\,\text{V}$, $E^\circ(\ce{Cl/Cl-}) = +1.36\,\text{V}$. The strongest oxidizing agent is: (a) $\ce{MnO4-}$ (b) $\ce{Cl-}$ (c) $\ce{Cr^3+}$ (d) $\ce{Mn^2+}$.
    \item \textbf{[Variant v3: Cengage Theory Concept App 1 Q4, p. 14]} Can an aqueous solution of $1\,\text{M } \ce{FeSO4}$ be stored in a nickel vessel? Given $E^\circ(\ce{Ni^2+/Ni}) = -0.25\,\text{V}, E^\circ(\ce{Fe^2+/Fe}) = -0.44\,\text{V}$.
\end{itemize}
\end{problembox}
"""

part03 = r"""\chapter{Master Problem Bank: Thermodynamics of Cells & Nernst Equation}
\label{chap:qb_thermodynamics}

\begin{tcolorbox}[enhanced,colback=subtleamber,colframe=accentamber,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part III Organization: Nernst Equation & Cell Thermodynamics}]
This part compiles all questions and multi-step quantitative problems on the Nernst equation, equilibrium constants, cell Gibbs energy, enthalpy, entropy, temperature coefficients, and reversible cell heat from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 3.1: Nernst Equation Calculations}

\begin{problembox}
\textbf{Q.3.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-I Q42 / NA Level-1 Q105]}
\label{q:qb-c3-01}

Calculate the EMF of the cell at $25^\circ\text{C}$:
\begin{equation*}
    \ce{Zn(s)} \mid \ce{Zn^2+(aq, } 0.01\,\text{M}\ce{)} \parallel \ce{Fe^2+(aq, } 0.001\,\text{M}\ce{)} \mid \ce{Fe(s)}
\end{equation*}
Given: $E^\circ(\ce{Zn^2+/Zn}) = -0.763\,\text{V}$ and $E^\circ(\ce{Fe^2+/Fe}) = -0.440\,\text{V}$.
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $+0.3525\,\text{V}$
    \item $+0.2935\,\text{V}$
    \item $+0.3230\,\text{V}$
    \item $-0.3230\,\text{V}$
\end{enumerate}
\end{multicols}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-I Q45, p. 4]} For the cell $\ce{Cd} \mid \ce{Cd^2+}(0.01\,\text{M}) \parallel \ce{Ag+}(0.5\,\text{M}) \mid \ce{Ag}$, given $E^\circ(\ce{Cd^2+/Cd}) = -0.40\,\text{V}$ and $E^\circ(\ce{Ag+/Ag}) = +0.80\,\text{V}$, calculate $E_{\text{cell}}$ at $298\,\text{K}$.
    \item \textbf{[Variant v2: GRB Practice Problem 12, p. 47]} Calculate the potential of a Daniell cell when $[\ce{Zn^2+}] = 0.5\,\text{M}$ and $[\ce{Cu^2+}] = 0.01\,\text{M}$. Standard potential $E^\circ_{\text{cell}} = 1.10\,\text{V}$.
    \item \textbf{[Variant v3: Cengage DPP 3.3 Q3, p. 5]} The potential of a hydrogen electrode at $298\,\text{K}$ in contact with a solution of $\text{pH} = 3$ and $P_{\ce{H2}} = 1\,\text{atm}$ is: (a) $-0.177\,\text{V}$ (b) $+0.177\,\text{V}$ (c) $-0.059\,\text{V}$ (d) $0.000\,\text{V}$.
\end{itemize}
\end{problembox}

\begin{problembox}
\textbf{Q.3.2} \hfill \textbf{[Primary Source: Narendra Avasthi Level-2 Q38 / PRSN Ex-II Q18]}
\label{q:qb-c3-02}

For the cell $\ce{Pt} \mid \ce{H2}(1\,\text{bar}) \mid \ce{HA}(0.1\,\text{M}) \parallel \ce{Ag+}(0.1\,\text{M}) \mid \ce{Ag}$, the cell EMF is measured to be $0.985\,\text{V}$ at $298\,\text{K}$. Given $E^\circ(\ce{Ag+/Ag}) = +0.800\,\text{V}$, calculate the acid dissociation constant $K_a$ of the weak monobasic acid \ce{HA}.

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-II Sec A Q24, p. 14]} The EMF of the cell $\ce{Pt, H2}(1\,\text{atm}) \mid \text{Buffer } (\ce{CH3COOH} + \ce{CH3COONa}) \parallel \ce{KCl}(\text{sat}) \mid \ce{Hg2Cl2}, \ce{Hg}$ is $0.518\,\text{V}$. If $E_{\text{SCE}} = 0.242\,\text{V}$, calculate the pH of the buffer.
    \item \textbf{[Variant v2: GRB Practice Problem 24, p. 48]} A hydrogen electrode dipping into a solution of an organic acid of unknown strength gives an EMF of $0.236\,\text{V}$ when coupled with a standard calomel electrode. Calculate the pH and $[\ce{H+}]$ of the solution.
\end{itemize}
\end{problembox}

\section{Subtopic 3.2: Equilibrium Constant ($K_{eq}$) from $E^\circ_{\text{cell}}$}

\begin{problembox}
\textbf{Q.3.3} \hfill \textbf{[Primary Source: GRB Practice Problem 34, p. 49 / NA Level-1 Q118]}
\label{q:qb-c3-03}

Find the equilibrium constant $K_{eq}$ at $298\,\text{K}$ for the reaction:
\begin{equation*}
    \ce{Cu^2+(aq) + In+(aq) <=> Cu+(aq) + In^2+(aq)}
\end{equation*}
Given: $E^\circ(\ce{Cu^2+/Cu+}) = +0.15\,\text{V}$ and $E^\circ(\ce{In^2+/In+}) = -0.42\,\text{V}$.
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $1.0 \times 10^5$
    \item $4.4 \times 10^9$
    \item $2.1 \times 10^{19}$
    \item $8.8 \times 10^{-10}$
\end{enumerate}
\end{multicols}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 1 Ex-I Q65, p. 6]} Calculate the equilibrium constant for the disproportionation reaction $\ce{2Cu+(aq) <=> Cu^2+(aq) + Cu(s)}$ at $25^\circ\text{C}$. Given $E^\circ(\ce{Cu+/Cu}) = +0.52\,\text{V}$ and $E^\circ(\ce{Cu^2+/Cu}) = +0.34\,\text{V}$.
    \item \textbf{[Variant v2: Pearson Ex-I Q60, p. 6]} For the cell reaction $\ce{Sn(s) + 2Fe^3+(aq) -> Sn^2+(aq) + 2Fe^2+(aq)}$, $E^\circ_{\text{cell}} = 0.61\,\text{V}$. The equilibrium constant $K$ is approximately: (a) $10^{10}$ (b) $10^{20}$ (c) $10^{30}$ (d) $10^5$.
    \item \textbf{[Variant v3: Cengage DPP 3.3 Q7, p. 5]} The relationship between $\Delta G^\circ$ and $E^\circ_{\text{cell}}$ implies that for an electrochemical cell to be in chemical equilibrium, the required condition is: (a) $E^\circ_{\text{cell}} = 0$ (b) $E_{\text{cell}} = 0$ (c) $\Delta G^\circ = 0$ (d) $Q = 1$.
\end{itemize}
\end{problembox}

\section{Subtopic 3.3: Cell Thermodynamics: $\Delta G, \Delta S, \Delta H$ & Temperature Coefficient}

\begin{problembox}
\textbf{Q.3.4} \hfill \textbf{[Primary Source: Atkins Topic 6C.4 / Neeraj Kumar Part 1 Ex-II Sec A Q32]}
\label{q:qb-c3-04}

The EMF of the standard Weston cadmium cell is expressed as a function of temperature:
\begin{equation*}
    E_t = 1.01845 - 4.05 \times 10^{-5}(t - 20) - 9.5 \times 10^{-7}(t - 20)^2 \quad (\text{in Volts})
\end{equation*}
where $t$ is the temperature in $^\circ\text{C}$. For the cell reaction:
\begin{equation*}
    \ce{Cd(s) + Hg2SO4(s) + \tfrac{8}{3}H2O(l) -> CdSO4.\tfrac{8}{3}H2O(s) + 2Hg(l)} \quad (n = 2)
\end{equation*}
Calculate at $t = 25^\circ\text{C}$:
\begin{enumerate}[label=(\alph*)]
    \item The temperature coefficient $\left(\frac{\partial E}{\partial T}\right)_P$
    \item The Gibbs free energy change $\Delta G$ in $\text{kJ\,mol}^{-1}$
    \item The entropy change $\Delta S$ in $\text{J\,K}^{-1}\,\text{mol}^{-1}$
    \item The reaction enthalpy $\Delta H$ in $\text{kJ\,mol}^{-1}$
    \item The reversible heat exchange $q_{\text{rev}}$ with the surroundings
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: GRB Practice Problem 28, p. 48]} The EMF of a galvanic cell is $1.05\,\text{V}$ at $298\,\text{K}$ and its temperature coefficient is $-4.0 \times 10^{-4}\,\text{V\,K}^{-1}$. If $n = 2$, calculate $\Delta H$ for the cell reaction.
    \item \textbf{[Variant v2: Narendra Avasthi Level-2 Q48, p. 28]} A cell has $E = 1.20\,\text{V}$ and $\Delta H = -200\,\text{kJ\,mol}^{-1}$ for a $2$-electron process. The temperature coefficient $(\partial E/\partial T)_P$ is: (a) $+5.4 \times 10^{-4}\,\text{V\,K}^{-1}$ (b) $-5.4 \times 10^{-4}\,\text{V\,K}^{-1}$ (c) $+2.7 \times 10^{-4}\,\text{V\,K}^{-1}$ (d) zero.
    \item \textbf{[Variant v3: Cengage DPP 3.4 Q4, p. 7]} If a cell absorbs heat from its surroundings during reversible operation at constant $T$ and $P$, then: (a) $(\partial E/\partial T)_P > 0$ (b) $(\partial E/\partial T)_P < 0$ (c) $\Delta H > \Delta G$ (d) Both (a) and (c).
\end{itemize}
\end{problembox}
"""

with open("question_bank/part02_galvanic_cells.tex", "w", encoding="utf-8") as f:
    f.write(part02)
with open("question_bank/part03_thermodynamics.tex", "w", encoding="utf-8") as f:
    f.write(part03)

print("Generated question_bank/part02_galvanic_cells.tex and part03_thermodynamics.tex successfully")
