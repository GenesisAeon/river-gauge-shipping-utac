# river-gauge-shipping-utac

GenesisAeon Package 130 -- Rhine / Western-Europe low-water inland
shipping impacts (container throughput, Kaub gauge, cascade mechanics,
IfW Kiel GDP note). **Deliberately has no UTAC/CREP/AFET bridge** -- see
[DISCLAIMER.md](DISCLAIMER.md).

Complements [`glacier-buffer-utac`](https://github.com/GenesisAeon/glacier-buffer-utac)
(P99) with the economic / logistics side of low-water events. Own
package, not a P99 extension -- cross-reference only; do not rederive
P99 hydrology here.

For a plain-language German companion, see [WHITEPAPER.md](WHITEPAPER.md).

## What's real here

- **Bedoya-Maya et al. (2024, *Transportation Research Part D*)** --
  DOI 10.1016/j.trd.2024.104190: **-0.2%** throughput per day under
  critical water level; **-5.9%** when disruption > 24 days;
  vulnerability **doubled since 2018**; without resilience **7-20%**
  projected annual container throughput loss by 2050.
- **Vinke et al. (2022, *Climate Risk Management*)** -- DOI
  10.1016/j.crm.2022.100400: cascade / network-effect model (Rhine
  2018). Encoded as mechanics note, not a single threshold.
- **Kaub 78 cm** -- operational consensus (not single-study); severe
  events: load factor **10-30%** of nominal.
- **IfW Kiel (2018)** -- ~**0.4%** GDP on annual view; industrial
  production ~**1%** (peak **1.5%**) at 30 days below 78 cm Kaub
  (kielinstitut.de).

**Explicitly omitted:** unconfirmed Bundesbank 0.2pp Q3-2018 figure.

## Quickstart

```bash
pip install river-gauge-shipping-utac
```

```python
from river_gauge_shipping_utac import (
    CRITICAL_WATER_LEVEL_CM,
    AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL,
    is_relationship_generalizable_beyond_rhine,
    does_vulnerability_increase_over_time,
    is_kaub_threshold_from_single_study,
)

print(CRITICAL_WATER_LEVEL_CM)  # 78
print(AVG_THROUGHPUT_LOSS_PCT_PER_DAY_UNDER_CRITICAL)  # -0.2
print(is_relationship_generalizable_beyond_rhine())  # False
print(does_vulnerability_increase_over_time())  # True
print(is_kaub_threshold_from_single_study())  # False
```

## Development

```bash
pip install -e ".[dev]"
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
