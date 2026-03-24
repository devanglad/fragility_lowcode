# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:44:33 2026

@author: devang lad
"""

import numpy as np
import pandas as pd

def logistic_fragility(IM, eta, Ns, beta_0, beta_1, beta_2, beta_3):
    """
    Logistic regression fragility function
    """
    z = beta_0 + beta_1 * np.log(IM) + beta_2 * eta + beta_3 * Ns
    P = np.exp(z) / (1 + np.exp(z))
    return P


def get_fragility_from_csv(frame, subtype, edp, limit_state, IM, eta, Ns):
    df = pd.read_csv("data/fragility_parameters.csv")

    row = df[
        (df["FrameType"] == frame) &
        (df["SubType"] == subtype) &
        (df["EDP"] == edp) &
        (df["LimitState"] == limit_state)
    ].iloc[0]

    return logistic_fragility(
        IM, eta, Ns,
        row["beta_0"], row["beta_1"],
        row["beta_2"], row["beta_3"]
    )
