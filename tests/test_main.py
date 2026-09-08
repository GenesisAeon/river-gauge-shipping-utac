from __future__ import annotations

from river_gauge_shipping_utac import (
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
    LOAD_FACTOR_PCT_NOMINAL_HIGH,
    LOAD_FACTOR_PCT_NOMINAL_LOW,
    PACKAGE_ID,
    PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH,
    PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW,
    THROUGHPUT_LOSS_PCT_WHEN_DISRUPTION_OVER_24_DAYS,
    VINKE_2022_CASCADE_MECHANICS_NOTE,
    VINKE_2022_CITATION,
    VULNERABILITY_DOUBLED_SINCE_YEAR,
    __version__,
    does_vulnerability_increase_over_time,
    is_kaub_threshold_from_single_study,
    is_relationship_generalizable_beyond_rhine,
)


def test_package_id_and_version() -> None:
    assert PACKAGE_ID == 130
    assert __version__ == "1.0.0"


def test_bedoya_maya_constants() -> None:
    assert BEDOYA_MAYA_2024_CITATION["doi"] == "10.1016/j.trd.2024.104190"
    assert AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL == -0.2
    assert THROUGHPUT_LOSS_PCT_WHEN_DISRUPTION_OVER_24_DAYS == -5.9
    assert VULNERABILITY_DOUBLED_SINCE_YEAR == 2018
    assert PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW == 7
    assert PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH == 20
    assert (
        PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_LOW
        < PROJECTED_ANNUAL_CONTAINER_THROUGHPUT_LOSS_PCT_2050_HIGH
    )


def test_vinke_cascade_note_no_threshold_constant() -> None:
    assert VINKE_2022_CITATION["doi"] == "10.1016/j.crm.2022.100400"
    assert "cascade" in VINKE_2022_CASCADE_MECHANICS_NOTE.lower()
    assert "not a single numeric threshold" in VINKE_2022_CASCADE_MECHANICS_NOTE.lower()


def test_kaub_gauge_operational_consensus() -> None:
    assert CRITICAL_WATER_LEVEL_CM == 78
    assert LOAD_FACTOR_PCT_NOMINAL_LOW == 10
    assert LOAD_FACTOR_PCT_NOMINAL_HIGH == 30
    assert LOAD_FACTOR_PCT_NOMINAL_LOW < LOAD_FACTOR_PCT_NOMINAL_HIGH
    assert is_kaub_threshold_from_single_study() is False


def test_ifw_kiel_gdp_and_industrial() -> None:
    assert GDP_LOSS_PCT_ANNUAL_VIEW == 0.4
    assert INDUSTRIAL_PRODUCTION_LOSS_PCT_AT_30_DAYS_BELOW_KAUB == 1.0
    assert INDUSTRIAL_PRODUCTION_LOSS_PCT_PEAK_AT_30_DAYS_BELOW_KAUB == 1.5
    assert DAYS_BELOW_KAUB_FOR_INDUSTRIAL_PRODUCTION_FIGURE == 30
    assert IFW_KIEL_2018_CITATION["source"] == "kielinstitut.de"
    assert IFW_KIEL_2018_CITATION["year"] == 2018


def test_honesty_structural() -> None:
    assert is_relationship_generalizable_beyond_rhine() is False
    assert does_vulnerability_increase_over_time() is True
    assert is_kaub_threshold_from_single_study() is False


def test_bundesbank_figure_excluded() -> None:
    assert "intentionally omitted" in BUNDESBANK_0_2PP_EXCLUSION_NOTE.lower()
    # Must not appear as an encoded numeric constant in the public API.
    from river_gauge_shipping_utac import constants as c

    names = [n for n in dir(c) if n.isupper()]
    assert not any("BUNDESBANK" in n and n.endswith("_PCT") for n in names)
    assert "BUNDESBANK_0_2PP_EXCLUSION_NOTE" in names


def test_cross_ref_p99_docs_only() -> None:
    assert "glacier-buffer-utac" in CROSS_REF_P99_NOTE
    assert "P99" in CROSS_REF_P99_NOTE
    assert "Do not rederive" in CROSS_REF_P99_NOTE


def test_no_crep_afet_gamma_bridge_symbols() -> None:
    import re
    from pathlib import Path

    import river_gauge_shipping_utac as m

    public = " ".join(n for n in dir(m) if not n.startswith("_")).upper()
    assert "CREP" not in public
    assert "AFET" not in public
    assert "GAMMA" not in public

    # Disclaimer may mention "no UTAC/CREP/AFET bridge"; strip that phrase,
    # then ensure no remaining bridge vocabulary / Gamma inventions.
    src = Path(m.__file__).resolve().parent
    blob = "\n".join(p.read_text(encoding="utf-8") for p in src.glob("*.py"))
    assert re.search(r"no\s+UTAC/CREP/AFET", blob, flags=re.IGNORECASE)
    cleaned = re.sub(
        r"no\s+UTAC/CREP/AFET(?:\s+bridge)?",
        "",
        blob,
        flags=re.IGNORECASE,
    ).upper()
    assert "CREP" not in cleaned
    assert "AFET" not in cleaned
    assert "GAMMA" not in cleaned
