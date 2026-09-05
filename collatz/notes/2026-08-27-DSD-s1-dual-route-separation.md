# DSD audit: split the s=1 program into independent and physical routes

Date: 2026-08-27

Status: **proof-control correction / SAFE dependency separation.** This note does not add a Collatz theorem; it prevents a circularity introduced by misclassifying recent physical-boundary reductions.

## 1. Why the split is necessary

The canonical `C6A` node was defined as an **independent** local `s=1` Hensel/lower-bound route. Its purpose is to obtain a local lower bound without reading the downstream near-root/reset budget, so that a later comparison is logically independent.

Recent results include:

- `2^72<Z<2^73` checkpoint exposure;
- the 40-bit renewal debit/credit corridor;
- the `28x28` mixed-radix checkpoint join;
- local 26-trit / 40-bit renewal-address exposure;
- the four-window singleton candidate reduction.

These are all valid, but the sharp versions use the **physical reset strip** supplied by the global route `C4R`.

Therefore they must not be silently inserted into the independent lower-bound node `C6A`.

## 2. Common local structure

The following remains independent of the physical reset budget:

\[
\boxed{
\text{A0 local grammar}
\to
s=1\text{ exact renewal}
\to
\text{pre }0\to0\text{ ballot bridge}
+\text{tail }0\to-1\text{ first passage}
}
\]

and the exact full-block invariant

\[
\Xi=K_R-3^qK_L.
\]

These local facts may feed either strategy.

## 3. Route A — independent lower-bound strategy

Define the independent route schematically as

\[
\boxed{
(C4F,C5)
\to S1L/S1I
\to S1H.
}
\]

`S1H` may use:

- local A0 formation grammar;
- ordering-only Bellman structure;
- exact Hensel/Xi algebra;
- finite-depth exact relaxations proved independently.

It may **not** use:

- the reset gap `<0.478G`;
- the physical defect ceiling `<0.981G`;
- checkpoint bounds derived from that reset strip;
- the physical 40-bit debit/credit corridor;
- physical boundary pruning obtained from those quantities.

Only after an independent lower result is obtained may it be compared with the physical budget.

## 4. Route B — direct physical-intersection strategy

The recent checkpoint/address work belongs instead to

\[
\boxed{
C4R+S1L/S1I
\to S1P0
\to S1P1
\to S1P2
\to S1P3
\to S1PX.
}
\]

Here the physical reset strip is part of the formation domain, so it is legitimate to use it to shrink the target state space.

The route asks directly whether

\[
\boxed{
\text{physical boundary descriptors}
\cap
\text{complete ordered/ballot extension language}
=\varnothing.
}
\]

Examples of valid Route-B descriptors are:

- bounded ordinary `Z`;
- `L_-=3X-Z`, `L_+=3Y-Z`;
- `L_+-L_-=3(Y-X)`;
- shallow mixed-radix checkpoint residues;
- the four shallow boundary windows.

Because this is a direct intersection test, using physical target information is not circular.

## 5. What Route B must not be called

A result obtained after physical target pruning must not be relabeled as an **independent local lower bound** and then compared back against the same physical target or budget.

Forbidden pattern:

\[
\boxed{
\text{physical reset data}
\to\text{pruned digital language}
\to\text{``independent'' lower bound}
\to\text{compare with physical reset data}.
}
\]

That is exactly the reverse dependency the DSD audit is intended to block.

## 6. Current status of the two routes

### Route A

**OPEN.** The finite-depth Hensel/Bellman hierarchy and ordering structure are valid, but no independent `s=1` lower theorem currently closes the branch.

### Route B

**OPEN, but structurally narrowed.** Candidate formation now passes through:

\[
\boxed{
\text{renewal}
\to73\text{-bit }Z
\to40\text{-bit }L_\pm
\to28\times28\text{ checkpoint meet}
\to37/28/28/24\text{ four-window singleton}.
}
\]

The remaining proof obligation is the **extension/join theorem**: the shallow compatible boundary descriptors must extend through the entire pre ballot bridge and tail first-passage bridge.

## 7. Relation to all-surplus coverage

Neither Route A nor Route B for `s=1` implies

\[
s\ge2
\]

coverage.

Thus even a complete `s=1` closure does not promote to `C6B` without a separate all-surplus theorem or audited partition.

## 8. DSD status

### SAFE

- dual-route separation;
- physical data allowed only in direct-intersection route;
- independent lower route remains isolated;
- no automatic `s=1 -> all-s` promotion.

### OPEN

- independent local `s=1` lower theorem;
- physical direct-intersection extension theorem;
- all-surplus coverage.

Companion machine audit:

`collatz/src/dsd_s1_dual_route_subdag_audit.py`.
