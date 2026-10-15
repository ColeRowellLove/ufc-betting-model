"""Odds maths: vig removal, expected value, Kelly sizing, closing line value.

All odds here are decimal odds unless the name says otherwise.
"""

from __future__ import annotations

import math


def american_to_decimal(american: float) -> float:
    """Convert American moneyline odds to decimal odds."""
    if american == 0:
        raise ValueError("American odds cannot be 0")
    if american > 0:
        return 1.0 + american / 100.0
    return 1.0 + 100.0 / -american


def devig_multiplicative(decimal_a: float, decimal_b: float) -> tuple[float, float]:
    """Remove the vig from a two-way market by normalising implied probabilities."""
    if decimal_a <= 1.0 or decimal_b <= 1.0:
        raise ValueError("Decimal odds must be greater than 1")
    inv_a, inv_b = 1.0 / decimal_a, 1.0 / decimal_b
    total = inv_a + inv_b
    return inv_a / total, inv_b / total


def expected_value(p: float, decimal_odds: float) -> float:
    """Expected profit per unit staked: p * d - 1."""
    return p * decimal_odds - 1.0


def kelly_fraction(p: float, decimal_odds: float) -> float:
    """Full-Kelly fraction of bankroll; 0 when there is no edge."""
    b = decimal_odds - 1.0
    if b <= 0:
        raise ValueError("Decimal odds must be greater than 1")
    return max(0.0, (b * p - (1.0 - p)) / b)


def stake(
    p: float,
    decimal_odds: float,
    bankroll: float,
    kelly_multiplier: float = 0.25,
    max_fraction: float = 0.02,
) -> float:
    """Fractional-Kelly stake, capped at ``max_fraction`` of the bankroll."""
    fraction = min(kelly_multiplier * kelly_fraction(p, decimal_odds), max_fraction)
    return fraction * bankroll


def closing_line_value(decimal_taken: float, decimal_close: float) -> float:
    """CLV = ln(d_taken / d_close); positive means you beat the closing price."""
    return math.log(decimal_taken / decimal_close)
