# -*- coding: utf-8 -*-
"""Sanitize Greek and math Unicode symbols across all extracted LaTeX files."""
import glob

unicode_map = {
    'α': r'$\alpha$',
    'β': r'$\beta$',
    'γ': r'$\gamma$',
    'δ': r'$\delta$',
    'ε': r'$\varepsilon$',
    'θ': r'$\theta$',
    'κ': r'$\kappa$',
    'λ': r'$\lambda$',
    'μ': r'$\mu$',
    'ν': r'$\nu$',
    'π': r'$\pi$',
    'ρ': r'$\rho$',
    'σ': r'$\sigma$',
    'τ': r'$\tau$',
    'φ': r'$\phi$',
    'ω': r'$\omega$',
    'Δ': r'$\Delta$',
    'Λ': r'$\Lambda$',
    'Ω': r'$\Omega$',
    '×': r'$\times$',
    '÷': r'$\div$',
    '±': r'$\pm$',
    '≤': r'$\le$',
    '≥': r'$\ge$',
    '≠': r'$\ne$',
    '≈': r'$\approx$',
    '∞': r'$\infty$',
    '√': r'$\sqrt{}$',
    '°': r'$^\circ$',
    'Å': r'\AA',
    '℃': r'$^\circ\text{C}$',
    '℉': r'$^\circ\text{F}$',
    '•': r'$\bullet$',
    '→': r'$\to$',
    '←': r'$\leftarrow$',
    '⇌': r'$\rightleftharpoons$',
    '⇒': r'$\implies$',
    '–': '--',
    '—': '---',
    '‘': "'",
    '’': "'",
    '“': '"',
    '”': '"',
}

files = glob.glob("question_bank/extracted/*.tex") + glob.glob("question_bank/*.tex")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for u_char, latex_repl in unicode_map.items():
        content = content.replace(u_char, latex_repl)
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Sanitized {fpath}")

print("Unicode replacement complete.")
