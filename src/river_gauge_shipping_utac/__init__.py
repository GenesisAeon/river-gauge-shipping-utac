"""river-gauge-shipping-utac -- Rhine / Western-Europe low-water inland
shipping impacts (container throughput, Kaub gauge, cascade mechanics,
IfW Kiel GDP note).

GenesisAeon Package 130. Complements glacier-buffer-utac (P99) with the
economic / logistics side of low-water events on glacier-fed rivers.
Own package, not a P99 extension -- cross-reference P99 in docs only.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

Scope is Rhine / Western Europe only. The unconfirmed Bundesbank
0.2 percentage-point Q3-2018 figure is intentionally omitted.
"""

from __future__ import annotations

from .constants import (
    AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL,
    BEDOYA_MAYA_2024_CITATION,
    BUNDESBANK_0_2PP_EXCLUSION_NOTE,
    CRITICAL_WATER_LEVEL_CM,
    CROSS_REF_P99_NOTE,
    DAYS_BELOW_KAUB_FOR_INDUSTRIAL_PRODUCTION_FIGURE,
    GDP_LOSS_PCT_ANNUAL_VIEW,
    IFW_KIEL_2018_CITATION,
    INDUSTRIAL_PRODUCTION_LOSS_PCT_AT_30_DAYS_BELOW_KAUB,
    INDUSTRIAL_PRODUCTION_LOSS_PCT_PEAK_AT_30_DAYS_BELOW_KAUB,
    KAUB_GAUGE_NOTE,
    LOAD_FACTOR_PCT_NOMINAL_HIGH,
    LOAD_FACTOR_PCT_NOMINAL_LOW,
    PACKAGE_ID,
    PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH,
    PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW,
    SCOPE_NOTE,
    THROUGHPUT_LOSS_PCT_WHEN_DISRUPTION_OVER_24_DAYS,
    VINKE_2022_CASCADE_MECHANICS_NOTE,
    VINKE_2022_CITATION,
    VULNERABILITY_DOUBLED_SINCE_YEAR,
)
from .honesty import (
    does_vulnerability_increase_over_time,
    is_kaub_threshold_from_single_study,
    is_relationship_generalizable_beyond_rhine,
)

__version__ = "1.0.0"

__all__ = [
    "AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL",
    "BEDOYA_MAYA_2024_CITATION",
    "BUNDESBANK_0_2PP_EXCLUSION_NOTE",
    "CRITICAL_WATER_LEVEL_CM",
    "CROSS_REF_P99_NOTE",
    "DAYS_BELOW_KAUB_FOR_INDUSTRIAL_PRODUCTION_FIGURE",
    "GDP_LOSS_PCT_ANNUAL_VIEW",
    "IFW_KIEL_2018_CITATION",
    "INDUSTRIAL_PRODUCTION_LOSS_PCT_AT_30_DAYS_BELOW_KAUB",
    "INDUSTRIAL_PRODUCTION_LOSS_PCT_PEAK_AT_30_DAYS_BELOW_KAUB",
    "KAUB_GAUGE_NOTE",
    "LOAD_FACTOR_PCT_NOMINAL_HIGH",
    "LOAD_FACTOR_PCT_NOMINAL_LOW",
    "PACKAGE_ID",
    "PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH",
    "PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW",
    "SCOPE_NOTE",
    "THROUGHPUT_LOSS_PCT_WHEN_DISRUPTION_OVER_24_DAYS",
    "VINKE_2022_CASCADE_MECHANICS_NOTE",
    "VINKE_2022_CITATION",
    "VULNERABILITY_DOUBLED_SINCE_YEAR",
    "does_vulnerability_increase_over_time",
    "is_kaub_threshold_from_single_study",
    "is_relationship_generalizable_beyond_rhine",
    "__version__",
]
