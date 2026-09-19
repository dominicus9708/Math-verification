#!/usr/bin/env python3
"""MATH-259 permanent r=10 singleton-shell ledger validator."""
import argparse
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
LEDGER=ROOT/"results"/"2026-09-19-math259-r10-singleton-shell-ledger.tsv"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--require-complete",action="store_true")
    args=ap.parse_args()

    rows=[]
    with LEDGER.open(encoding="utf-8") as f:
        head=f.readline().rstrip("\n").split("\t")
        assert head==["L","status","evidence"],head
        for line in f:
            L,status,evidence=line.rstrip("\n").split("\t")
            rows.append((int(L),status,evidence))
    assert [x[0] for x in rows]==list(range(13,73))
    assert all(x[1] in {"OPEN","CLOSED"} for x in rows)
    assert len(rows)==60

    closed=[L for L,s,_ in rows if s=="CLOSED"]
    opened=[L for L,s,_ in rows if s=="OPEN"]
    assert all(e for _,s,e in rows if s=="CLOSED")

    # Permanent supporting theorem/certificate files must remain present.
    required=[
        ROOT/"notes"/"2026-09-19-math224-r10-highL-singleton-carry-shell.md",
        ROOT/"src"/"2026_09_19_math224_highL_singleton_shell.py",
        ROOT/"notes"/"2026-09-19-math249-lowL-paid-exit-oddstep-ap.md",
        ROOT/"src"/"2026_09_19_math249_lowL_paid_exit_ap_export.py",
        ROOT/"notes"/"2026-09-19-math250-lowL45-52-shell-gate.md",
        ROOT/"notes"/"2026-09-19-math256-r10-conditional-shell-aggregation.md",
    ]
    for p in required:
        assert p.exists(),p

    print("closed_count",len(closed))
    print("open_count",len(opened))
    print("closed_L",",".join(map(str,closed)))
    print("open_L",",".join(map(str,opened)))
    if args.require_complete:
        assert not opened, opened
        print("PASS MATH-259 COMPLETE r10 singleton-shell ledger")
    else:
        print("PASS MATH-259 current r10 singleton-shell ledger")
        print("r10 layer remains OPEN while any L is OPEN")

if __name__=="__main__":
    main()
