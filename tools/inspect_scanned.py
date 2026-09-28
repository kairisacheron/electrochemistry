# -*- coding: utf-8 -*-
import fitz, sys
from rapidocr_onnxruntime import RapidOCR
sys.stdout.reconfigure(encoding='utf-8')

ocr = RapidOCR()

def inspect_scanned(filename):
    doc = fitz.open(filename)
    print(f"=== {filename} (Total pages: {len(doc)}) ===")
    for p in range(0, min(len(doc), 45), 4):
        pix = doc[p].get_pixmap(dpi=100)
        res, _ = ocr(pix.tobytes('png'))
        if res:
            first_lines = " | ".join([r[1] for r in res[:4]])
            print(f"Page {p+1}: {first_lines}")
    print()

inspect_scanned("ElectroChemistry(Nrndr).pdf")
inspect_scanned("ElectroChemistryProblems(Prsn).pdf")
inspect_scanned("ElectroChemistryDPP(cng).pdf")
