"""Structural honesty checks for river-gauge-shipping-utac (P130).

These functions encode documented scope and epistemic limits -- not
derived model outputs. Always return the fixed booleans below.
"""

from __future__ import annotations

from .constants import VULNERABILITY_DOUBLED_SINCE_YEAR


def is_relationship_generalizable_beyond_rhine() -> bool:
    """Whether the encoded water-level / throughput / GDP relationships
    may be generalised beyond the Rhine / Western Europe.

    Documented evidence is Rhine- and Western-Europe-specific; no
    general (non-Rhine) gauge-to-capacity model is claimed. Always False.
    """
    return False


def does_vulnerability_increase_over_time() -> bool:
    """Whether vulnerability to critical low-water conditions has
    increased over time.

    Bedoya-Maya et al. (2024) document that vulnerability has doubled
    since VULNERABILITY_DOUBLED_SINCE_YEAR (2018). Always True.
    """
    _ = VULNERABILITY_DOUBLED_SINCE_YEAR  # documented baseline year
    return True


def is_kaub_threshold_from_single_study() -> bool:
    """Whether the 78 cm Kaub critical threshold comes from a single
    study.

    It is documented, cross-confirmed operational consensus (ICIS,
    Chemistry World, freight trade press), not single-study-based.
    Always False.
    """
    return False
