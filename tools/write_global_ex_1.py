
# -*- coding: utf-8 -*-
"""Write all 8 global exercise category files to the exercises/ directory."""
import os

os.makedirs("exercises", exist_ok=True)

# ============================================================
# 1. SUBJECTIVE.TEX
# ============================================================
subjective = r"""\chapter*{Global Exercise Bank --- Subjective Problems}
\addcontentsline{toc}{chapter}{Global Exercise Bank: Subjective Problems}
\label{chap:subjective}

\begin{tcolorbox}[enhanced,colback=subtleblue,colframe=primarynavy,arc=2mm,boxrule=1pt,
    title=\textbf{\large Subjective / Descriptive Problems (All Chapters)}]
Deep derivations, multi-step quantitative problems and open-ended questions.
Sources: \textbf{[ATK]}, \textbf{[NRJ]} Ex-II Subjective, \textbf{[PRSN]} Ex-II.
\end{tcolorbox}

\section*{S-1. Conductance and Transport}

\begin{problembox}
\textbf{S.1} \hfill \textbf{[ATK Topic 6D / NRJ Subjective Q3]}

Derive the Debye--H\"{u}ckel--Onsager (DHO) equation $\Lambda_m = \Lambda_m^\circ - b\sqrt{C}$, identifying the physical origin of the two contributions to the slope $b$. State all assumptions made in the derivation and their range of validity.
\end{problembox}
\begin{solution}
The DHO equation arises because at finite concentration, a central ion experiences two retarding effects on its migration:

\textbf{1. Relaxation (Asymmetry) Effect:} Each central ion is surrounded by an ionic atmosphere of opposite charge. In the absence of an applied field, this atmosphere is perfectly spherical. When a field is applied and the central ion migrates, the atmosphere cannot instantly rearrange --- it lags behind. The net effect is a backward electrical force on the migrating ion, reducing its velocity.

The contribution to the slope: $b_1 = \frac{z^3 e^3 \kappa}{6\pi\varepsilon_0\varepsilon_r k_B T}$ (where $\kappa \propto \sqrt{c}$ is the Debye screening parameter).

\textbf{2. Electrophoretic Effect:} The ionic atmosphere itself also migrates in the applied field --- in the \textit{opposite} direction to the central ion. The central ion must move through this countercurrent of solvent/ions, increasing the effective viscous drag.

Contribution: $b_2 \propto \sqrt{c}$ via the electrophoretic velocity $v_{\text{eph}} = \frac{ze\kappa}{6\pi\eta}$.

\textbf{Combined:}
\begin{equation*}
    \Lambda_m = \Lambda_m^\circ - (A\Lambda_m^\circ + B)\sqrt{c}
\end{equation*}
where $A$ captures the relaxation effect and $B$ captures the electrophoretic effect, both $\propto \sqrt{c}$.

\textbf{Assumptions:}
\begin{itemize}
    \item Point charges (ions have no excluded volume)
    \item Dilute solution ($I < 0.01\,\text{mol\,L}^{-1}$)
    \item Linear response: applied field $\ll$ thermal forces
    \item Primitive model (solvent = dielectric continuum)
\end{itemize}
\end{solution}

\begin{problembox}
\textbf{S.2} \hfill \textbf{[NRJ Ex-II Subjective Q5 / PRSN Ex-II Q14]}

A conductometric titration is performed: $25\,\text{mL}$ of $0.1\,\text{M}$ acetic acid (\ce{CH3COOH}) is titrated with $0.1\,\text{M}$ \ce{NaOH}. Sketch the conductance-vs-volume curve, indicate the equivalence point, and explain the trend in each region. Which ionic species cause the conductance to change in each region?
\end{problembox}
\begin{solution}
\textbf{Regions of the conductometric titration (weak acid vs.\ strong base):}

\textbf{Region 1 (Before equivalence point):} Adding \ce{NaOH} to \ce{CH3COOH}:
\begin{equation*}
    \ce{CH3COOH + NaOH -> CH3COONa + H2O}
\end{equation*}
\ce{CH3COOH} (weak, poorly conducting) is replaced by \ce{CH3COO-Na+} (strong electrolyte, well-conducting). Conductance \textbf{increases gradually} (not steeply, because \ce{CH3COONa} is a moderate conductor and the buffer formed partially suppresses further dissociation).

\textbf{At the equivalence point (25~mL added):} All acetic acid is converted to sodium acetate. Conductance is at a local minimum before the steep rise.

\textbf{Region 2 (After equivalence point):} Excess \ce{NaOH} is added. \ce{Na+} and \ce{OH-} accumulate. \ce{OH-} has extremely high molar ionic conductivity ($\lambda^\circ_{\ce{OH-}} = 198\,\text{S\,cm}^2\,\text{mol}^{-1}$), so conductance \textbf{rises steeply}.

The \textbf{V-shape with a gentle initial rise and steep post-equivalence rise} is the characteristic curve.
\end{solution}

\section*{S-2. Cell Thermodynamics}

\begin{problembox}
\textbf{S.3} \hfill \textbf{[ATK Topic 6C.4 / NRJ Subjective Q8]}

For the cell $\ce{Pt | H2(g, 1 bar) | HCl(aq) | AgCl(s) | Ag(s)}$, the EMF varies with temperature as $E = 0.2224 - 6.4\times10^{-4}(T-298)\,\text{V}$. At $298\,\text{K}$: calculate (a) $\Delta G$, (b) $\Delta S$, (c) $\Delta H$, (d) $q_{rev}$ (heat reversibly exchanged with surroundings). [$F = 96500$, $n=1$]
\end{problembox}
\begin{solution}
At $T = 298\,\text{K}$, $E = 0.2224\,\text{V}$ and $\left(\frac{\partial E}{\partial T}\right)_P = -6.4\times10^{-4}\,\text{V\,K}^{-1}$.

(a) $\Delta G = -nFE = -1\times96500\times0.2224 = \mathbf{-21462\,\text{J\,mol}^{-1} = -21.46\,\text{kJ\,mol}^{-1}}$

(b) $\Delta S = nF\left(\frac{\partial E}{\partial T}\right)_P = 1\times96500\times(-6.4\times10^{-4}) = \mathbf{-61.76\,\text{J\,mol}^{-1}\text{K}^{-1}}$

(c) $\Delta H = \Delta G + T\Delta S = -21462 + 298\times(-61.76) = -21462 - 18404 = \mathbf{-39866\,\text{J\,mol}^{-1} = -39.87\,\text{kJ\,mol}^{-1}}$

(d) $q_{rev} = T\Delta S = 298\times(-61.76) = \mathbf{-18404\,\text{J\,mol}^{-1} = -18.4\,\text{kJ\,mol}^{-1}}$

The negative $q_{rev}$ means the cell \textit{releases} heat to the surroundings when operating reversibly at $298\,\text{K}$ --- consistent with $\Delta S < 0$ (entropy decreases).
\end{solution}

\begin{problembox}
\textbf{S.4} \hfill \textbf{[NRJ Subjective Q10 / PRSN Advanced]}

A concentration cell (without transference) is constructed:
\[\ce{Ag(s) | AgNO3(c_1) || AgNO3(c_2) | Ag(s)}, \quad c_1 = 0.01\,\text{M},\; c_2 = 0.1\,\text{M}\]
(a) Write the cell reaction and identify which side is the anode.
(b) Calculate $E_{\text{cell}}$ at $298\,\text{K}$.
(c) Show that the cell will spontaneously drive silver from the dilute side to the concentrated side.
\end{problembox}
\begin{solution}
(a) Anode (oxidation): $\ce{Ag(s) -> Ag+(c_1) + e-}$ (dilute side, lower $E$).\\
Cathode (reduction): $\ce{Ag+(c_2) + e- -> Ag(s)}$ (concentrated side, higher $E$).\\
Net: $\ce{Ag+(c_2) -> Ag+(c_1)}$ (transfer of silver ions from concentrated to dilute).

(b) $E = -\frac{RT}{F}\ln\frac{c_1}{c_2} = -\frac{0.0591}{1}\log\frac{0.01}{0.1} = -0.0591\times(-1) = \mathbf{+0.0591\,\text{V}}$

(c) Since $E > 0$, $\Delta G = -nFE < 0$: the process is spontaneous. Ag is oxidized at the dilute anode and deposited at the concentrated cathode --- net, Ag is ``transferred'' from the low-concentration side to the high-concentration side (ions in solution). The system drives towards concentration equilibration.
\end{solution}

\section*{S-3. Faraday's Laws and Industrial Electrolysis}

\begin{problembox}
\textbf{S.5} \hfill \textbf{[NRJ Subjective Q14 / PRSN Ex-II Q20]}

In the Hall--H\'{e}roult process, a cell operates at $5\,\text{V}$ and $100\,\text{kA}$ to produce aluminium. (a) Calculate the mass of Al produced per hour. (b) Calculate the electrical energy consumed per kg of Al. (c) If electricity costs \$0.05/kWh, what is the electricity cost per tonne of Al? [$M_{\ce{Al}} = 27$, $n=3$, $F = 96500$]
\end{problembox}
\begin{solution}
(a) $Q = 100000\,\text{A} \times 3600\,\text{s} = 3.6\times10^8\,\text{C}$\\
$m = \frac{M\cdot Q}{n\cdot F} = \frac{27\times3.6\times10^8}{3\times96500} = \frac{9.72\times10^9}{289500} = \mathbf{33574\,\text{g} \approx 33.6\,\text{kg\,h}^{-1}}$

(b) Power $= V\times I = 5\times100000 = 500\,\text{kW}$.\\
Energy per hour $= 500\,\text{kWh}$.\\
Energy per kg $= 500/33.6 = \mathbf{14.9\,\text{kWh\,kg}^{-1}}$.

(c) Energy per tonne $= 14.9\times1000 = 14900\,\text{kWh}$.\\
Cost per tonne $= 14900\times0.05 = \$\mathbf{745}$ per tonne of Al.
\end{solution}
"""

with open("exercises/subjective.tex", "w", encoding="utf-8") as f:
    f.write(subjective)
print("subjective.tex:", len(subjective), "chars")

# ============================================================
# 2. SINGLE_CORRECT.TEX
# ============================================================
single_correct = r"""\chapter*{Global Exercise Bank --- Single Correct MCQs}
\addcontentsline{toc}{chapter}{Global Exercise Bank: Single Correct MCQs}
\label{chap:single_correct}

\begin{tcolorbox}[enhanced,colback=subtlegreen,colframe=cengagegreen,arc=2mm,boxrule=1pt,
    title=\textbf{\large Single Correct Option MCQs (All Chapters)}]
Sources: \textbf{[CNG-TH]} Concept App., \textbf{[GRB]} Ex-I, \textbf{[NA]} Level-1, \textbf{[ESS]}, \textbf{[CNG-DPP]}.
\end{tcolorbox}

\begin{problembox}
\textbf{SC.1} \hfill \textbf{[GRB Ex-I / ESS Q]}

The unit of molar conductance ($\Lambda_m$) is:
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $\Omega^{-1}$
    \item $\text{S\,cm}^2\,\text{mol}^{-1}$
    \item $\text{S\,cm}^{-1}$
    \item $\Omega\,\text{cm}^2\,\text{mol}^{-1}$
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(b)} $\text{S\,cm}^2\,\text{mol}^{-1}$ (also written $\Omega^{-1}\,\text{cm}^2\,\text{mol}^{-1}$ or $\text{S\,m}^2\,\text{mol}^{-1}$ in SI). $\Lambda_m = \kappa/c$ where $\kappa$ (S\,cm$^{-1}$), $c$ (mol\,cm$^{-3}$).
\end{solution}

\begin{problembox}
\textbf{SC.2} \hfill \textbf{[CNG-TH Concept App. / GRB]}

For a weak electrolyte at infinite dilution, which of Kohlrausch's law gives $\Lambda_m^\circ$?
\begin{enumerate}[label=(\alph*)]
    \item By extrapolating the Kohlrausch plot ($\Lambda_m$ vs $\sqrt{c}$) to $c=0$
    \item By adding $\lambda^\circ$ of constituent ions algebraically
    \item Both (a) and (b)
    \item (a) only for strong electrolytes; (b) only for weak electrolytes
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{(d)} For strong electrolytes, the $\Lambda_m$ vs $\sqrt{c}$ plot is linear and can be extrapolated to $c\to0$ (method a). For weak electrolytes (like acetic acid), the plot shows a sharp, non-linear upswing at low concentrations and cannot be extrapolated reliably; instead, Kohlrausch's law of independent migration (method b) must be used to calculate $\Lambda_m^\circ$ indirectly from strong electrolyte data.
\end{solution}

\begin{problembox}
\textbf{SC.3} \hfill \textbf{[NA Level-1 Q6]}

The molar conductance of $0.1\,\text{M}$ \ce{CH3COOH} is $5.2\,\text{S\,cm}^2\,\text{mol}^{-1}$ and $\Lambda_m^\circ(\ce{CH3COOH}) = 390.7\,\text{S\,cm}^2\,\text{mol}^{-1}$. The degree of dissociation $\alpha$ is:
\begin{multicols}{4}
\begin{enumerate}[label=(\alph*)]
    \item $0.0133$
    \item $0.133$
    \item $0.75$
    \item $0.33$
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(a)} $\alpha = \Lambda_m/\Lambda_m^\circ = 5.2/390.7 = 0.0133$
\end{solution}

\begin{problembox}
\textbf{SC.4} \hfill \textbf{[GRB Ex-I / CNG-TH]}

In the standard hydrogen electrode (SHE), the standard conditions are:
\begin{enumerate}[label=(\alph*)]
    \item $[\ce{H+}] = 1\,\text{mol\,L}^{-1}$, $P_{\ce{H2}} = 1\,\text{atm}$, $T = 298\,\text{K}$
    \item $[\ce{H+}] = 1\,\text{mol\,L}^{-1}$, $P_{\ce{H2}} = 1\,\text{bar}$, $T = 298\,\text{K}$
    \item $a_{\ce{H+}} = 1$, $f_{\ce{H2}} = 1\,\text{bar}$, $T = 298\,\text{K}$
    \item $[\ce{H+}] = 7\,\text{M}$, $P_{\ce{H2}} = 1\,\text{bar}$, $T = 298\,\text{K}$
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{(c)} The strictly correct thermodynamic definition uses \textit{activities}: $a_{\ce{H+}} = 1$ (unit activity of H$^+$) and $f_{\ce{H2}} = 1\,\text{bar}$ (unit fugacity of H$_2$). In practice, $1\,\text{mol\,L}^{-1}$ \ce{HCl} approximates unit activity, but for a rigorous JEE/Olympiad answer, (c) is most correct.
\end{solution}

\begin{problembox}
\textbf{SC.5} \hfill \textbf{[CNG-DPP DPP-2 / GRB Q]}

Which of the following couples has the \textbf{highest} tendency to act as a reducing agent?
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $\ce{Li+/Li}$ ($E^\circ = -3.05\,\text{V}$)
    \item $\ce{Zn^2+/Zn}$ ($E^\circ = -0.76\,\text{V}$)
    \item $\ce{Cu^2+/Cu}$ ($E^\circ = +0.34\,\text{V}$)
    \item $\ce{Ag+/Ag}$ ($E^\circ = +0.80\,\text{V}$)
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(a)} The most negative $E^\circ$ means the metal is most easily oxidized (strongest reducing agent). Li$^+$/Li has $E^\circ = -3.05\,\text{V}$: Li is the strongest reducing agent in the electrochemical series.
\end{solution}

\begin{problembox}
\textbf{SC.6} \hfill \textbf{[ESS §24 / GRB Q]}

The transference number of $\ce{K+}$ in \ce{KCl} at infinite dilution is approximately $0.49$. This means:
\begin{enumerate}[label=(\alph*)]
    \item $49\%$ of the current is carried by \ce{K+} ions
    \item $49\%$ of the ions are \ce{K+}
    \item \ce{K+} moves $49\%$ faster than \ce{Cl-}
    \item $49\%$ of \ce{KCl} is dissociated
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{(a)} The transference number $t_+ = 0.49$ means $49\%$ of the electric current is transported by \ce{K+} ions; the remaining $51\%$ is transported by \ce{Cl-} ions ($t_- = 0.51$). Since $t_+ \approx t_-$, both ions have nearly equal mobilities --- hence KCl (and KNO$_3$, NH$_4$NO$_3$) are used in salt bridges.
\end{solution}

\begin{problembox}
\textbf{SC.7} \hfill \textbf{[NA Level-1 Q12 / GRB]}

The $\text{EMF}$ of the cell $\ce{Zn | ZnSO4(0.01 M) || CuSO4(1 M) | Cu}$ at $298\,\text{K}$ is: [$E^\circ(\ce{Cu^2+/Cu})=+0.34\,\text{V}$, $E^\circ(\ce{Zn^2+/Zn})=-0.76\,\text{V}$]
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $1.10\,\text{V}$
    \item $1.16\,\text{V}$
    \item $1.04\,\text{V}$
    \item $0.98\,\text{V}$
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(b)}\\
$E^\circ_{\text{cell}} = 0.34 - (-0.76) = 1.10\,\text{V}$\\
Nernst ($n=2$): $E = 1.10 - \frac{0.0591}{2}\log\frac{0.01}{1} = 1.10 - \frac{0.0591}{2}\times(-2) = 1.10 + 0.0591 = \mathbf{1.16\,\text{V}}$
\end{solution}

\begin{problembox}
\textbf{SC.8} \hfill \textbf{[CNG-TH Concept App / NA Q14]}

Given $K_{sp}(\ce{AgCl}) = 1.8\times10^{-10}$ at $298\,\text{K}$ and $E^\circ(\ce{Ag+/Ag}) = +0.80\,\text{V}$, the standard reduction potential of the $\ce{Ag | AgCl(s) | Cl-}$ electrode is:
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $+0.22\,\text{V}$
    \item $+0.50\,\text{V}$
    \item $-0.22\,\text{V}$
    \item $+0.80\,\text{V}$
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(a)}\\
$E^\circ(\ce{AgCl/Ag}) = E^\circ(\ce{Ag+/Ag}) + 0.0591\log K_{sp}$\\
$= 0.80 + 0.0591\log(1.8\times10^{-10}) = 0.80 + 0.0591\times(-9.745) = 0.80 - 0.576 = \mathbf{+0.224\,\text{V} \approx +0.22\,\text{V}}$
\end{solution}

\begin{problembox}
\textbf{SC.9} \hfill \textbf{[GRB / CNG-DPP DPP-3]}

In a Daniell cell, the salt bridge contains saturated \ce{KCl}. Its primary function is to:
\begin{enumerate}[label=(\alph*)]
    \item Provide \ce{K+} and \ce{Cl-} as reactants in the cell reaction
    \item Prevent mixing of the two electrolytes
    \item Maintain electrical neutrality in both half-cells and eliminate liquid junction potential
    \item Increase the cell potential by providing a third electrolyte
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{(c)} The salt bridge serves two roles: (i) maintains electrical neutrality by allowing ion migration (\ce{K+} into the cathode solution, \ce{Cl-} into the anode solution, as ions are consumed/produced), and (ii) minimizes the liquid junction potential because $t_+ \approx t_-$ for \ce{KCl} (both ions have nearly equal transference numbers), so the junction potential nearly cancels.
\end{solution}

\begin{problembox}
\textbf{SC.10} \hfill \textbf{[NA Level-1 Q20]}

The equilibrium constant for the cell reaction of the Daniel cell (\ce{Zn | Zn^2+ || Cu^2+ | Cu}) at $298\,\text{K}$ is: [$E^\circ_{\text{cell}} = 1.10\,\text{V}$, $n=2$]
\begin{multicols}{2}
\begin{enumerate}[label=(\alph*)]
    \item $10^{37.2}$
    \item $10^{3.72}$
    \item $e^{85.6}$
    \item $10^{18.6}$
\end{enumerate}
\end{multicols}
\end{problembox}
\begin{solution}
\textbf{(a)}\\
$\log K = \frac{n\,E^\circ}{0.0591} = \frac{2\times1.10}{0.0591} = \frac{2.20}{0.0591} = 37.23$\\
$K = 10^{37.23} \approx \mathbf{10^{37.2}}$
\end{solution}
"""
with open("exercises/single_correct.tex", "w", encoding="utf-8") as f:
    f.write(single_correct)
print("single_correct.tex:", len(single_correct), "chars")

# ============================================================
# 3. MULTIPLE_CORRECT.TEX
# ============================================================
multiple_correct = r"""\chapter*{Global Exercise Bank --- Multiple Correct MCQs}
\addcontentsline{toc}{chapter}{Global Exercise Bank: Multiple Correct MCQs}
\label{chap:multiple_correct}

\begin{tcolorbox}[enhanced,colback=subtleblue,colframe=primarynavy,arc=2mm,boxrule=1pt,
    title=\textbf{\large One or More Than One Correct Options (All Chapters)}]
Sources: \textbf{[NRJ]} Ex-II Multi, \textbf{[PRSN]} Ex-II, \textbf{[CNG-TH]}, \textbf{[NA]} Level-3.
\end{tcolorbox}

\begin{problembox}
\textbf{MC.1} \hfill \textbf{[NRJ Ex-II Q5 / PRSN Ex-II Q3]}

Which of the following statements about the molar conductance of electrolytes are \textbf{correct}?
\begin{enumerate}[label=(\alph*)]
    \item For strong electrolytes, $\Lambda_m$ increases linearly with $1/\sqrt{c}$ according to Kohlrausch's law.
    \item For weak electrolytes, $\Lambda_m$ cannot be obtained by extrapolating the $\Lambda_m$ vs $\sqrt{c}$ plot.
    \item The specific conductance ($\kappa$) always decreases on dilution.
    \item At the same concentration, $\Lambda_m$ of a strong electrolyte is always greater than that of a weak electrolyte of the same formula type.
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{Correct: (a), (b), (c)}

(a) True: Debye--H\"{u}ckel--Onsager equation $\Lambda_m = \Lambda_m^\circ - b\sqrt{c}$ is linear in $\sqrt{c}$.\\
(b) True: Weak electrolytes show a steep non-linear rise at low $c$; cannot be extrapolated.\\
(c) True: $\kappa = \Lambda_m \cdot c/1000$. Though $\Lambda_m$ increases on dilution, $c$ decreases much faster, so $\kappa$ always decreases on dilution.\\
(d) Not always true: At very low $c$, the weak electrolyte may be nearly fully dissociated and approach $\Lambda_m^\circ$, which can be comparable to the strong electrolyte.
\end{solution}

\begin{problembox}
\textbf{MC.2} \hfill \textbf{[PRSN Ex-II Q7 / NRJ Multi Q8]}

Which of the following cells have $E^\circ_{\text{cell}} > 0$ (spontaneous under standard conditions)?
\begin{enumerate}[label=(\alph*)]
    \item $\ce{Zn | Zn^2+ || Cu^2+ | Cu}$; $E^\circ(\ce{Zn^2+/Zn})=-0.76$, $E^\circ(\ce{Cu^2+/Cu})=+0.34\,\text{V}$
    \item $\ce{Cu | Cu^2+ || Ag+ | Ag}$; $E^\circ(\ce{Cu^2+/Cu})=+0.34$, $E^\circ(\ce{Ag+/Ag})=+0.80\,\text{V}$
    \item $\ce{Ag | Ag+ || Cu^2+ | Cu}$ (reverse of above)
    \item $\ce{Pt, H2 | H+(pH=7) | O2(1 bar), Pt}$; $E^\circ(\ce{O2/H2O})=+1.23\,\text{V}$
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{Correct: (a), (b), (d)}

(a) $E^\circ = 0.34 - (-0.76) = +1.10\,\text{V} > 0$ \checkmark\\
(b) $E^\circ = 0.80 - 0.34 = +0.46\,\text{V} > 0$ \checkmark\\
(c) $E^\circ = 0.34 - 0.80 = -0.46\,\text{V} < 0$ (non-spontaneous) \texttimes\\
(d) At pH = 7: $E_{\ce{H+/H2}} = -0.0591\times7 = -0.414\,\text{V}$; $E_{\text{cell}} = 1.23 - (-0.414) = +1.644\,\text{V} > 0$ \checkmark
\end{solution}

\begin{problembox}
\textbf{MC.3} \hfill \textbf{[NA Level-3 Q5 / NRJ Ex-II Multi Q12]}

In the electrolysis of an aqueous \ce{NaCl} solution with inert platinum electrodes, which of the following statements are \textbf{correct}?
\begin{enumerate}[label=(\alph*)]
    \item In dilute solution, \ce{H2} is produced at the cathode.
    \item In dilute solution, \ce{O2} is produced at the anode.
    \item In concentrated solution, \ce{Cl2} is produced at the anode.
    \item Na metal is deposited at the cathode in both dilute and concentrated solutions.
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{Correct: (a), (b), (c)}

(a) True: \ce{H+} is preferentially reduced over \ce{Na+} in both dilute and concentrated. \checkmark\\
(b) True: In dilute NaCl on Pt, oxygen overpotential is not enough to divert; \ce{OH-}/\ce{H2O} is oxidized. \checkmark\\
(c) True: High [\ce{Cl-}] + high $\eta_{\ce{O2}}$ on graphite/Pt at high current density $\Rightarrow$ \ce{Cl2}. \checkmark\\
(d) False: Na metal cannot be deposited from aqueous solution (water is reduced first; Na would react violently with water anyway). \texttimes
\end{solution}

\begin{problembox}
\textbf{MC.4} \hfill \textbf{[NRJ Ex-II Multi Q16]}

Which of the following are correct statements about corrosion of iron?
\begin{enumerate}[label=(\alph*)]
    \item It is an electrochemical process involving local anodic and cathodic regions.
    \item Salt water accelerates corrosion by increasing ionic conductivity.
    \item Connecting iron to a copper plate slows corrosion of iron.
    \item Rusting requires both oxygen and water simultaneously.
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{Correct: (a), (b), (d)}

(a) True: Corrosion proceeds via local galvanic cells (e.g., grain boundaries as anodes). \checkmark\\
(b) True: NaCl ions increase the electrolyte conductivity, allowing faster ion transport between anodic and cathodic regions, greatly accelerating corrosion. \checkmark\\
(c) False: Cu is less active than Fe ($E^\circ_{\ce{Cu}} = +0.34\,\text{V}$, $E^\circ_{\ce{Fe}} = -0.44\,\text{V}$); Fe acts as anode in the galvanic couple $\Rightarrow$ Fe corrodes faster. \texttimes\\
(d) True: Both are required as established. \checkmark
\end{solution}

\begin{problembox}
\textbf{MC.5} \hfill \textbf{[PRSN Ex-II Q12 / CNG-TH Advanced]}

For the half-reaction $\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}$ ($E^\circ = +1.51\,\text{V}$), which of the following are true?
\begin{enumerate}[label=(\alph*)]
    \item Lowering the pH increases $E$ for this half-reaction.
    \item Raising $[\ce{Mn^2+}]$ decreases $E$.
    \item This half-reaction can oxidize \ce{Cl-} to \ce{Cl2} under standard conditions.
    \item $E^\circ$ for the reverse reaction is $-1.51\,\text{V}$.
\end{enumerate}
\end{problembox}
\begin{solution}
\textbf{Correct: (b), (c), (d)}

(a) False: Nernst equation shows $E = E^\circ - \frac{0.0591}{5}\log\frac{[\ce{Mn^2+}]}{[\ce{MnO4-}][\ce{H+}]^8}$. Lowering $[\ce{H+}]$ (increasing term in denominator) \textit{decreases} $E$. \texttimes\\
(b) True: Higher $[\ce{Mn^2+}]$ increases the numerator in the log term $\Rightarrow$ $E$ decreases. \checkmark\\
(c) True: $E^\circ(\ce{Cl2/Cl-}) = +1.36\,\text{V} < 1.51\,\text{V}$, so \ce{MnO4-} can oxidize \ce{Cl-} to \ce{Cl2} (standard condition). \checkmark\\
(d) True: Reversing the half-reaction reverses the sign of $E^\circ$. \checkmark
\end{solution}
"""
with open("exercises/multiple_correct.tex", "w", encoding="utf-8") as f:
    f.write(multiple_correct)
print("multiple_correct.tex:", len(multiple_correct), "chars")

# ============================================================
# 4. ASSERTION_REASON.TEX
# ============================================================
assertion_reason = r"""\chapter*{Global Exercise Bank --- Assertion--Reason}
\addcontentsline{toc}{chapter}{Global Exercise Bank: Assertion--Reason}
\label{chap:assertion_reason}

\begin{tcolorbox}[enhanced,colback=subtleamber,colframe=accentamber,arc=2mm,boxrule=1pt,
    title=\textbf{\large Assertion--Reason Questions (All Chapters)}]
Use the following key:\\
\textbf{(a)} Both A and R are true; R is the correct explanation of A.\\
\textbf{(b)} Both A and R are true; R is NOT the correct explanation of A.\\
\textbf{(c)} A is true; R is false.\\
\textbf{(d)} A is false; R is true.
\end{tcolorbox}

\begin{problembox}
\textbf{AR.1} \hfill \textbf{[GRB / ESS]}

\textbf{A:} The specific conductance ($\kappa$) of an electrolyte solution always decreases on dilution.

\textbf{R:} On dilution, the number of ions per unit volume decreases even though the degree of dissociation increases.
\end{problembox}
\begin{solution}
\textbf{(a)} Both A and R are true; R correctly explains A. $\kappa = \Lambda_m \cdot c/1000$: although $\Lambda_m$ increases on dilution, the concentration $c$ decreases proportionally faster, so $\kappa$ always decreases.
\end{solution}

\begin{problembox}
\textbf{AR.2} \hfill \textbf{[CNG-TH / NRJ]}

\textbf{A:} The standard hydrogen electrode (SHE) is used as the universal reference electrode.

\textbf{R:} The standard reduction potential of the SHE is arbitrarily defined as exactly zero at all temperatures.
\end{problembox}
\begin{solution}
\textbf{(c)} A is true; R is false. The SHE is the universal reference, but its potential is set to zero only at $298\,\text{K}$ as a convention. At other temperatures, the potential of the SHE is not zero (it varies with temperature due to the temperature dependence of thermodynamic quantities). The convention $E^\circ_{\text{SHE}} = 0$ applies at $298\,\text{K}$, $a_{\ce{H+}}=1$, $f_{\ce{H2}}=1\,\text{bar}$.
\end{solution}

\begin{problembox}
\textbf{AR.3} \hfill \textbf{[ATK / GRB]}

\textbf{A:} The temperature coefficient of EMF, $(\partial E/\partial T)_P$, can be positive, negative, or zero.

\textbf{R:} The sign of $(\partial E/\partial T)_P$ depends on the sign of the entropy change $\Delta S$ for the cell reaction.
\end{problembox}
\begin{solution}
\textbf{(a)} Both true; R correctly explains A. $\Delta S = nF(\partial E/\partial T)_P$. If the cell reaction proceeds with an increase in entropy ($\Delta S > 0$), then $(\partial E/\partial T)_P > 0$ (EMF increases with temperature). If $\Delta S < 0$, EMF decreases with temperature. $\Delta S = 0$ gives a temperature-independent EMF.
\end{solution}

\begin{problembox}
\textbf{AR.4} \hfill \textbf{[GRB / CNG-DPP]}

\textbf{A:} During the discharge of a lead-acid battery, the density of sulfuric acid decreases.

\textbf{R:} During discharge, sulfuric acid is consumed at both electrodes to form \ce{PbSO4}, and water is produced.
\end{problembox}
\begin{solution}
\textbf{(a)} Both true; R correctly explains A. Net discharge: $\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}$. \ce{H2SO4} (dense, $\rho=1.84\,\text{g/mL}$) is consumed; water (lighter, $\rho=1.00\,\text{g/mL}$) is produced $\Rightarrow$ density decreases.
\end{solution}

\begin{problembox}
\textbf{AR.5} \hfill \textbf{[CNG-TH / NRJ]}

\textbf{A:} \ce{KCl}, \ce{KNO3}, and \ce{NH4NO3} are preferred filling materials for salt bridges.

\textbf{R:} These salts have nearly equal ionic mobilities for cation and anion ($t_+ \approx t_-$), which minimizes liquid junction potential.
\end{problembox}
\begin{solution}
\textbf{(a)} Both true; R correctly explains A. The liquid junction potential is minimized when cation and anion transference numbers are equal. For \ce{KCl}: $t_+ = 0.491$, $t_- = 0.509$. For \ce{KNO3} and \ce{NH4NO3}: similar near-equality. These salts also have high solubility and are non-reactive with most electrolytes.
\end{solution}

\begin{problembox}
\textbf{AR.6} \hfill \textbf{[ATK / CNG-TH Advanced]}

\textbf{A:} The mobility of \ce{H+} in aqueous solution ($3.62\times10^{-7}\,\text{m}^2\,\text{V}^{-1}\,\text{s}^{-1}$) is approximately 5 times larger than a typical ion like \ce{Na+} ($5.19\times10^{-8}\,\text{m}^2\,\text{V}^{-1}\,\text{s}^{-1}$).

\textbf{R:} The anomalously high mobility of \ce{H+} is due to the Grotthuss (proton-hopping) mechanism, where \ce{H+} is transferred sequentially along a chain of hydrogen-bonded water molecules rather than migrating as a physical particle.
\end{problembox}
\begin{solution}
\textbf{(a)} Both true; R correctly explains A. In the Grotthuss mechanism, protons hop from one water molecule to the next via hydrogen-bond rearrangements (like a Newton's cradle), which is far faster than the physical diffusion of a bare ion through the viscous water medium. Similarly, \ce{OH-} has high mobility via the same mechanism running in reverse.
\end{solution}

\begin{problembox}
\textbf{AR.7} \hfill \textbf{[GRB / CNG-DPP DPP-5]}

\textbf{A:} Galvanized (zinc-coated) steel remains protected from rusting even when the zinc coating is scratched.

\textbf{R:} Tin-coated steel (tinned iron / food-grade steel) corrodes faster than uncoated iron when the tin layer is scratched.
\end{problembox}
\begin{solution}
\textbf{(b)} Both statements are true but R is not an explanation of A (they are independent facts). A is true because Zn ($E^\circ = -0.76\,\text{V}$) is more active than Fe ($-0.44\,\text{V}$) and acts as sacrificial anode. R is also true: Sn ($E^\circ = -0.14\,\text{V}$) is less active than Fe, so when the Sn coating is scratched, Fe acts as the anode and corrodes faster than bare Fe would, because it is in galvanic contact with Sn. Both are true but are separate, contrasting facts --- not a cause-effect pair.
\end{solution}
"""
with open("exercises/assertion_reason.tex", "w", encoding="utf-8") as f:
    f.write(assertion_reason)
print("assertion_reason.tex:", len(assertion_reason), "chars")

print("\nAll 4 files written successfully.")
