
# -*- coding: utf-8 -*-
ch06 = r"""\chapter{Electrolysis, Faraday's Laws \& Electrode Kinetics}
\label{chap:electrolysis_faraday}

% ==============================================================================
% SECTION 6.1
% ==============================================================================
\section{Mechanism of Electrolysis}

\textbf{Electrolysis} is the process of using an externally applied electrical current to drive a thermodynamically non-spontaneous chemical reaction at the electrodes of an \textbf{electrolytic cell}. Unlike a galvanic cell (which converts chemical energy spontaneously into electrical energy), an electrolytic cell requires an external DC power supply.

\begin{conceptbox}[Electrolytic vs.\ Galvanic Cell]
\begin{center}
\begin{tabular}{lll}
\toprule
\textbf{Property} & \textbf{Electrolytic Cell} & \textbf{Galvanic Cell}\\
\midrule
Reaction direction & Non-spontaneous ($\Delta G>0$) & Spontaneous ($\Delta G<0$)\\
Energy conversion & Electrical $\to$ Chemical & Chemical $\to$ Electrical\\
External source & Required & Not needed\\
Anode polarity & Positive (+) & Negative ($-$)\\
Cathode polarity & Negative ($-$) & Positive (+)\\
Both electrodes & Oxidation at anode & Oxidation at anode\\
\bottomrule
\end{tabular}
\end{center}
\end{conceptbox}

\subsection{Ion Migration in an Electrolytic Cell}
When DC voltage is applied:
\begin{itemize}
    \item \textbf{Cations} ($\ce{M^{n+}}$) migrate to the \textbf{cathode} (negative) and are \textbf{reduced}.
    \item \textbf{Anions} ($\ce{X^{m-}}$) migrate to the \textbf{anode} (positive) and are \textbf{oxidized}.
\end{itemize}

\subsection{Preferential Discharge Theory}

\begin{conceptbox}[Preferential Discharge Principle]
The ion that requires the \textbf{least energy} to be discharged is preferentially discharged.
\begin{itemize}
    \item \textbf{Cathode} (reduction): cation with the \textbf{highest (most positive) $E^\circ_{\text{red}}$} is discharged first.
    \item \textbf{Anode} (oxidation): anion that is \textbf{easiest to oxidize} (lowest $E^\circ_{\text{red}}$) is discharged first.
\end{itemize}
\end{conceptbox}

\textbf{Preferred order at cathode} (most $\to$ least preferred):
\[
\ce{Ag+ > Hg^2+ > Fe^3+ > Cu^2+ > H+(aq) > Pb^2+ > Sn^2+ > Fe^2+ > Zn^2+ > Al^3+ > Mg^2+ > Na+ > Ca^2+ > K+}
\]

\textbf{Preferred order at anode} (most $\to$ least preferred):
\[
\ce{I- > Br- > Cl- > OH- > NO3- > SO4^2- > F-}
\]

Metals \textit{below} hydrogen in the electrochemical series deposit preferentially over \ce{H2} from aqueous solution (e.g.\ \ce{Cu^2+}, \ce{Ag+}). Metals \textit{above} hydrogen cause \ce{H2} to evolve instead.

\subsection{Overpotential and Overvoltage}
\label{subsec:overpotential}

The voltage actually required to drive continuous electrolysis always exceeds the thermodynamic back-EMF. The excess is called the \textbf{overpotential} ($\eta$):
\begin{equation}
    \boxed{\eta = E_{\text{applied}} - E_{\text{theoretical}}}
\end{equation}

\subsubsection{Causes of Overpotential}
\begin{enumerate}
    \item \textbf{Concentration polarization}: depletion or accumulation of ions at the electrode surface creates a concentration-cell back-EMF.
    \item \textbf{Activation overpotential} (charge-transfer overpotential): energy barrier for the electron-transfer step, described by the \textbf{Butler--Volmer equation}:
    \begin{equation}
        j = j_0 \left[\exp\!\left(\frac{\alpha F\,\eta}{RT}\right) - \exp\!\left(-\frac{(1-\alpha)F\,\eta}{RT}\right)\right]
    \end{equation}
    where $j_0$ = \textbf{exchange current density} (equilibrium reaction rate) and $\alpha$ = \textbf{transfer coefficient} ($\approx 0.5$).
    \item \textbf{Resistance overpotential} (Ohmic drop): $iR$ drop across the electrolyte.
\end{enumerate}

\begin{atkinsbox}[Hydrogen Overpotential on Various Electrode Materials (at $25^\circ\text{C}$, $0.1\,\text{M}\,\ce{H2SO4}$)]
\begin{center}
\begin{tabular}{ll@{\quad\quad}ll}
\toprule
\textbf{Electrode} & $\boldsymbol{\eta_{\ce{H2}}}$ & \textbf{Electrode} & $\boldsymbol{\eta_{\ce{H2}}}$\\
\midrule
Platinized Pt & $\approx 0.00\,\text{V}$ & Mercury (Hg) & $\approx 0.78\,\text{V}$\\
Polished Pt & $\approx 0.09\,\text{V}$ & Lead (Pb) & $\approx 0.52\,\text{V}$\\
Gold (Au) & $\approx 0.02\,\text{V}$ & Zinc (Zn) & $\approx 0.70\,\text{V}$\\
Nickel (Ni) & $\approx 0.21\,\text{V}$ & Iron (Fe) & $\approx 0.40\,\text{V}$\\
Graphite (C) & $\approx 0.60\,\text{V}$ & Tin (Sn) & $\approx 0.75\,\text{V}$\\
\bottomrule
\end{tabular}
\end{center}
\textbf{Key consequences:}
\begin{itemize}
    \item High $\eta_{\ce{H2}}$ on mercury ($\approx 0.78\,\text{V}$) allows deposition of Zn, Cd from \textit{aqueous} solution on Hg cathode, even though thermodynamics favors \ce{H2} evolution.
    \item High oxygen overpotential on graphite ($\approx 0.80\,\text{V}$) causes \ce{Cl2} evolution to be preferred over \ce{O2} in concentrated brine at graphite anodes (chlor-alkali process).
    \item Small $\eta_{\ce{H2}}$ on platinized Pt makes it an excellent reference for $E^\circ = 0.00\,\text{V}$.
\end{itemize}
\end{atkinsbox}

% ==============================================================================
% SECTION 6.2
% ==============================================================================
\section{Faraday's Laws of Electrolysis}

Faraday's laws quantitatively connect the amount of chemical change at electrodes to the quantity of charge (electricity) passed through the cell.

\subsection{Faraday's First Law}

\begin{conceptbox}[Faraday's First Law of Electrolysis]
\textbf{Statement:} The mass of substance deposited or liberated at an electrode is directly proportional to the quantity of charge passed:
\begin{align}
    w &\propto Q \nonumber\\
    \Aboxed{w &= Z \cdot Q = Z \cdot I \cdot t}
\end{align}
\begin{itemize}
    \item $w$ = mass of substance (g)
    \item $Z$ = electrochemical equivalent (g\,C$^{-1}$)
    \item $Q = I \cdot t$ = charge (C); $I$ = current (A); $t$ = time (s)
\end{itemize}
\end{conceptbox}

\subsubsection{Electrochemical Equivalent ($Z$)}

The electrochemical equivalent relates to atomic/molecular properties:
\begin{equation}
    \boxed{Z = \frac{E}{F} = \frac{M}{nF}}
\end{equation}
\begin{itemize}
    \item $E = M/n$ = equivalent weight of the substance
    \item $M$ = molar mass (g\,mol$^{-1}$)
    \item $n$ = number of electrons transferred per formula unit
    \item $F = 96485 \approx 96500\,\text{C\,mol}^{-1}$ = Faraday's constant
\end{itemize}

The complete formula combining all parameters:
\begin{equation}
    \boxed{w = \frac{M \cdot I \cdot t}{n\,F}} \qquad \text{or equivalently} \qquad \boxed{n_{\text{mol}} = \frac{I \cdot t}{n\,F}}
\end{equation}

\subsection{Faraday's Second Law}

\begin{conceptbox}[Faraday's Second Law of Electrolysis]
\textbf{Statement:} When the same quantity of electricity passes through different electrolytes connected in series, the masses of different substances deposited or liberated at the respective electrodes are proportional to their equivalent weights:
\begin{equation}
    \boxed{\frac{w_1}{w_2} = \frac{E_1}{E_2} = \frac{M_1/n_1}{M_2/n_2}}
\end{equation}
\textbf{Corollary:} All cells in series receive the same charge $Q$, hence the same number of moles of equivalents $= Q/F$.
\end{conceptbox}

\subsection{Faraday's Constant}

\begin{equation}
    \boxed{F = N_A \cdot e = (6.022\times10^{23}\,\text{mol}^{-1})(1.602\times10^{-19}\,\text{C}) = 96485\,\text{C\,mol}^{-1} \approx 96500\,\text{C\,mol}^{-1}}
\end{equation}

One Faraday ($96485\,\text{C}$) deposits exactly one gram-equivalent of any substance:
\begin{center}
\begin{tabular}{lll}
\toprule
\textbf{Substance} & \textbf{Reaction} & \textbf{Deposited per Faraday}\\
\midrule
Silver (Ag) & \ce{Ag+ + e- -> Ag} & $108/1 = 108\,\text{g}$\\
Copper (Cu) & \ce{Cu^2+ + 2e- -> Cu} & $63.5/2 = 31.75\,\text{g}$\\
Aluminum (Al) & \ce{Al^3+ + 3e- -> Al} & $27/3 = 9\,\text{g}$\\
Hydrogen (H) & \ce{2H+ + 2e- -> H2} & $1\,\text{g} = 11.2\,\text{L at STP}$\\
Oxygen (O) & \ce{O2 + 4H+ + 4e- -> 2H2O} & $8\,\text{g O} = 5.6\,\text{L at STP}$\\
\bottomrule
\end{tabular}
\end{center}

\begin{examplebox}[Three-Cell Series Circuit: Ag, Cu, and \ce{H2}]
\textbf{Problem:} A steady current of $2\,\text{A}$ flows for $3\,\text{hours}$ through three series-connected cells: (i) \ce{AgNO3}(aq)/Pt, (ii) \ce{CuSO4}(aq)/Pt, (iii) acidified water/Pt. Calculate the mass of Ag and Cu deposited and the volume of \ce{H2} evolved. [$M_{\ce{Ag}}=108$; $M_{\ce{Cu}}=63.5$; $n_{\ce{Ag}}=1$; $n_{\ce{Cu}}=2$; $n_{\ce{H2}}=2$]

\textbf{Solution:}
\begin{align*}
Q &= I \times t = 2\,\text{A} \times (3 \times 3600\,\text{s}) = 21600\,\text{C}\\[4pt]
\text{Equivalents passed} &= \frac{Q}{F} = \frac{21600}{96500} = 0.2238\,\text{eq}
\end{align*}
\begin{enumerate}
    \item \textbf{Ag} ($n=1$, $E_{\ce{Ag}}=108$):
    $w_{\ce{Ag}} = 0.2238 \times 108 = \mathbf{24.17\,\text{g}}$
    \item \textbf{Cu} ($n=2$, $E_{\ce{Cu}}=31.75$):
    $w_{\ce{Cu}} = 0.2238 \times 31.75 = \mathbf{7.11\,\text{g}}$
    \item \textbf{\ce{H2}} ($n=2$, $E_{\ce{H}}=1$, moles of \ce{H2} $= 0.2238/2 = 0.1119\,\text{mol}$):
    $V_{\ce{H2}} = 0.1119 \times 22.4 = \mathbf{2.51\,\text{L at STP}}$
\end{enumerate}
\end{examplebox}

% ==============================================================================
% SECTION 6.3
% ==============================================================================
\section{Current Efficiency}

Side reactions (parallel electrode processes, e.g.\ \ce{H2} evolution alongside metal deposition) consume charge without forming the desired product. The \textbf{current efficiency} quantifies productive utilization of charge:

\begin{conceptbox}[Current Efficiency]
\begin{equation}
    \boxed{\eta_{\text{curr}} = \frac{w_{\text{actual}}}{w_{\text{theoretical}}} \times 100\%}
\end{equation}
where $w_{\text{theoretical}}$ is calculated from Faraday's first law assuming 100\% selectivity.
\end{conceptbox}

\begin{examplebox}[Current Efficiency in Copper Electroplating]
\textbf{Problem:} A $5\,\text{A}$ current for $1\,\text{h}$ deposits only $5.63\,\text{g}$ Cu.
[$M_{\ce{Cu}} = 63.5$, $n=2$]

\textbf{Solution:}
\begin{align*}
w_{\text{theor}} &= \frac{M\cdot I\cdot t}{n\cdot F} = \frac{63.5 \times 5 \times 3600}{2 \times 96500} = 5.932\,\text{g}\\
\eta_{\text{curr}} &= \frac{5.63}{5.932}\times 100\% = \mathbf{94.9\%}
\end{align*}
The remaining $5.1\%$ was consumed by \ce{H2} evolution at the cathode.
\end{examplebox}

% ==============================================================================
% SECTION 6.4
% ==============================================================================
\section{Quantitative Electrolysis of Important Systems}

Products depend on: (1) electrolyte type (molten vs.\ aqueous), (2) concentration, (3) electrode material, (4) current density and overpotential.

\subsection{Electrolysis of Molten Salts}

\begin{examplebox}[Molten \ce{NaCl} --- Downs Cell]
\begin{align*}
\text{Cathode:}& \quad \ce{Na+(l) + e- -> Na(l)}\\
\text{Anode:}& \quad \ce{2Cl-(l) -> Cl2(g) + 2e-}\\
\text{Net:}& \quad \ce{2NaCl(l) -> 2Na(l) + Cl2(g)}
\end{align*}
\ce{CaCl2} is added to lower the melting point from $801^\circ\text{C}$ to $\approx580^\circ\text{C}$. A circular iron cathode with a surrounding graphite anode ensures separation of products.
\end{examplebox}

\subsection{Aqueous Electrolysis: Systematic Analysis}

\subsubsection{Dilute \ce{H2SO4} or Acidified Water (Inert Pt Electrodes)}
\begin{align*}
\text{Cathode:}& \quad \ce{2H+(aq) + 2e- -> H2(g)}\\
\text{Anode:}& \quad \ce{2H2O(l) -> O2(g) + 4H+(aq) + 4e-}\\
\text{Net:}& \quad \ce{2H2O(l) -> 2H2(g) + O2(g)}
\end{align*}
Molar ratio $\ce{H2}:\ce{O2} = 2:1$ (by moles = by volume at same $T$, $P$).

\subsubsection{Dilute \ce{NaCl}(aq) --- Pt Electrodes}
Low [\ce{Cl-}]: oxygen overpotential on Pt is not large enough to divert to \ce{Cl2}.
\begin{itemize}
    \item Cathode: \ce{H2(g)} evolved ($\ce{H+}$ or $\ce{H2O}$ reduced)
    \item Anode: \ce{O2(g)} evolved ($\ce{OH-}$/$\ce{H2O}$ oxidized, not \ce{Cl-})
\end{itemize}

\subsubsection{Concentrated \ce{NaCl} Brine (Chlor-Alkali Process --- Graphite or MMO Anode)}
High [\ce{Cl-}] + high $\eta_{\ce{O2}}$ on graphite: \ce{Cl2} preferred at anode.
\begin{align*}
\text{Cathode:}& \quad \ce{2H2O(l) + 2e- -> H2(g) + 2OH-(aq)}\\
\text{Anode:}& \quad \ce{2Cl-(aq) -> Cl2(g) + 2e-}\\
\text{Net:}& \quad \ce{2NaCl(aq) + 2H2O(l) -> Cl2(g) + H2(g) + 2NaOH(aq)}
\end{align*}
Three valuable industrial chemicals produced simultaneously. This is the Castner--Kellner cell (Hg cathode variant) or membrane cell (modern variant).

\subsubsection{\ce{CuSO4}(aq) with Inert Pt Electrodes}
\begin{itemize}
    \item Cathode: \ce{Cu^2+ + 2e- -> Cu(s)} ($E^\circ = +0.34\,\text{V}$, strongly preferred over \ce{H+})
    \item Anode: \ce{2H2O -> O2(g) + 4H+ + 4e-} (\ce{SO4^2-} not oxidized on Pt)
    \item Effect: $[\ce{Cu^2+}]$ decreases; $[\ce{H2SO4}]$ increases; solution acidifies.
\end{itemize}

\subsubsection{\ce{CuSO4}(aq) with Active Copper Anode (Electrorefining)}
\begin{itemize}
    \item Cathode: \ce{Cu^2+ + 2e- -> Cu(s)} --- pure Cu deposited
    \item Anode: \ce{Cu(s) -> Cu^2+(aq) + 2e-} --- impure Cu dissolves
    \item $[\ce{CuSO4}]$ remains constant; precious metal impurities (Ag, Au) fall as \textbf{anode mud}
\end{itemize}

\subsubsection{\ce{AgNO3}(aq)}
\begin{itemize}
    \item Inert Pt cathode: \ce{Ag+(aq) + e- -> Ag(s)} (basis of silver plating)
    \item Inert Pt anode: \ce{2H2O -> O2 + 4H+ + 4e-} (\ce{NO3-} not discharged; solution acidifies)
    \item Active Ag anode: \ce{Ag(s) -> Ag+(aq) + e-} (electrolyte maintained)
\end{itemize}

\subsubsection{\ce{NaOH}(aq) --- Pt Electrodes}
Cathode: \ce{H2(g)}. Anode: \ce{O2(g)}. Net: water electrolyzed; [\ce{NaOH}] increases.

\subsubsection{\ce{K2SO4}(aq) --- Pt Electrodes}
Cathode: \ce{H2(g)}. Anode: \ce{O2(g)}. Net: equivalent to dilute \ce{H2SO4}.

\subsection{Kolbe's Electrolytic Synthesis}

Oxidative decarboxylation of carboxylate anions at a smooth Pt anode forms alkyl radicals, which couple:
\begin{equation}
    \ce{2RCOO^-(aq) ->[\text{Pt anode}] R-R(g) + 2CO2(g) + 2e-}
\end{equation}

\begin{examplebox}[Kolbe Cross-Coupling Products]
Electrolysis of a mixture of \ce{CH3COONa} and \ce{C2H5COONa} yields \textbf{three alkanes}:
\begin{align*}
\ce{2CH3COO^-} &\to \ce{CH3CH3(g) + 2CO2 + 2e-} & (\text{ethane})\\
\ce{2C2H5COO^-} &\to \ce{C2H5C2H5(g) + 2CO2 + 2e-} & (\text{butane})\\
\ce{CH3COO^- + C2H5COO^-} &\to \ce{CH3C2H5(g) + 2CO2 + 2e-} & (\text{propane, cross-coupling})
\end{align*}
General rule: $n$ different carboxylate anions produce $\binom{n+1}{2}$ different alkanes.
\end{examplebox}

% ==============================================================================
% SECTION 6.5
% ==============================================================================
\section{Decomposition Potential and Back-EMF}

The \textbf{decomposition potential} (decomposition voltage) is the minimum applied voltage to sustain continuous electrolysis at an observable rate:
\begin{equation}
    \boxed{E_{\text{decomp}} = E_{\text{back-EMF}} + |\eta_{\text{cathode}}| + |\eta_{\text{anode}}| + iR}
\end{equation}
$E_{\text{back-EMF}} = E^\circ_{\text{cell (galvanic)}}$ = EMF of the cell that the products would form spontaneously.

\begin{examplebox}[Decomposition Potential of Dilute \ce{H2SO4}]
\begin{align*}
E^\circ(\ce{H+/H2}) &= 0.00\,\text{V} \qquad E^\circ(\ce{O2/H2O}) = +1.23\,\text{V}\\
E_{\text{back}} &= 1.23 - 0.00 = 1.23\,\text{V (theoretical)}
\end{align*}
With $\eta_{\ce{H2}}$ and $\eta_{\ce{O2}}$ on polished Pt electrodes, experimentally $E_{\text{decomp}} \approx 1.67\,\text{V}$.
\end{examplebox}

% ==============================================================================
% SECTION 6.6
% ==============================================================================
\section{Important Industrial Electrolytic Processes}

\subsection{Electrolytic Refining of Metals}

\begin{itemize}
    \item \textbf{Setup:} Impure metal = anode; pure metal sheet = cathode; aqueous salt of same metal = electrolyte.
    \item \textbf{Process:} Impure anode dissolves; pure metal deposits on cathode. Impurities less noble than the metal pass into solution; noble metal impurities (Ag, Au, Pt) fall as \textbf{anode mud} and are economically valuable.
    \item \textbf{Applied to:} Cu, Ag, Au, Pb, Sn, Ni, Zn.
\end{itemize}

\subsection{Electroplating}

The object to be plated forms the cathode; the plating metal (or an inert anode) forms the anode; electrolyte = salt of the plating metal.

\begin{center}
\begin{tabular}{llll}
\toprule
\textbf{Plating} & \textbf{Electrolyte} & \textbf{Anode} & \textbf{Purpose}\\
\midrule
Nickel & \ce{NiSO4}(aq) & Ni metal & Corrosion resistance\\
Chromium & Acidic \ce{CrO3} & Inert Pb & Hardness, shine\\
Silver & \ce{AgCN} complex & Ag metal & Cutlery, jewelry\\
Gold & \ce{[Au(CN)2]^-} & Au metal & Electronics, jewelry\\
Zinc (galvanizing) & \ce{ZnSO4}(aq) & Zn metal & Rust prevention on steel\\
Copper & \ce{CuSO4} + \ce{H2SO4} & Cu metal & PCB circuits\\
\bottomrule
\end{tabular}
\end{center}

\subsection{Hall--H\'{e}roult Process (Aluminium Production)}

Purified \ce{Al2O3} (alumina) is dissolved in molten cryolite (\ce{Na3AlF6}) at $\approx 950^\circ\text{C}$ to reduce the melting point and improve conductivity:
\begin{align*}
\text{Cathode (molten Al pool):}& \quad \ce{Al^3+ + 3e- -> Al(l)}\\
\text{Anode (graphite, consumed):}& \quad \ce{C(s) + 2O^2-(l) -> CO2(g) + 4e-}
\end{align*}
Graphite anodes are progressively consumed and require periodic replacement.

\subsection{Downs Cell (Sodium and Chlorine Production)}

Electrolysis of molten \ce{NaCl}/\ce{CaCl2} mixture at $\approx580^\circ\text{C}$:
\begin{align*}
\text{Cathode:}& \quad \ce{Na+(l) + e- -> Na(l)}\\
\text{Anode:}& \quad \ce{2Cl-(l) -> Cl2(g) + 2e-}
\end{align*}

\section{Summary Table: Electrode Products for Common Electrolytic Systems}

\begin{center}
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{p{4.5cm}p{2.8cm}p{3.2cm}p{3cm}}
\toprule
\textbf{Electrolyte} & \textbf{Electrode} & \textbf{Cathode Product} & \textbf{Anode Product}\\
\midrule
Molten \ce{NaCl} & Pt & Na metal & \ce{Cl2} gas\\
Dilute \ce{H2SO4}(aq) & Pt & \ce{H2} gas & \ce{O2} gas\\
Dilute \ce{NaCl}(aq) & Pt & \ce{H2} gas & \ce{O2} gas\\
Conc.\ \ce{NaCl}(aq) & Graphite & \ce{H2}~gas + \ce{NaOH} & \ce{Cl2} gas\\
\ce{CuSO4}(aq) & Pt (inert) & Cu metal & \ce{O2} gas\\
\ce{CuSO4}(aq) & Cu (active) & Cu metal & Cu dissolves\\
\ce{AgNO3}(aq) & Pt (inert) & Ag metal & \ce{O2} gas\\
\ce{AgNO3}(aq) & Ag (active) & Ag metal & Ag dissolves\\
Molten \ce{Al2O3}/cryolite & Graphite & Al metal & \ce{CO2} gas\\
\ce{NiSO4}(aq) & Ni (active) & Ni metal & Ni dissolves\\
\ce{NaOH}(aq) & Pt & \ce{H2} gas & \ce{O2} gas\\
\ce{K2SO4}(aq) & Pt & \ce{H2} gas & \ce{O2} gas\\
Molten \ce{Al2O3} alone & C & Al(l) & \ce{O2}/\ce{CO2}\\
\ce{ZnSO4}(aq) & Hg (cathode) & Zn metal (due to high $\eta_{\ce{H2}}$) & \ce{O2} gas\\
\bottomrule
\end{tabular}
\end{center}
"""

with open(r"chapters/ch06_electrolysis_faraday.tex", "w", encoding="utf-8") as f:
    f.write(ch06)
print("ch06 written:", len(ch06), "chars")
