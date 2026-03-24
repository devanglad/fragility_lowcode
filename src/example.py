# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:45:46 2026

@author: devang lad cege
"""
from src.fragility import get_fragility_from_csv

P = get_fragility_from_csv(
    frame="Steel",
    subtype="Welded",
    edp="MIDR",
    limit_state="LS2",
    IM=0.4,
    eta=20,
    Ns=6
)

print(f"Probability of exceedance: {P:.4f}")

