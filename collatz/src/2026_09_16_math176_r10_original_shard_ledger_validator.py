#!/usr/bin/env python3
"""MATH-176: validate permanent r=10 original-shard closure ledger.

This is bookkeeping/reproducibility infrastructure only.  It regenerates the
frozen r=10 MATH-115 source and the exact MATH-114 128-way partition, then
checks that every CLOSED ledger row refers to one original shard with exactly
the expected occurrence mass and an existing certificate record.

Without --require-complete, a valid partial ledger prints PASS PARTIAL and
makes no r=10 layer-closure claim.  With --require-complete, all shard IDs
0..127 must occur exactly once and their mass must equal the frozen layer mass.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED_CYLINDERS = 278_725
EXPECTED_LAYER_MASS = 27_557_263_803_397
EXPECTED_SHARDS = 128


def run(cmd: list[str], *, stdout=None, stderr=None) -> None:
    subprocess.run(cmd, check=True, stdout=stdout, stderr=stderr)


def regenerate_expected(repo: Path, tmp: Path) -> dict[int, int]:
    src = tmp / "r10.tsv"
    log = tmp / "r10-export.log"
    shards = tmp / "r10-shards"
    with src.open("w") as out, log.open("w") as err:
        run(
            [
                sys.executable,
                str(repo / "collatz/src/2026_09_13_math115_generic_r2_r12_exporter.py"),
                "--r",
                "10",
            ],
            stdout=out,
            stderr=err,
        )
    text = log.read_text()
    expected_log = (
        "MATH-115 export PASS r=10 cylinders=278725 "
        "occurrences=27557263803397 max_multiplicity=830483089363"
    )
    assert expected_log in text, text

    prep_log = tmp / "r10-prepare.log"
    with prep_log.open("w") as out:
        run(
            [
                sys.executable,
                str(repo / "collatz/src/2026_09_13_math115_prepare_mass_balanced_shards.py"),
                "--input",
                str(src),
                "--shards",
                str(EXPECTED_SHARDS),
                "--out-dir",
                str(shards),
            ],
            stdout=out,
            stderr=subprocess.STDOUT,
        )

    masses: dict[int, int] = {}
    total_rows = 0
    for s in range(EXPECTED_SHARDS):
        p = shards / f"shard-{s:03d}.tsv"
        assert p.exists(), p
        mass = 0
        rows = 0
        for line in p.read_text().splitlines():
            if not line.strip():
                continue
            a, b, m = map(int, line.split("\t"))
            assert a >= 0 and b > 0 and m > 0
            mass += m
            rows += 1
        assert rows > 0, (s, rows)
        masses[s] = mass
        total_rows += rows

    assert len(masses) == EXPECTED_SHARDS
    assert sum(masses.values()) == EXPECTED_LAYER_MASS
    # MATH-114 exact splitting may increase record count relative to source;
    # the canonical known prepared count is 278,739.
    assert total_rows == 278_739, total_rows
    return masses


def read_ledger(repo: Path, ledger: Path, expected: dict[int, int]) -> tuple[set[int], int]:
    rows = list(csv.DictReader(ledger.open(), delimiter="\t"))
    required = {
        "original_shard",
        "status",
        "math_id",
        "workflow_run",
        "certified_mass",
        "certificate_ref",
    }
    assert rows, "empty ledger"
    assert required.issubset(rows[0].keys()), rows[0].keys()

    seen: set[int] = set()
    mass_sum = 0
    for row in rows:
        s = int(row["original_shard"])
        assert 0 <= s < EXPECTED_SHARDS, s
        assert s not in seen, f"duplicate original shard {s}"
        seen.add(s)
        assert row["status"] == "CLOSED", (s, row["status"])
        assert row["math_id"].startswith("MATH-"), (s, row["math_id"])
        assert row["workflow_run"].isdigit(), (s, row["workflow_run"])
        mass = int(row["certified_mass"])
        assert mass == expected[s], (s, mass, expected[s])
        cert = repo / row["certificate_ref"]
        assert cert.is_file(), (s, cert)
        mass_sum += mass
    return seen, mass_sum


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--ledger",
        default="collatz/results/2026-09-16-math176-r10-original-shard-ledger.tsv",
    )
    ap.add_argument("--require-complete", action="store_true")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[2]
    ledger = repo / args.ledger
    assert ledger.is_file(), ledger

    with tempfile.TemporaryDirectory(prefix="math176-") as td:
        expected = regenerate_expected(repo, Path(td))
    seen, mass_sum = read_ledger(repo, ledger, expected)

    if args.require_complete:
        assert seen == set(range(EXPECTED_SHARDS)), (
            "missing",
            sorted(set(range(EXPECTED_SHARDS)) - seen),
        )
        assert mass_sum == EXPECTED_LAYER_MASS, (mass_sum, EXPECTED_LAYER_MASS)
        print(
            "PASS MATH-176 COMPLETE original_shards=128 "
            f"certified_mass={mass_sum} r10_layer_aggregation_ready=1"
        )
    else:
        print(
            "PASS MATH-176 PARTIAL "
            f"closed_original_shards={len(seen)} certified_mass={mass_sum} "
            "r10_layer_aggregation_ready=0"
        )
        print("closed_ids=" + ",".join(map(str, sorted(seen))))
        print("NO r=10 LAYER CLOSURE CLAIM")


if __name__ == "__main__":
    main()
