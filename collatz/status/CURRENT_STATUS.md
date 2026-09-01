# Current status — 2026-09-01

## Current branch

Research branch: `collatz-stage4-window-threshold`

Primary active object: `A0, s=1, Route-B` long-membership closure.

## Last fully reduced search family

Every current Route-B survivor belongs to the exact 14-root arithmetic forest with first threshold disagreement

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Canonical certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

This forest is a search-family representation after SAFE upstream pruning.  It is not a proof that any root realizes full membership.

## Current structural state

The following components are available as exact/local tools:

- source affine cylinder and exact bit refinement;
- finite interval payload compression;
- fixed-count ballot and target-dominance representation;
- exact dual H/L grammar;
- target-specific H/L–Stern-Brocot scale alignment;
- fixed-resolution correction/projective states;
- ternary suffix carry and displacement cylinders;
- normalized defect semiring;
- projective-cylinder exact defect floors;
- inverse physical defect budget and min-plus dominance reductions.

## Current stopping point

The next computation should operate directly on the 14 source roots using an exact family state of the form

`active source/control state × interval payload × minimum physical-risk/defect label`

and close a node whenever the certified defect/physical inequality holds for its entire source interval.

Additional predicates are to be activated lazily:

- checkpoint residue coherence;
- ternary/projective suffix constraints;
- tail first-passage constraints;
- renewal/C4F/global formation compatibility.

A predicate is not carried merely because a diagnostic coordinate exists; it is carried when the unresolved membership definition actually queries it.

## Current mathematical bottleneck

The core open question is still the long membership/nonmembership problem for the 14-root families through the complete pre bridge and required tail/checkpoint interface.

In shorthand:

`14 roots -> compressed family refinement -> certified defect accumulation -> physical closure OR unresolved membership predicate -> lazy refinement`

## What is already ruled out

Do not restart these rejected proof shortcuts:

- target adic mismatch as automatic membership rejection;
- interval inclusion as correction-language membership;
- endpoint exposure as same-orbit connectivity;
- product of marginal densities without independence;
- local carry greedy as a global defect minimizer before the cylinder sequence is fixed;
- terminal ternary saturation as an automatic contradiction with an early defect invisible at that ternary resolution.

## What has not been proved

- no global 14-root closure yet;
- no complete Route-B membership/nonmembership theorem yet;
- no Route-A completion yet;
- no all-surplus `s>=2` completion yet;
- no global Collatz proof.

## Resume instruction

When computation resumes, start from `../frontier/A0_S1_ROUTEB.md` rather than from the chronological `notes/` directory.
