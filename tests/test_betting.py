import math

import pytest

from ufc_model.betting import (
    american_to_decimal,
    closing_line_value,
    devig_multiplicative,
    expected_value,
    kelly_fraction,
    stake,
)


def test_american_to_decimal() -> None:
    assert american_to_decimal(150) == pytest.approx(2.5)
    assert american_to_decimal(-200) == pytest.approx(1.5)
    with pytest.raises(ValueError, match="odds"):
        american_to_decimal(0)


def test_devig_sums_to_one() -> None:
    p_a, p_b = devig_multiplicative(1.5, 2.8)
    assert p_a + p_b == pytest.approx(1.0)
    assert p_a > p_b


def test_devig_rejects_bad_odds() -> None:
    with pytest.raises(ValueError, match="odds"):
        devig_multiplicative(1.0, 2.0)


def test_expected_value() -> None:
    assert expected_value(0.5, 2.0) == pytest.approx(0.0)
    assert expected_value(0.55, 2.0) == pytest.approx(0.10)


def test_kelly_zero_without_edge() -> None:
    assert kelly_fraction(0.4, 2.0) == 0.0
    assert kelly_fraction(0.6, 2.0) == pytest.approx(0.2)


def test_stake_is_capped() -> None:
    # Full Kelly 0.2 -> quarter Kelly 0.05, capped at 2% of a $200 pool.
    assert stake(0.6, 2.0, bankroll=200.0) == pytest.approx(4.0)


def test_clv_sign() -> None:
    assert closing_line_value(2.2, 2.0) == pytest.approx(math.log(1.1))
    assert closing_line_value(1.8, 2.0) < 0
