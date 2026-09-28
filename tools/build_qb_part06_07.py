# -*- coding: utf-8 -*-
"""Generate question_bank/part06_electrolysis.tex and part07_batteries_corrosion.tex."""
import os

part06 = r"""\chapter{Master Problem Bank: Electrolysis, Faraday's Laws & Overvoltage}
\label{chap:qb_electrolysis}

\begin{tcolorbox}[enhanced,colback=subtlegold,colframe=accentamber,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part VI Organization: Electrolysis, Faraday's Laws & Kinetics}]
This part compiles all questions and quantitative problems on preferential discharge, overpotential ($\eta$) on various electrode materials, Faraday's 1st and 2nd laws, current efficiency, and industrial electrolytic cells from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 6.1: Preferential Discharge Theory & Overpotential ($\eta$)}

\begin{problembox}
\textbf{Q.6.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 2 Ex-II Sec B Q4 / GRB §12.3]}
\label{q:qb-c6-01}

Predict the primary product liberated at the cathode and at the anode during the electrolysis of an aqueous $1\,\text{M}$ solution of \ce{NaCl} under the following two distinct experimental conditions:
\begin{enumerate}[label=(\alph*)]
    \item Using inert platinum (Pt) electrodes at low current density
    \item Using a liquid mercury (Hg) cathode and graphite anode (Castner--Kellner cell)
\end{enumerate}
Explain the physical role of hydrogen overvoltage on mercury ($\eta_{\ce{H2/Hg}} \approx 1.5\,\text{V}$) in determining the cathodic product.

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-II Sec A Q56, p. 21]} During the electrolysis of aqueous \ce{NaCl} with mercury cathode, sodium is discharged instead of hydrogen because: (a) $E^\circ(\ce{Na+/Na}) > E^\circ(\ce{H+/H2})$ (b) hydrogen overvoltage on mercury is exceptionally high (c) sodium forms amalgam with mercury lowering its discharge potential (d) both (b) and (c).
    \item \textbf{[Variant v2: Narendra Avasthi Level-1 Q142, p. 20]} During electrolysis of aqueous \ce{CuSO4} solution using copper electrodes, the process taking place at the anode is: (a) evolution of \ce{O2} (b) evolution of \ce{SO2} (c) dissolution of copper into $\ce{Cu^2+}$ (d) deposition of sulfate.
    \item \textbf{[Variant v3: Cengage Theory p. 78]} Why does chlorine gas evolve at the anode during electrolysis of concentrated aqueous \ce{NaCl} even though thermodynamic standard reduction potential of oxygen ($E^\circ = 1.23\,\text{V}$) is lower than that of chlorine ($E^\circ = 1.36\,\text{V}$)?
\end{itemize}
\end{problembox}

\section{Subtopic 6.2: Faraday's 1st and 2nd Laws & Current Efficiency}

\begin{problembox}
\textbf{Q.6.2} \hfill \textbf{[Primary Source: GRB Practice Problem 64, p. 52 / NA Level-1 Q58]}
\label{q:qb-c6-02}

A constant current of $3.0\,\text{A}$ is passed for $2.0\,\text{hours}$ through three electrolytic cells connected in series containing solutions of:
(A) \ce{AgNO3(aq)}, (B) \ce{CuSO4(aq)}, (C) \ce{CrCl3(aq)}.
Assuming $100\%$ current efficiency, calculate the mass deposited at the cathode in each cell:
\begin{enumerate}[label=(\alph*)]
    \item Mass of silver (Atomic mass $= 108.0$)
    \item Mass of copper (Atomic mass $= 63.5$)
    \item Mass of chromium (Atomic mass $= 52.0$)
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Neeraj Kumar Part 2 Ex-I Q68, p. 38]} The same quantity of electrical charge that deposited $1.08\,\text{g}$ of silver from \ce{AgNO3} will deposit what mass of aluminium from molten \ce{AlCl3}? (a) $0.09\,\text{g}$ (b) $0.27\,\text{g}$ (c) $0.81\,\text{g}$ (d) $1.08\,\text{g}$.
    \item \textbf{[Variant v2: Essential §24.4 Solved Ex 3, p. 863]} What current strength in amperes is required to deposit $5.00\,\text{g}$ of gold from a solution of \ce{HAuCl4} in $1.0\,\text{hour}$? ($\text{At. mass of Au} = 197.0$, $n = 3$).
    \item \textbf{[Variant v3: Pearson Ex-I Q82, p. 7]} In an electroplating process, a current of $10.0\,\text{A}$ deposits $12.0\,\text{g}$ of zinc in $1.0\,\text{hour}$. The current efficiency ($\eta_{\text{curr}}$) is: (a) $98.5\%$ (b) $82.4\%$ (c) $65.2\%$ (d) $50.0\%$.
\end{itemize}
\end{problembox}

\begin{problembox}
\textbf{Q.6.3} \hfill \textbf{[Primary Source: Narendra Avasthi Level-2 Q10, p. 25 / PRSN Ex-II Q8]}
\label{q:qb-c6-03}

An aqueous solution of $0.1\,\text{M } \ce{CuSO4}$ ($1.0\,\text{L}$) is electrolyzed between inert Pt electrodes with a steady current of $9.65\,\text{A}$ for $1000\,\text{seconds}$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the mass of copper deposited at the cathode.
    \item Calculate the total volume of oxygen gas evolved at the anode measured at STP ($0^\circ\text{C}, 1\,\text{atm}$).
    \item Calculate the final $\text{pH}$ of the solution after electrolysis (assume volume remains constant at $1.0\,\text{L}$).
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Cengage DPP 3.2 Q19, p. 4]} A current strength of $96.5\,\text{A}$ is passed for $10\,\text{seconds}$ through $1\,\text{L}$ of $0.1\,\text{M}$ aqueous \ce{CuSO4}. The pH of the resulting solution is: (a) $1.0$ (b) $2.0$ (c) $3.0$ (d) $7.0$.
    \item \textbf{[Variant v2: Neeraj Kumar Part 2 Ex-II Sec A Q34, p. 44]} When $100\,\text{mL}$ of $0.2\,\text{M } \ce{AgNO3}$ is electrolyzed until half the silver is deposited, how many moles of $\ce{H+}$ ions are produced in the electrolyte?
    \item \textbf{[Variant v3: GRB Practice Problem 68, p. 52]} Electrolysis of dilute \ce{H2SO4} for $1.0\,\text{hour}$ produces $112\,\text{mL}$ of \ce{O2} at STP at the anode. What volume of \ce{H2} is evolved at the cathode at the same temperature and pressure?
\end{itemize}
\end{problembox}
"""

part07 = r"""\chapter{Master Problem Bank: Commercial Cells, Fuel Cells & Corrosion}
\label{chap:qb_batteries_corrosion}

\begin{tcolorbox}[enhanced,colback=subtleamber,colframe=primarynavy,arc=2mm,boxrule=1pt,
    title=\textbf{\large Part VII Organization: Commercial Batteries, Fuel Cells & Corrosion}]
This part compiles all questions and multi-step quantitative problems on primary dry cells, secondary storage batteries (lead-acid, nicad, lithium-ion), hydrogen-oxygen fuel cells, and electrochemical corrosion mechanisms from all 8 books. Identical and redundant variants from other books are co-located beneath each primary problem with full source citations.
\end{tcolorbox}

\section{Subtopic 7.1: Secondary Batteries (Lead-Acid Storage Accumulator)}

\begin{problembox}
\textbf{Q.7.1} \hfill \textbf{[Primary Source: Neeraj Kumar Part 1 Ex-II Sec C Passage 3 / GRB §12.31]}
\label{q:qb-c7-01}

For the lead-acid storage accumulator during discharge:
\begin{enumerate}[label=(\alph*)]
    \item Write the balanced half-reactions at the negative electrode (\ce{Pb}) and positive electrode (\ce{PbO2}), and the overall net cell reaction.
    \item A lead storage battery contains $3.0\,\text{L}$ of $38\%\,(w/w)$ \ce{H2SO4} ($\text{density} = 1.28\,\text{g\,cm}^{-3}$). After discharging at a steady current of $4.0\,\text{A}$ for $50.0\,\text{hours}$, calculate the mass of \ce{H2SO4} consumed and the mass of \ce{PbSO4} formed on the plates.
    \item Explain why the electrolyte density falls to $\approx 1.15\,\text{g\,cm}^{-3}$ upon complete discharge, and how this property is utilized to assess the state of charge.
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Narendra Avasthi Level-3 Passage 4, p. 38]} During recharging of a lead-acid cell, the reaction occurring at the electrode connected to the positive terminal of the charger is: (a) $\ce{PbSO4 -> Pb}$ (b) $\ce{PbSO4 -> PbO2}$ (c) $\ce{Pb -> PbSO4}$ (d) $\ce{H2O -> H2}$.
    \item \textbf{[Variant v2: Pearson Ex-II Sec D Q8, p. 34]} A commercial lead storage battery delivers $100\,\text{A}\cdot\text{h}$ of charge. The theoretical minimum mass of \ce{PbO2} consumed is: (a) $446\,\text{g}$ (b) $223\,\text{g}$ (c) $892\,\text{g}$ (d) $112\,\text{g}$.
    \item \textbf{[Variant v3: Cengage Theory p. 95]} What is the nominal single-cell voltage of a fully charged lead-acid cell, and how many cells are placed in series to construct a standard $12\,\text{V}$ automobile battery?
\end{itemize}
\end{problembox}

\section{Subtopic 7.2: Primary Batteries & Secondary Alkaline Cells}

\begin{problembox}
\textbf{Q.7.2} \hfill \textbf{[Primary Source: GRB §12.30 Objective Q125 / NA Level-1 Q180]}
\label{q:qb-c7-02}

In a standard Leclanch\'{e} dry cell:
\begin{enumerate}[label=(\alph*)]
    \item What constitutes the anode and cathode materials?
    \item What is the chemical function of \ce{MnO2} in the electrolyte paste?
    \item What is the role of \ce{ZnCl2} in preventing gas pressure buildup from released \ce{NH3}?
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-I Q102, p. 11]} In the alkaline dry cell, the electrolyte paste is: (a) \ce{NH4Cl + ZnCl2} (b) \ce{KOH} (c) \ce{H2SO4} (d) \ce{NaOH}.
    \item \textbf{[Variant v2: Neeraj Kumar Part 1 Ex-II Sec D Q4, p. 28]} In a nickel-cadmium (Nicad) rechargeable cell, the reaction at the cathode during discharge is: (a) reduction of \ce{NiO(OH)} to \ce{Ni(OH)2} (b) oxidation of Cd (c) reduction of \ce{Cd(OH)2} (d) oxidation of Ni.
    \item \textbf{[Variant v3: Cengage Theory p. 93]} Why does a mercury button cell maintain a constant operating voltage ($\approx 1.35\,\text{V}$) throughout its lifetime, whereas a Leclanché dry cell voltage drops continuously?
\end{itemize}
\end{problembox}

\section{Subtopic 7.3: Fuel Cells & Thermodynamic Efficiency ($\eta$)}

\begin{problembox}
\textbf{Q.7.3} \hfill \textbf{[Primary Source: Atkins Topic 6C.4 / Neeraj Kumar Part 1 Ex-II Sec C Passage 5]}
\label{q:qb-c7-03}

For the alkaline hydrogen--oxygen fuel cell operating at $298\,\text{K}$:
\begin{equation*}
    \ce{2H2(g) + O2(g) -> 2H2O(l)}
\end{equation*}
Given: $\Delta G^\circ = -474.4\,\text{kJ}$ and $\Delta H^\circ = -571.6\,\text{kJ}$ for the reaction as written ($n = 4$).
\begin{enumerate}[label=(\alph*)]
    \item Calculate the standard theoretical cell potential $E^\circ_{\text{cell}}$.
    \item Calculate the maximum theoretical thermodynamic efficiency $\eta_{\text{th}} = \frac{\Delta G^\circ}{\Delta H^\circ} \times 100\%$.
    \item Explain why fuel cell efficiencies ($\sim 70\text{--}80\%$) exceed the Carnot efficiency limit of conventional thermal power plants.
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: GRB §12.32 Solved Ex 52, p. 42]} In the Apollo space mission, the alkaline \ce{H2-O2} fuel cell produced both electrical power and drinking water for astronauts. Write the electrode reactions in concentrated hot \ce{KOH} electrolyte.
    \item \textbf{[Variant v2: Narendra Avasthi Level-3 Passage 6, p. 40]} If a fuel cell reaction has a positive temperature coefficient $(\partial E/\partial T)_P > 0$, its thermodynamic efficiency $\eta$: (a) exceeds $100\%$ (b) is less than $100\%$ (c) equals zero (d) cannot be defined.
    \item \textbf{[Variant v3: Cengage Theory p. 100]} Contrast the alkaline fuel cell with the Proton Exchange Membrane Fuel Cell (PEMFC) in terms of electrolyte and operating temperature.
\end{itemize}
\end{problembox}

\section{Subtopic 7.4: Corrosion Mechanism, Rusting & Protection}

\begin{problembox}
\textbf{Q.7.4} \hfill \textbf{[Primary Source: GRB §12.33 / NA Level-1 Q195]}
\label{q:qb-c7-04}

Explain the electrochemical mechanism of rusting of iron in the presence of moist air containing dissolved $\ce{CO2}$:
\begin{enumerate}[label=(\alph*)]
    \item Write the anode and cathode half-reactions that form the localized galvanic micro-cells.
    \item What is the chemical formula of rust?
    \item Distinguish between sacrificial protection (galvanization with zinc) and cathodic protection using impressed direct current. Why is zinc preferred over tin for protecting iron sheets that are exposed to surface scratches?
\end{enumerate}

\tcbline
\textbf{\color{accentamber}Cross-Book Redundant / Identical Variants:}
\begin{itemize}[leftmargin=*,itemsep=2pt]
    \item \textbf{[Variant v1: Pearson Ex-II Sec D Q18, p. 35]} Rusting of iron is accelerated by: (a) presence of electrolytes (salts like \ce{NaCl}) (b) acidic environment ($\text{pH} < 7$) (c) contact with less electropositive metals (e.g. Cu, Sn) (d) all of the above.
    \item \textbf{[Variant v2: Neeraj Kumar Part 1 Ex-II Sec D Q8, p. 28]} In cathodic protection of underground pipelines, blocks of which active metal are connected to the steel pipe? (a) Magnesium or Zinc (b) Copper (c) Silver (d) Lead.
    \item \textbf{[Variant v3: Cengage Theory p. 104]} Explain why coating iron with tin (\ce{Sn}) accelerates corrosion if the tin coating is scratched, whereas coating with zinc (\ce{Zn}) continues to protect the underlying iron even when scratched.
\end{itemize}
\end{problembox}
"""

with open("question_bank/part06_electrolysis.tex", "w", encoding="utf-8") as f:
    f.write(part06)
with open("question_bank/part07_batteries_corrosion.tex", "w", encoding="utf-8") as f:
    f.write(part07)

print("Generated question_bank/part06_electrolysis.tex and part07_batteries_corrosion.tex successfully")
