#!/usr/bin/env python3
"""MATH-258 exact set-equality regression for the MATH-249 transform at L=54."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent

def load(name,path):
    spec=spec_from_file_location(name,HERE/path)
    mod=module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

m224=load("m224","2026_09_19_math224_highL_singleton_shell.py")
m249=load("m249","2026_09_19_math249_lowL_paid_exit_ap_export.py")

L=54

def shortcut(n):
    return n//2 if n%2==0 else (3*n+1)//2

def main():
    ys=m224.anchors(L)
    assert len(ys)==96_611

    direct=set()
    for y in ys:
        x=y
        for _ in range(L):
            x=shortcut(x)
        assert x&1
        x=shortcut(x)  # opening paid odd
        direct.add(x)

    rows=m249.rows_for_L(L)
    ap=set()
    mass=0
    for a,b,m in rows:
        mass+=m
        for j in range(m):
            ap.add(a+b*j)

    assert direct==ap
    assert mass>=len(ap)
    print("L",L)
    print("explicit_source_anchors",len(ys))
    print("direct_post_opening_states",len(direct))
    print("ap_rows",len(rows))
    print("ap_raw_mass",mass)
    print("ap_unique_states",len(ap))
    print("PASS MATH-258 MATH-249 exact-set regression at L54")

if __name__=="__main__":
    main()
