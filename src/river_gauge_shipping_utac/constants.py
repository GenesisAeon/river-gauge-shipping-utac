"""Verified constants for Rhine / Western-Europe low-water inland shipping impacts.

GenesisAeon Package 130. Complements glacier-buffer-utac (P99) with the
economic / logistics side of low-water events on glacier-fed rivers.
Own package, not a P99 extension -- different physical/economic domain
(logistics/economy vs hydrology/ecology). Cross-reference P99 in docs
only; do not rederive P99 hydrology here.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

Scope is Rhine / Western Europe only. Do not generalise beyond that
geography. The unconfirmed Bundesbank 0.2 percentage-point Q3-2018
growth figure is intentionally omitted.
"""

from __future__ import annotations

PACKAGE_ID = 130

# =====================================================================
# Bedoya-Maya, F., Shobayo, P., Beckers, J., van Hassel, E. (2024).
# "The impact of critical water levels on container inland waterway
# transport." Transportation Research Part D: Transport and Environment.
# DOI: 10.1016/j.trd.2024.104190
# =====================================================================

BEDOYA_MAYA_2024_CITATION = {
    "authors": "Bedoya-Maya, F., Shobayo, P., Beckers, J., van Hassel, E.",
    "year": 2024,
    "title": "The impact of critical water levels on container inland waterway transport",
    "journal": "Transportation Research Part D: Transport and Environment",
    "doi": "10.1016/j.trd.2024.104190",
}

# Average throughput disturbance under critical water level (percent per day).
AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL = -0.2

# Throughput loss when disruption lasts more than 24 days (percent).
THROUGHPUT_LOSS_PCT_WHEN_DISRUPTION_OVER_24_DAYS = -5.9

# Vulnerability to critical conditions has doubled since this year
# (Bedoya-Maya et al. 2024 documents the doubling; year is the baseline).
VULNERABILITY_DOUBLED_SINCE_YEAR = 2018

# Projected annual container throughput loss by 2050 without resilience
# measures (percent), low/high bounds.
PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW = 7
PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH = 20

# =====================================================================
# Vinke, F.R.S., van Koningsveld, M., van Dorsser, C., Baart, F.,
# van Gelder, P., Vellinga, T. (2022). "Cascading effects of sustained
# low water on inland shipping." Climate Risk Management, 35, 100400.
# DOI: 10.1016/j.crm.2022.100400
#
# Systemic cascade model, Rhine 2018 case study. No single threshold
# constant -- encode as cascade-mechanics note only.
# =====================================================================

VINKE_2022_CITATION = {
    "authors": (
        "Vinke, F.R.S., van Koningsveld, M., van Dorsser, C., "
        "Baart, F., van Gelder, P., Vellinga, T."
    ),
    "year": 2022,
    "title": "Cascading effects of sustained low water on inland shipping",
    "journal": "Climate Risk Management",
    "volume": 35,
    "article_id": "100400",
    "doi": "10.1016/j.crm.2022.100400",
}

VINKE_2022_CASCADE_MECHANICS_NOTE = (
    "Vinke et al. (2022) provide a systemic cascade / network-effect "
    "model of sustained low water on inland shipping, with the Rhine "
    "2018 low-water event as the case study. This is core-tier evidence "
    "for cascade mechanics, not a single numeric threshold. Do not "
    "collapse it into one constant."
)

# =====================================================================
# Kaub gauge (Rhine) -- documented, cross-confirmed operational consensus
# (ICIS, Chemistry World, freight trade press; not a single study).
# =====================================================================

KAUB_GAUGE_NOTE = (
    "Kaub gauge critical water level is documented, cross-confirmed "
    "operational consensus (ICIS, Chemistry World, freight trade press), "
    "not single-study-based. Same category as other Rhine 78 cm "
    "operational references in the ecosystem."
)

CRITICAL_WATER_LEVEL_CM = 78

# Load factor as percent of nominal capacity under severe low-water
# events (2018, 2022, Aug. 2026), low/high documented range.
LOAD_FACTOR_PCT_NOMINAL_LOW = 10
LOAD_FACTOR_PCT_NOMINAL_HIGH = 30

# =====================================================================
# IfW Kiel (Institut fuer Weltwirtschaft), 2018 -- institute own statement
# cited from kielinstitut.de. Methodologically linked to industrial
# production decline of ~1% (peak 1.5%) at 30 days below 78 cm Kaub.
# =====================================================================

IFW_KIEL_2018_CITATION = {
    "authors": "IfW Kiel (Institut fuer Weltwirtschaft)",
    "year": 2018,
    "title": (
        "Niedrigwasser am Rhein: auf Jahressicht etwa 0,4 Prozent "
        "Wirtschaftsleistung"
    ),
    "source": "kielinstitut.de",
    "url_note": "Direct institute statement; cite kielinstitut.de",
}

# Approximate annual-view GDP loss (percent) attributed to the low-water
# event by IfW Kiel 2018.
GDP_LOSS_PCT_ANNUAL_VIEW = 0.4

# Industrial production decline (~1%, peak 1.5%) when water stays below
# 78 cm Kaub for 30 days -- IfW Kiel methodological link.
INDUSTRIAL_PRODUCTION_LOSS_PCT_AT_30_DAYS_BELOW_KAUB = 1.0
INDUSTRIAL_PRODUCTION_LOSS_PCT_PEAK_AT_30_DAYS_BELOW_KAUB = 1.5
DAYS_BELOW_KAUB_FOR_INDUSTRIAL_PRODUCTION_FIGURE = 30

# Explicit exclusion note (unconfirmed; do not encode as a constant).
BUNDESBANK_0_2PP_EXCLUSION_NOTE = (
    "The Bundesbank 0.2 percentage-point Q3-2018 growth-effect figure "
    "is intentionally omitted: the August 2018 Monthly Report was "
    "identified, but the exact wording could not be confirmed on "
    "bundesbank.de / publikationen.bundesbank.de. Do not invent or "
    "approximate it."
)

SCOPE_NOTE = (
    "All quantitative relationships in this package are Rhine / "
    "Western-Europe specific. No general (non-Rhine) water-level to "
    "capacity model is claimed. See is_relationship_generalizable_beyond_rhine()."
)

CROSS_REF_P99_NOTE = (
    "Cross-reference: glacier-buffer-utac (P99) covers hydrology / "
    "ecology of glacier-fed river buffers. This package (P130) covers "
    "logistics / economy of low-water shipping impacts. Do not rederive "
    "P99 here."
)
