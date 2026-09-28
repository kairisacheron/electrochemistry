# -*- coding: utf-8 -*-
"""Write exercises/matrix_match.tex."""
import os

matrix_match = r"""\chapter*{Global Exercise Bank --- Matrix Match Questions}
\addcontentsline{toc}{chapter}{Global Exercise Bank: Matrix Match Questions}
\label{chap:matrix_match}

\begin{tcolorbox}[enhanced,colback=subtlegreen,colframe=cengagegreen,arc=2mm,boxrule=1pt,
    title=\textbf{\large Multi-Concept Matrix Matching Problems (All Chapters)}]
$4 \times 4$ and $4 \times 5$ cross-topic matching matrices testing structural, mechanistic, and numerical principles.
Sources: \textbf{[NA]} Level-2 Matchings, \textbf{[PRSN]} Advanced Matchings, \textbf{[NRJ]} Matrix-Match.
\end{tcolorbox}

\begin{problembox}
\textbf{MM.1} \hfill \textbf{[NA Level-2 / PRSN]}

Match the electrode system in Column~I with its characteristic redox half-cell reaction or potential equation in Column~II:

\begin{center}
\begin{tabular}{p{0.05\textwidth}p{0.40\textwidth}|p{0.05\textwidth}p{0.42\textwidth}}
\toprule
\multicolumn{2}{c|}{\textbf{Column I (Electrode System)}} & \multicolumn{2}{c}{\textbf{Column II (Characteristics / Formula)}} \\
\midrule
(A) & Calomel Electrode & (P) & $E = E^\circ - \frac{2.303 RT}{F} \text{pH}$ \\
(B) & Quinhydrone Electrode & (Q) & Reversible with respect to chloride ion; $E^\circ \approx +0.2422\,\text{V}$ for saturated \ce{KCl} \\
(C) & Glass Electrode & (R) & Involves keto-enol / quinone-hydroquinone organic redox equilibrium \\
(D) & Hydrogen Electrode & (S) & Potential depends on exchange of alkali metal cations across a hydrated silicate membrane \\
    & & (T) & Reference electrode with $E^\circ = 0.000\,\text{V}$ at all temperatures by convention \\
\bottomrule
\end{tabular}
\end{center}
\end{problembox}
\begin{solution}
\textbf{Match: (A) $\to$ (Q); (B) $\to$ (P, R); (C) $\to$ (S); (D) $\to$ (P, T)}

\textbf{Detailed Explanations:}
\begin{itemize}
    \item \textbf{(A) Calomel Electrode:} Consists of $\ce{Hg(l)} \mid \ce{Hg2Cl2(s)} \mid \ce{Cl^-}$. It is a metal-insoluble metal salt electrode reversible with respect to chloride ion. For saturated \ce{KCl} at $25^\circ\text{C}$, $E = +0.2422\,\text{V}$. Matches \textbf{(Q)}.
    \item \textbf{(B) Quinhydrone Electrode:} Contains an equimolar molecular complex of benzoquinone (\ce{Q}) and hydroquinone (\ce{H2Q}). The reaction is $\ce{Q + 2H+ + 2e^- <=> H2Q}$. Its potential is $E = E^\circ - \frac{RT}{F}\ln \frac{1}{[\ce{H+}]} = E^\circ - 0.0591\,\text{pH}$ at $25^\circ\text{C}$. Matches \textbf{(P, R)}.
    \item \textbf{(C) Glass Electrode:} An ion-selective membrane electrode consisting of a thin, specially formulated lithium/sodium silicate glass bulb. Its potential arises from ion-exchange equilibria at the hydrated gel layer on the inner and outer surfaces. Matches \textbf{(S)}.
    \item \textbf{(D) Hydrogen Electrode:} The primary standard reference electrode with $E^\circ \equiv 0.000\,\text{V}$ at all temperatures by international thermodynamic convention (T). At $P_{\ce{H2}} = 1\,\text{bar}$, $E = -0.0591\,\text{pH}$ at $298\,\text{K}$ (P). Matches \textbf{(P, T)}.
\end{itemize}
\end{solution}

\begin{problembox}
\textbf{MM.2} \hfill \textbf{[NRJ Matrix-Match / NA]}

Match the conductometric titration in Column~I with the shape of the conductance curve / behavior of conductance prior to the equivalence point in Column~II (titrant added from burette into analyte solution in beaker):

\begin{center}
\begin{tabular}{p{0.05\textwidth}p{0.42\textwidth}|p{0.05\textwidth}p{0.40\textwidth}}
\toprule
\multicolumn{2}{c|}{\textbf{Column I (Titration System)}} & \multicolumn{2}{c}{\textbf{Column II (Conductance Curve Characteristics)}} \\
\midrule
(A) & \ce{HCl(aq)} vs \ce{NaOH(aq)} & (P) & Sharp drop in conductance before equivalence point due to removal of highly mobile $\ce{H+}$ ions \\
(B) & \ce{CH3COOH(aq)} vs \ce{NaOH(aq)} & (Q) & Initial slight decrease followed by steady increase before equivalence point due to buffer formation \\
(C) & \ce{HCl(aq)} vs \ce{NH4OH(aq)} & (R) & Conductance remains almost constant after equivalence point due to weak ionization of excess titrant \\
(D) & \ce{AgNO3(aq)} vs \ce{KCl(aq)} & (S) & Conductance remains almost constant before equivalence point, then rises sharply after \\
    & & (T) & Conductance increases steeply after equivalence point due to excess unneutralized mobile \ce{OH-} ions \\
\bottomrule
\end{tabular}
\end{center}
\end{problembox}
\begin{solution}
\textbf{Match: (A) $\to$ (P, T); (B) $\to$ (Q, T); (C) $\to$ (P, R); (D) $\to$ (S)}

\textbf{Detailed Explanations:}
\begin{itemize}
    \item \textbf{(A) \ce{HCl} vs \ce{NaOH}:} Strong acid vs strong base. Before equivalence, $\ce{H+}$ ($\lambda^\circ \approx 350\,\text{S\,cm}^2\,\text{mol}^{-1}$) is replaced by $\ce{Na+}$ ($\lambda^\circ \approx 50$), causing conductance to drop steeply (P). After equivalence, excess $\ce{Na+}$ and highly mobile $\ce{OH-}$ ($\lambda^\circ \approx 198$) cause conductance to rise steeply (T). Matches \textbf{(P, T)}.
    \item \textbf{(B) \ce{CH3COOH} vs \ce{NaOH}:} Weak acid vs strong base. Addition of \ce{NaOH} initially suppresses \ce{CH3COOH} dissociation (slight dip), then creates a \ce{CH3COOH}/\ce{CH3COONa} buffer where concentration of conducting $\ce{Na+}$ and $\ce{CH3COO-}$ increases steadily (Q). After equivalence, excess \ce{OH-} causes steep rise (T). Matches \textbf{(Q, T)}.
    \item \textbf{(C) \ce{HCl} vs \ce{NH4OH}:} Strong acid vs weak base. Initial steep drop as $\ce{H+}$ is replaced by $\ce{NH4+}$ (P). Beyond equivalence, excess \ce{NH4OH} is weakly ionized in the presence of $\ce{NH4+}$ (common ion effect), so conductance remains almost flat/constant (R). Matches \textbf{(P, R)}.
    \item \textbf{(D) \ce{AgNO3} vs \ce{KCl}:} Precipitation titration: $\ce{Ag+ + NO3- + K+ + Cl- -> AgCl(s) v + K+ + NO3-}$. Since $\lambda^\circ(\ce{Ag+}) \approx 61.9$ and $\lambda^\circ(\ce{K+}) \approx 73.5$ are very similar, conductance remains nearly constant before equivalence. After equivalence, added \ce{K+} and \ce{Cl-} cause a sharp rise (S). Matches \textbf{(S)}.
\end{itemize}
\end{solution}

\begin{problembox}
\textbf{MM.3} \hfill \textbf{[PRSN / CNG-TH]}

Match the thermodynamic and kinetic electrochemical quantities in Column~I with their correct expressions and dimensional relations in Column~II:

\begin{center}
\begin{tabular}{p{0.05\textwidth}p{0.40\textwidth}|p{0.05\textwidth}p{0.42\textwidth}}
\toprule
\multicolumn{2}{c|}{\textbf{Column I (Quantity)}} & \multicolumn{2}{c}{\textbf{Column II (Expression / Identity)}} \\
\midrule
(A) & Reversible cell reaction entropy $\Delta S$ & (P) & $nFT\left(\frac{\partial E}{\partial T}\right)_P - nFE$ \\
(B) & Reaction enthalpy $\Delta H$ & (Q) & $nF \left(\frac{\partial E}{\partial T}\right)_P$ \\
(C) & Heat absorbed reversibly $q_{\text{rev}}$ & (R) & $T \Delta S = nFT \left(\frac{\partial E}{\partial T}\right)_P$ \\
(D) & Maximum thermodynamic efficiency $\eta$ & (S) & $\frac{\Delta G}{\Delta H} = 1 - \frac{T\Delta S}{\Delta H} = \frac{E}{E - T(\partial E/\partial T)_P}$ \\
    & & (T) & $-\frac{\Delta H}{T}$ \\
\bottomrule
\end{tabular}
\end{center}
\end{problembox}
\begin{solution}
\textbf{Match: (A) $\to$ (Q); (B) $\to$ (P); (C) $\to$ (R); (D) $\to$ (S)}

\textbf{Detailed Explanations:}
\begin{itemize}
    \item \textbf{(A) Reaction Entropy $\Delta S$:} From Maxwell's relation $\left(\frac{\partial \Delta G}{\partial T}\right)_P = -\Delta S$, substituting $\Delta G = -nFE$ gives $-\frac{\partial(nFE)}{\partial T} = -nF\left(\frac{\partial E}{\partial T}\right)_P = -\Delta S$, hence $\Delta S = nF\left(\frac{\partial E}{\partial T}\right)_P$. Matches \textbf{(Q)}.
    \item \textbf{(B) Reaction Enthalpy $\Delta H$:} $\Delta H = \Delta G + T\Delta S = -nFE + nFT\left(\frac{\partial E}{\partial T}\right)_P$. Matches \textbf{(P)}.
    \item \textbf{(C) Reversible Heat $q_{\text{rev}}$:} From the Second Law, $q_{\text{rev}} = T\Delta S = nFT\left(\frac{\partial E}{\partial T}\right)_P$. Matches \textbf{(R)}.
    \item \textbf{(D) Thermodynamic Efficiency $\eta$:} $\eta = \frac{W_{\text{elec, max}}}{-\Delta H} = \frac{-\Delta G}{-\Delta H} = \frac{\Delta G}{\Delta H} = \frac{-nFE}{-nFE + nFT(\partial E/\partial T)_P} = \frac{E}{E - T(\partial E/\partial T)_P}$. Matches \textbf{(S)}.
\end{itemize}
\end{solution}

\begin{problembox}
\textbf{MM.4} \hfill \textbf{[GRB / NA Level-2]}

Match the electrolytic system in Column~I with the dominant anodic and cathodic electrode processes in Column~II:

\begin{center}
\begin{tabular}{p{0.05\textwidth}p{0.42\textwidth}|p{0.05\textwidth}p{0.40\textwidth}}
\toprule
\multicolumn{2}{c|}{\textbf{Column I (Electrolysis System)}} & \multicolumn{2}{c}{\textbf{Column II (Products / Reactions)}} \\
\midrule
(A) & Aqueous \ce{NaCl} with inert Pt electrodes & (P) & Cathode: $\ce{Na+(aq) + e^- + Hg -> Na-Hg(amalgam)}$ \\
(B) & Aqueous \ce{NaCl} with liquid mercury cathode & (Q) & Anode: $\ce{2Cl-(aq) -> Cl2(g) + 2e^-}$ \\
(C) & Aqueous \ce{CuSO4} with active Cu electrodes & (R) & Cathode: $\ce{2H2O(l) + 2e^- -> H2(g) + 2OH-(aq)}$ \\
(D) & Concentrated \ce{H2SO4(aq)} at high current density & (S) & Anode: $\ce{Cu(s) -> Cu^2+(aq) + 2e^-}$ (anode dissolution) \\
    & & (T) & Anode: $\ce{2HSO4^-(aq) -> S2O8^2-(aq) + 2H+(aq) + 2e^-}$ \\
\bottomrule
\end{tabular}
\end{center}
\end{problembox}
\begin{solution}
\textbf{Match: (A) $\to$ (Q, R); (B) $\to$ (P, Q); (C) $\to$ (S); (D) $\to$ (T)}

\textbf{Detailed Explanations:}
\begin{itemize}
    \item \textbf{(A) Aqueous \ce{NaCl} with Pt electrodes:} At the cathode, $E^\circ_{\text{red}}(\ce{H2O}) = -0.83\,\text{V} \gg E^\circ_{\text{red}}(\ce{Na+}) = -2.71\,\text{V}$, so $\ce{H2}$ gas evolves (R). At the anode, although $E^\circ(\ce{O2}) = 1.23\,\text{V} < E^\circ(\ce{Cl2}) = 1.36\,\text{V}$, the large overpotential of oxygen on Pt makes chlorine evolution kinetically favored (Q). Matches \textbf{(Q, R)}.
    \item \textbf{(B) Aqueous \ce{NaCl} with Hg cathode (Castner--Kellner cell):} The overpotential for $\ce{H+}$ discharge on liquid mercury is enormous ($\eta \approx 1.5\,\text{V}$). Sodium discharges preferentially into the mercury forming sodium amalgam \ce{Na-Hg} (P), while chlorine evolves at the graphite/Pt anode (Q). Matches \textbf{(P, Q)}.
    \item \textbf{(C) Aqueous \ce{CuSO4} with active Cu electrodes:} Copper refining: Cu cathode gains copper ($\ce{Cu^2+ + 2e^- -> Cu}$), while the Cu anode undergoes active dissolution into $\ce{Cu^2+}$ (S). Matches \textbf{(S)}.
    \item \textbf{(D) Concentrated \ce{H2SO4(aq)} at high current density:} At high acid concentration ($>50\%$) and high current density with Pt anode at low temperature, bisulfate ions dimerize into peroxodisulfuric acid: $\ce{2HSO4^- -> S2O8^2- + 2H+ + 2e^-}$ (Marshall's acid) (T). Matches \textbf{(T)}.
\end{itemize}
\end{solution}

\begin{problembox}
\textbf{MM.5} \hfill \textbf{[CNG-TH / PRSN]}

Match the battery/cell in Column~I with its active chemical constituents and electrolyte in Column~II:

\begin{center}
\begin{tabular}{p{0.05\textwidth}p{0.40\textwidth}|p{0.05\textwidth}p{0.42\textwidth}}
\toprule
\multicolumn{2}{c|}{\textbf{Column I (Cell / Battery)}} & \multicolumn{2}{c}{\textbf{Column II (Active Materials / Electrolyte)}} \\
\midrule
(A) & Leclanch\'{e} Dry Cell & (P) & Anode: \ce{Pb}; Cathode: \ce{PbO2}; Electrolyte: $38\%$ \ce{H2SO4} \\
(B) & Nickel--Cadmium (Nicad) Cell & (Q) & Anode: \ce{Zn}; Cathode: \ce{MnO2} + Carbon; Electrolyte: moist paste of \ce{NH4Cl} and \ce{ZnCl2} \\
(C) & Lead--Acid Accumulator & (R) & Anode: \ce{Cd}; Cathode: \ce{NiO(OH)}; Electrolyte: aqueous \ce{KOH} \\
(D) & Alkaline \ce{H2-O2} Fuel Cell & (S) & Porous carbon electrodes impregnated with Pt/Pd catalyst; Electrolyte: concentrated hot \ce{KOH} \\
    & & (T) & Nominal single-cell operating potential $\approx 1.2\text{--}1.4\,\text{V}$ \\
\bottomrule
\end{tabular}
\end{center}
\end{problembox}
\begin{solution}
\textbf{Match: (A) $\to$ (Q, T); (B) $\to$ (R, T); (C) $\to$ (P); (D) $\to$ (S, T)}

\textbf{Detailed Explanations:}
\begin{itemize}
    \item \textbf{(A) Leclanch\'{e} Dry Cell:} Zinc container acts as anode (Zn), graphite rod surrounded by \ce{MnO2} and carbon black acts as cathode, and paste of \ce{NH4Cl} + \ce{ZnCl2} serves as electrolyte (Q). Operating EMF is $\sim 1.5\,\text{V}$ (T). Matches \textbf{(Q, T)}.
    \item \textbf{(B) Nicad Cell:} Secondary alkaline cell. Anode is cadmium (\ce{Cd}), cathode is nickel(III) oxyhydroxide (\ce{NiO(OH)}), and electrolyte is basic aqueous \ce{KOH} (R). Cell EMF is $\sim 1.4\,\text{V}$ (T). Matches \textbf{(R, T)}.
    \item \textbf{(C) Lead--Acid Accumulator:} Anode is spongy lead, cathode is lead dioxide grid, and electrolyte is aqueous sulfuric acid with density $\sim 1.28\,\text{g\,cm}^{-3}$ (P). Nominal EMF is $\approx 2.05\,\text{V}$ per cell. Matches \textbf{(P)}.
    \item \textbf{(D) \ce{H2-O2} Fuel Cell (Bacon cell):} Uses porous carbon electrodes with finely divided platinum/palladium catalyst, continuously fed with \ce{H2} and \ce{O2} in hot aqueous \ce{KOH} ($200^\circ\text{C}$, $20\text{--}40\,\text{atm}$) (S). Theoretical EMF $E^\circ = 1.229\,\text{V}$ (T). Matches \textbf{(S, T)}.
\end{itemize}
\end{solution}
"""

with open("exercises/matrix_match.tex", "w", encoding="utf-8") as f:
    f.write(matrix_match)
print("Created exercises/matrix_match.tex successfully")
