
# -*- coding: utf-8 -*-
ch07 = r"""\chapter{Commercial Cells, Fuel Cells \& Corrosion}
\label{chap:commercial_cells}

% ==============================================================================
% SECTION 7.1: PRIMARY BATTERIES
% ==============================================================================
\section{Primary Batteries (Non-Rechargeable Cells)}

Primary batteries are \textbf{galvanic cells} that convert chemical energy into electrical energy through a spontaneous redox reaction. They are non-rechargeable because the electrode materials and electrolyte are consumed irreversibly during discharge.

\subsection{The Dry Cell (Leclanch\'{e} Cell)}

The dry cell is the most common primary battery (standard cylindrical AA, AAA, C, D batteries). It was invented by Georges Leclanch\'{e} in 1866.

\begin{conceptbox}[Dry Cell (Leclanch\'{e} Cell) --- Construction and Chemistry]
\textbf{Construction:}
\begin{itemize}
    \item \textbf{Anode:} Zinc container (Zn metal)
    \item \textbf{Cathode:} Carbon (graphite) rod surrounded by \ce{MnO2} paste
    \item \textbf{Electrolyte:} Moist paste of \ce{NH4Cl} + \ce{ZnCl2} (ammonium chloride / zinc chloride)
\end{itemize}

\textbf{Electrode Reactions:}
\begin{align*}
\text{Anode (oxidation):}& \quad \ce{Zn(s) -> Zn^2+(aq) + 2e-}\\
\text{Cathode (reduction):}& \quad \ce{2MnO2(s) + 2NH4+(aq) + 2e- -> Mn2O3(s) + 2NH3(g) + H2O(l)}\\
\text{Net:}& \quad \ce{Zn(s) + 2MnO2(s) + 2NH4+(aq) -> Zn^2+(aq) + Mn2O3(s) + 2NH3(g) + H2O(l)}
\end{align*}

\textbf{Ammonia} is immobilized by complexing with \ce{Zn^2+}: $\ce{Zn^2+ + 4NH3 -> [Zn(NH3)4]^2+}$

\textbf{EMF:} $\approx 1.5\,\text{V}$ (fresh cell); drops with discharge.

\textbf{Limitations:} Voltage drops under load; Zn can corrode locally even when not in use; cannot be recharged.
\end{conceptbox}

\subsection{The Alkaline Battery}

An improved version of the dry cell using an alkaline (KOH) electrolyte instead of the acidic \ce{NH4Cl} paste:

\begin{align*}
\text{Anode (oxidation):}& \quad \ce{Zn(s) + 2OH-(aq) -> ZnO(s) + H2O(l) + 2e-}\\
\text{Cathode (reduction):}& \quad \ce{2MnO2(s) + H2O(l) + 2e- -> Mn2O3(s) + 2OH-(aq)}\\
\text{Net:}& \quad \ce{Zn(s) + 2MnO2(s) -> ZnO(s) + Mn2O3(s)}
\end{align*}

\textbf{Advantages over Leclanch\'{e}:} Longer shelf life; more stable voltage under load; greater capacity; can be stored in a wider temperature range.

\textbf{EMF:} $\approx 1.5\,\text{V}$ (nominally same as Leclanch\'{e} but more stable).

\subsection{The Mercury Button Cell (Ruben--Mallory Cell)}

Used in hearing aids, watches, and electronic instruments requiring a \textbf{precisely constant voltage}:

\begin{align*}
\text{Anode:}& \quad \ce{Zn(s) + 2OH-(aq) -> ZnO(s) + H2O(l) + 2e-}\\
\text{Cathode:}& \quad \ce{HgO(s) + H2O(l) + 2e- -> Hg(l) + 2OH-(aq)}\\
\text{Net:}& \quad \ce{Zn(s) + HgO(s) -> ZnO(s) + Hg(l)}
\end{align*}

\textbf{Electrolyte:} Concentrated \ce{KOH} or \ce{NaOH} solution (absorbed in paste).

\textbf{EMF:} $\approx 1.35\,\text{V}$ (very stable throughout discharge because neither electrode material changes significantly in activity).

\textbf{Note:} Mercury cells are now banned in many countries due to mercury toxicity and environmental concerns.

% ==============================================================================
% SECTION 7.2: SECONDARY (RECHARGEABLE) BATTERIES
% ==============================================================================
\section{Secondary (Rechargeable) Batteries}

Secondary batteries can be restored to their original state by passing current through them in the reverse direction (recharging). The cell reactions are reversible.

\subsection{The Lead--Acid Storage Battery}

The lead--acid battery is the oldest and most widely used rechargeable battery, found in virtually every automobile.

\begin{conceptbox}[Lead--Acid Battery: Discharge Reactions (Cell Delivers Current)]
\textbf{Construction:}
\begin{itemize}
    \item \textbf{Anode:} Lead (Pb) plates (negative during discharge)
    \item \textbf{Cathode:} Lead(IV) oxide (\ce{PbO2}) plates (positive during discharge)
    \item \textbf{Electrolyte:} Dilute sulfuric acid (\ce{H2SO4}), density $\approx 1.28\,\text{g\,mL}^{-1}$ when fully charged
\end{itemize}

\textbf{Discharge Electrode Reactions:}
\begin{align*}
\text{Anode (oxidation):}& \quad \ce{Pb(s) + SO4^2-(aq) -> PbSO4(s) + 2e-} \quad (E^\circ = -0.36\,\text{V})\\
\text{Cathode (reduction):}& \quad \ce{PbO2(s) + SO4^2-(aq) + 4H+(aq) + 2e- -> PbSO4(s) + 2H2O(l)} \quad (E^\circ = +1.69\,\text{V})\\
\text{Net (discharge):}& \quad \ce{Pb(s) + PbO2(s) + 2H2SO4(aq) -> 2PbSO4(s) + 2H2O(l)}
\end{align*}
$E_{\text{cell}}^\circ = 1.69 - (-0.36) = 2.05\,\text{V}$ per cell. A 12-V battery contains 6 cells in series.
\end{conceptbox}

\begin{conceptbox}[Lead--Acid Battery: Charging Reactions (External Power Restores Cell)]
During charging, an external EMF $> 2.05\,\text{V}$ is applied, reversing the discharge reactions:
\begin{align*}
\text{Cathode (reduction, was discharged anode):}& \quad \ce{PbSO4(s) + 2e- -> Pb(s) + SO4^2-(aq)}\\
\text{Anode (oxidation, was discharged cathode):}& \quad \ce{PbSO4(s) + 2H2O(l) -> PbO2(s) + SO4^2-(aq) + 4H+(aq) + 2e-}\\
\text{Net (charging):}& \quad \ce{2PbSO4(s) + 2H2O(l) -> Pb(s) + PbO2(s) + 2H2SO4(aq)}
\end{align*}
\end{conceptbox}

\textbf{Key observations and quantitative analysis:}
\begin{itemize}
    \item Both electrodes form \ce{PbSO4(s)} during discharge --- the ``double sulphate'' rule.
    \item During discharge: \ce{H2SO4} is consumed and water is produced $\to$ density of electrolyte \textbf{decreases}.
    \item During charging: \ce{H2SO4} is regenerated $\to$ density \textbf{increases}. Density of electrolyte (measured with a hydrometer) is a direct indicator of \textbf{state of charge}:
    \begin{itemize}
        \item Fully charged: $\rho \approx 1.28\,\text{g\,mL}^{-1}$
        \item Half discharged: $\rho \approx 1.20\,\text{g\,mL}^{-1}$
        \item Fully discharged: $\rho \approx 1.10\,\text{g\,mL}^{-1}$
    \end{itemize}
    \item \textbf{Ampere-hour capacity:} A 12-V, 60~Ah battery can deliver 60~A for 1~h (or 1~A for 60~h). Energy stored $= V \times\text{Ah} = 12 \times 60 = 720\,\text{Wh} = 2.592\,\text{MJ}$.
\end{itemize}

\begin{examplebox}[Lead-Acid Battery: Mass and Density Change]
\textbf{Problem:} A lead-acid battery discharges for 2~h at 10~A. Calculate (a) the mass of Pb dissolved, (b) the mass of \ce{PbO2} consumed, (c) the mass of \ce{H2SO4} consumed, and (d) the mass of \ce{PbSO4} deposited on each electrode. [$M_{\ce{Pb}}=207$, $M_{\ce{PbO2}}=239$, $M_{\ce{H2SO4}}=98$, $M_{\ce{PbSO4}}=303$]

\textbf{Solution:}
\begin{align*}
Q &= 10\,\text{A} \times 2 \times 3600\,\text{s} = 72000\,\text{C}\\
\text{mol e}^- &= \frac{72000}{96500} = 0.7461\,\text{mol}
\end{align*}
For each electrode reaction ($n=2$ per formula unit):
$\text{mol reacted} = 0.7461/2 = 0.3730\,\text{mol}$

\begin{enumerate}
    \item $w_{\ce{Pb}} = 0.3730 \times 207 = \mathbf{77.2\,\text{g}}$ dissolved at anode
    \item $w_{\ce{PbO2}} = 0.3730 \times 239 = \mathbf{89.1\,\text{g}}$ consumed at cathode
    \item $w_{\ce{H2SO4}} = 0.3730 \times 2 \times 98 = \mathbf{73.1\,\text{g}}$ consumed (2 mol per mol of cell reaction)
    \item $w_{\ce{PbSO4}}$ at each electrode $= 0.3730 \times 303 = \mathbf{113.0\,\text{g}}$ (anode) + same amount at cathode
\end{enumerate}
\end{examplebox}

\subsection{Nickel--Cadmium (Nicad) Battery}

\begin{align*}
\text{Anode (discharge):}& \quad \ce{Cd(s) + 2OH-(aq) -> Cd(OH)2(s) + 2e-}\\
\text{Cathode (discharge):}& \quad \ce{NiO(OH)(s) + H2O(l) + e- -> Ni(OH)2(s) + OH-(aq)}\\
\text{Net:}& \quad \ce{Cd(s) + 2NiO(OH)(s) + 2H2O(l) -> Cd(OH)2(s) + 2Ni(OH)2(s)}
\end{align*}

\textbf{Electrolyte:} \ce{KOH}(aq). \textbf{EMF:} $\approx 1.25\,\text{V}$ per cell.

\textbf{Advantages:} Rechargeable hundreds of times; stable voltage; performs well at low temperatures.

\textbf{Disadvantages:} Memory effect (capacity decreases if not fully discharged before recharging); Cd is highly toxic.

\subsection{Lithium-Ion Battery}

The lithium-ion battery is the dominant rechargeable battery in consumer electronics and electric vehicles.

\begin{conceptbox}[Lithium-Ion Battery: Intercalation Mechanism]
\textbf{Key principle:} Lithium ions (\ce{Li+}) are reversibly ``intercalated'' (inserted/extracted) into layered crystalline structures of the electrode materials --- the electrodes themselves are not consumed.

\textbf{Electrode Materials (most common):}
\begin{itemize}
    \item \textbf{Cathode:} \ce{LiCoO2} (lithium cobalt oxide) --- layered structure
    \item \textbf{Anode:} Graphite (C) --- \ce{Li+} inserts between graphene layers to form \ce{LiC6}
    \item \textbf{Electrolyte:} Lithium hexafluorophosphate (\ce{LiPF6}) in organic carbonate solvents (non-aqueous)
\end{itemize}

\textbf{Discharge Reactions:}
\begin{align*}
\text{Anode (oxidation):}& \quad \ce{LiC6(s) -> Li+(aq) + e- + 6C(s)}\\
\text{Cathode (reduction):}& \quad \ce{Li_{1-x}CoO2 + xLi+(aq) + xe- -> LiCoO2(s)}\\
\text{Net:}& \quad \ce{LiC6 + Li_{1-x}CoO2 -> 6C + LiCoO2}
\end{align*}
During charging, the reverse occurs.
\end{conceptbox}

\textbf{Advantages:} High energy density ($\approx 150\text{--}250\,\text{Wh\,kg}^{-1}$); no memory effect; low self-discharge; wide operating temperature range; high cell voltage ($\approx 3.6\,\text{V}$ per cell).

\textbf{Disadvantages:} Risk of thermal runaway if overcharged or physically damaged; \ce{Co} is scarce and expensive; requires sophisticated battery management systems (BMS).

\textbf{Other cathode materials:} \ce{LiFePO4} (LFP --- safer, more stable), \ce{LiMn2O4} (LMO), \ce{Li(NiMnCo)O2} (NMC), \ce{Li(NiCoAl)O2} (NCA).

% ==============================================================================
% SECTION 7.3: FUEL CELLS
% ==============================================================================
\section{Fuel Cells}

A fuel cell is a galvanic cell that generates electricity by the \textbf{continuous} electrochemical oxidation of a fuel (supplied externally). Unlike a battery, a fuel cell does not run down as long as fuel and oxidant are supplied.

\begin{conceptbox}[Fuel Cell vs.\ Battery]
\begin{itemize}
    \item \textbf{Battery:} Closed system; stores energy in electrode materials; runs down when material consumed.
    \item \textbf{Fuel Cell:} Open system; converts chemical energy of externally supplied fuel; runs continuously.
    \item Both are galvanic cells with spontaneous overall reactions.
\end{itemize}
\end{conceptbox}

\subsection{Alkaline Hydrogen--Oxygen Fuel Cell (Apollo Mission Cell)}

This cell was used to power the Apollo spacecraft. It operates in alkaline \ce{KOH} electrolyte:

\begin{conceptbox}[Alkaline \ce{H2}--\ce{O2} Fuel Cell Reactions]
\textbf{Electrolyte:} Hot concentrated \ce{KOH}(aq) at $\approx200^\circ\text{C}$, 20--40~atm

\begin{align*}
\text{Anode (fuel electrode, oxidation):}& \quad \ce{H2(g) + 2OH-(aq) -> 2H2O(l) + 2e-}\\
\text{Cathode (air electrode, reduction):}& \quad \ce{O2(g) + 2H2O(l) + 4e- -> 4OH-(aq)}\\
\text{Net (overall):}& \quad \ce{2H2(g) + O2(g) -> 2H2O(l)}
\end{align*}

$E^\circ_{\text{cell}} = E^\circ(\ce{O2/OH-}) - E^\circ(\ce{H2/OH-}) = 0.40 - (-0.83) = 1.23\,\text{V}$

A bonus: the water produced is \textbf{drinkable} --- it served as drinking water for the Apollo astronauts!
\end{conceptbox}

\subsection{Proton Exchange Membrane (PEM) Fuel Cell}

The PEM fuel cell is the leading technology for automobiles and portable power:

\begin{conceptbox}[PEM Fuel Cell]
\textbf{Electrolyte:} Solid polymer membrane (Nafion$^\circledR$) --- conducts \ce{H+} ions only, not electrons.
\textbf{Operating temperature:} $60\text{--}90^\circ\text{C}$.
\textbf{Electrode material:} Pt or Pt alloy catalysts.

\begin{align*}
\text{Anode:}& \quad \ce{H2(g) -> 2H+(aq) + 2e-}\\
\text{Cathode:}& \quad \ce{O2(g) + 4H+(aq) + 4e- -> 2H2O(l)}\\
\text{Net:}& \quad \ce{2H2(g) + O2(g) -> 2H2O(l)}
\end{align*}

\textbf{Proton pathway:} \ce{H+} ions move through the solid Nafion membrane from anode to cathode.
\textbf{Electron pathway:} Electrons flow through the external circuit (producing usable current).
\end{conceptbox}

\subsection{Thermodynamic Efficiency of Fuel Cells}

A conventional heat engine is limited by the Carnot efficiency:
\begin{equation}
    \eta_{\text{Carnot}} = 1 - \frac{T_{\text{cold}}}{T_{\text{hot}}} = \frac{T_{\text{hot}} - T_{\text{cold}}}{T_{\text{hot}}}
\end{equation}
A fuel cell converts Gibbs free energy directly to electrical work, bypassing the thermal step, and has a thermodynamic efficiency:
\begin{equation}
    \boxed{\eta_{\text{FC}} = \frac{\Delta G}{\Delta H} = \frac{-nFE_{\text{cell}}}{\Delta H}}
\end{equation}

\begin{examplebox}[Efficiency of the \ce{H2}--\ce{O2} Fuel Cell]
For \ce{2H2(g) + O2(g) -> 2H2O(l)} at $298\,\text{K}$:
\begin{align*}
\Delta H^\circ &= -572\,\text{kJ\,mol}^{-1}\\
\Delta G^\circ &= -nFE^\circ = -4 \times 96500 \times 1.23 = -474.8\,\text{kJ\,mol}^{-1}\\
\eta &= \frac{474.8}{572} = \mathbf{83\%}
\end{align*}
Compare with Carnot efficiency of a typical heat engine operating between $650\,\text{K}$ and $300\,\text{K}$:
$\eta_{\text{Carnot}} = 1 - 300/650 = 53.8\%$.

The fuel cell achieves significantly higher thermodynamic efficiency because it avoids the intermediate thermal step.
\end{examplebox}

% ==============================================================================
% SECTION 7.4: CORROSION
% ==============================================================================
\section{Corrosion: Electrochemical Mechanism and Prevention}

Corrosion is the \textbf{spontaneous electrochemical deterioration} of metals by reaction with their environment. It is responsible for enormous economic losses worldwide ($\approx3\text{--}4\%$ of GDP in industrialized nations).

\subsection{Electrochemical Mechanism of Rusting of Iron}

Rusting of iron is an electrochemical process that requires both water and oxygen (an electrolyte and an oxidant). Pure water without dissolved oxygen does not cause significant rusting. The process involves local galvanic cells formed at different points on the iron surface (due to grain boundaries, surface impurities, stress differences, dissolved salts, etc.):

\begin{conceptbox}[Electrochemical Mechanism of Rusting]
\textbf{At the anodic region} (where iron is in contact with less oxygenated water):
\begin{align*}
\text{Anode:}& \quad \ce{Fe(s) -> Fe^2+(aq) + 2e-} \quad (E^\circ = -0.44\,\text{V})
\end{align*}

\textbf{At the cathodic region} (where iron is in contact with more oxygenated water):
\begin{align*}
\text{Cathode (neutral/alkaline):}& \quad \ce{O2(g) + 2H2O(l) + 4e- -> 4OH-(aq)} \quad (E^\circ = +0.40\,\text{V})\\
\text{Cathode (acidic):}& \quad \ce{O2(g) + 4H+(aq) + 4e- -> 2H2O(l)} \quad (E^\circ = +1.23\,\text{V})
\end{align*}

\textbf{Overall reaction forming iron(II) hydroxide:}
\begin{align*}
&\ce{Fe(s) -> Fe^2+(aq) + 2e-} \quad \times 2\\
&\ce{O2(g) + 2H2O(l) + 4e- -> 4OH-(aq)}\\
\hline
&\ce{2Fe(s) + O2(g) + 2H2O(l) -> 2Fe(OH)2(s)}
\end{align*}

\textbf{Further oxidation by dissolved oxygen} converts \ce{Fe(OH)2} to rust (\ce{Fe2O3} hydrate):
\begin{align*}
&\ce{4Fe(OH)2(s) + O2(g) + 2H2O(l) -> 4Fe(OH)3(s)}\\
&\ce{2Fe(OH)3(s) -> Fe2O3 . H2O(s) + 2H2O(l)} \quad \text{(hydrated iron(III) oxide = \textbf{rust})}
\end{align*}

\textbf{Rust composition:} \ce{Fe2O3 . xH2O} (hydrated iron(III) oxide), also written as \ce{Fe(OH)3} or \ce{FeO(OH)}.

$E^\circ_{\text{cell}} = +0.40 - (-0.44) = 0.84\,\text{V}$ (spontaneous, $\Delta G < 0$).
\end{conceptbox}

\subsection{Factors Promoting Corrosion}

\begin{enumerate}
    \item \textbf{Presence of electrolytes:} Salt water (sea spray, road salt) greatly accelerates corrosion by increasing electrolyte conductivity.
    \item \textbf{Dissolved oxygen:} Necessary as the cathodic oxidant; higher $[\ce{O2}]$ increases rate.
    \item \textbf{Acidity (lower pH):} Provides $\ce{H+}$ as an alternative cathodic reactant.
    \item \textbf{Temperature:} Higher temperature increases reaction rates.
    \item \textbf{Contact with a more noble metal:} Galvanic coupling; the less noble metal (higher $E^\circ$ for oxidation) corrodes preferentially (e.g., Fe in contact with Cu corrodes faster).
    \item \textbf{Physical stress/non-uniformity:} Stressed regions or grain boundaries act as anodes.
    \item \textbf{$\ce{CO2}$:} Dissolves in water to form carbonic acid ($\ce{H2CO3}$), reducing pH.
    \item \textbf{$\ce{SO2}$:} Industrial pollutant; forms \ce{H2SO4} in solution --- acid rain.
\end{enumerate}

\subsection{Corrosion Prevention Techniques}

\subsubsection{1. Barrier (Passive) Protection}
Physical coating isolates metal from the environment:
\begin{itemize}
    \item Painting, lacquering, varnishing
    \item Coating with polymers (PVC coating on reinforcing bars)
    \item Enameling and vitreous enamel coatings
    \item Electroplating with Ni, Cr, Sn, Au (noble metals)
    \item Galvanizing (zinc coating, see below)
    \item Anodizing aluminum (electrochemically thickening the natural \ce{Al2O3} layer)
\end{itemize}

\subsubsection{2. Sacrificial (Anodic) Protection --- Galvanization}

A more active (less noble) metal is placed in electrical contact with the metal to be protected. The more active metal acts as the \textbf{sacrificial anode} and corrodes preferentially while protecting the base metal:

\begin{conceptbox}[Galvanization (Zinc Coating on Steel)]
Zinc ($E^\circ_{\ce{Zn^2+/Zn}} = -0.76\,\text{V}$) is more active than iron ($E^\circ_{\ce{Fe^2+/Fe}} = -0.44\,\text{V}$).

When galvanized steel (Zn-coated steel) is scratched:
\begin{itemize}
    \item Zn acts as the \textbf{anode}: $\ce{Zn -> Zn^2+ + 2e-}$
    \item Fe acts as the \textbf{cathode}: $\ce{O2 + 2H2O + 4e- -> 4OH-}$
    \item Fe is protected; Zn sacrifices itself.
\end{itemize}
\textbf{Note:} If Fe is coated with Sn (tinned steel, used in food cans), and the coating is scratched, Sn ($E^\circ = -0.14\,\text{V}$) is \textit{less} active than Fe, so Fe acts as the anode and corrodes \textit{faster} than if uncoated. This is why damaged tin cans rust quickly.
\end{conceptbox}

Other sacrificial anodes used industrially:
\begin{itemize}
    \item Zinc blocks attached to ship hulls (protect the hull and propeller)
    \item Magnesium rods in underground pipelines and hot water tanks
    \item Zinc or Mg blocks on offshore drilling platforms
\end{itemize}

\subsubsection{3. Cathodic Protection with Impressed Current}

An external DC current is applied to make the metal to be protected the \textbf{cathode} of an electrolytic cell:
\begin{itemize}
    \item Used for pipelines, ship hulls, oil rigs, reinforced concrete structures.
    \item The metal structure is connected to the negative terminal of a DC power supply.
    \item An inert anode (graphite or titanium) is buried in the soil nearby.
    \item The impressed cathodic current prevents the metal from acting as an anode (oxidizing).
\end{itemize}

\subsubsection{4. Alloying}

Incorporating corrosion-resistant elements into the metal:
\begin{itemize}
    \item \textbf{Stainless steel:} Fe + 10.5\% Cr (+ Ni, Mo). Chromium forms a thin, adherent, self-healing \ce{Cr2O3} passive film.
    \item \textbf{Monel metal:} Ni + Cu alloy; resistant to seawater.
    \item \textbf{Cupronickel:} Cu + 10--30\% Ni; used in coins and marine engineering.
\end{itemize}

\subsubsection{5. Corrosion Inhibitors}

Chemical substances added to the corrosive medium to retard corrosion:
\begin{itemize}
    \item \textbf{Anodic inhibitors:} Increase anodic overpotential (e.g., chromates \ce{CrO4^2-}, nitrites \ce{NO2-}, phosphates). They promote passivation.
    \item \textbf{Cathodic inhibitors:} Slow the cathodic reaction (e.g., arsenic, bismuth compounds; increase $\eta_{\ce{H2}}$).
    \item \textbf{Mixed inhibitors:} Organic amines and surfactants that adsorb on both electrode surfaces.
\end{itemize}

\subsection{Standard Reduction Potential and Corrosion}

The ease of corrosion is directly related to the metal's position in the electrochemical series:
\begin{itemize}
    \item Metals with \textbf{very negative} $E^\circ$ (Na, K, Mg, Al) are highly reactive and corrode easily.
    \item Metals with \textbf{positive} $E^\circ$ (Au, Pt, Ag) are noble and do not corrode under normal conditions.
    \item Iron ($E^\circ = -0.44\,\text{V}$) is in the middle; it corrodes at a significant rate in the presence of water and oxygen.
\end{itemize}

\begin{atkinsbox}[Pilling--Bedworth Ratio: Passivation vs.\ Cracking]
The \textbf{Pilling--Bedworth (PB) ratio} determines whether an oxide film is protective:
\begin{equation}
    R_{\text{PB}} = \frac{V_{\text{oxide}}}{V_{\text{metal}}}= \frac{M_{\text{oxide}} \cdot \rho_{\text{metal}}}{n \cdot M_{\text{metal}} \cdot \rho_{\text{oxide}}}
\end{equation}
\begin{itemize}
    \item $R_{\text{PB}} < 1$: Oxide is porous (e.g., $\ce{MgO}$, $R=0.81$): not protective; metal corrodes.
    \item $1 < R_{\text{PB}} < 2$: Oxide is protective and adherent (e.g., $\ce{Al2O3}$, $R=1.28$; $\ce{Cr2O3}$, $R=2.02$).
    \item $R_{\text{PB}} > 2$: Oxide cracks and spalls off due to compressive stress (e.g., $\ce{Fe2O3}$, $R=2.14$): not protective.
\end{itemize}
Rust (\ce{Fe2O3}) has $R_{\text{PB}} > 2$, so it spalls off and exposes fresh Fe to further corrosion --- this is why rusting is a progressive, self-accelerating process unlike aluminum corrosion.
\end{atkinsbox}

\section{Comparison: Primary, Secondary, and Fuel Cells}

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{p{2.5cm}p{3.5cm}p{3.5cm}p{3.5cm}}
\toprule
\textbf{Property} & \textbf{Primary Cell} & \textbf{Secondary Cell} & \textbf{Fuel Cell}\\
\midrule
Rechargeability & Not rechargeable & Rechargeable & Continuous (not stored)\\
Fuel source & Internal (electrode) & Internal (electrode) & External (continuous)\\
Examples & Dry cell, Hg cell & Lead-acid, Li-ion & \ce{H2-O2}, PEM\\
Energy density & Moderate & Moderate--High & Very High\\
Reaction type & Irreversible & Reversible & Continuous\\
By-products & Chemical waste & Chemical waste & Only \ce{H2O} (\ce{H2}/\ce{O2})\\
\bottomrule
\end{tabular}
\end{center}
"""

with open(r"chapters/ch07_commercial_cells_corrosion.tex", "w", encoding="utf-8") as f:
    f.write(ch07)
print("ch07 written:", len(ch07), "chars,", ch07.count("\n"), "lines")
