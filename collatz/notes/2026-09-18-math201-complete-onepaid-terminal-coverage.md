# MATH-201 — complete one-paid terminal coverage ledger

Date: 2026-09-18

Status: `ONE-PAID BELLMAN/ADDRESS BRANCH CLOSED / FIRST-CELL STILL OPEN`

## 1. Purpose

The one-paid program was closed in several noncontiguous stages:

- shallow Bellman/resolution wedges;
- deep phase-danger/address corridors;
- compact-carry replay;
- exact finite multi-source horizon.

One small bookkeeping hole remained: the initial one-paid catalogue contains 53 source cylinders that are already singleton at macro depth 1, but the later depth-2--20 ledgers start from the remaining 857 multi-source cylinders.

This note audits those 53 initial singletons and then assembles the complete one-paid dependency ledger.

The result closes the **one-paid Bellman/address branch** of the current first-cell program. It does not close mixed or multi-paid paths, the first universal Farey cell, or Collatz.

## 2. Initial catalogue

MATH-061/MATH-075 use exactly

[
oxed{910}
]

canonical one-paid cylinders.

They split as

[
oxed{53	ext{ singleton}+857	ext{ multi-source}.}
]

The 857 multi-source cylinders are exactly the roots used by the later one-paid depth calculations.

## 3. Exact audit of the 53 depth-1 singletons

For each initial singleton cylinder, take its exact ordinary target anchor and continue the shortcut Collatz map until it reaches the frozen published floor

[
B_{m pub}=2^{71}.
]

The exact audit gives

[
oxed{53/53	ext{ descend to }le2^{71}.}
]

After deduplicating target anchors there are

[
oxed{26}
]

unique ordinary targets.

The maximum additional shortcut descent length is

[
oxed{25}.
]

The 53 singleton cylinders are distributed by the zero-cost-prefix length `L` as

| L | singleton cylinders |
|---:|---:|
| 67 | 16 |
| 68 | 9 |
| 69 | 20 |
| 70 | 4 |
| 71 | 4 |

Total:

[
16+9+20+4+4=53.
]

Thus macro depth 1 has no unresolved singleton terminal.

## 4. Complete one-paid terminal ledger

The exact terminal coverage is now:

| one-paid macro depth | status | source |
|---:|---|---|
| 1 | CLOSED | MATH-201 direct same-integer audit of the 53 initial singleton cylinders |
| 2--3 | CLOSED | MATH-082 Bellman wedge + exact phase / two ordinary residuals |
| 4--6 | CLOSED | MATH-086 strengthened one-paid atom bound `p>1/9` |
| 7 | CLOSED | MATH-106 |
| 8 | CLOSED | MATH-105 |
| 9 | CLOSED | MATH-104 |
| 10 | CLOSED | MATH-103 |
| 11 | CLOSED | MATH-102 |
| 12 | CLOSED | MATH-101 |
| 13 | CLOSED | MATH-100 |
| 14 | CLOSED | MATH-099 |
| 15 | CLOSED | MATH-098 |
| 16 | CLOSED | MATH-097 |
| 17 | CLOSED | MATH-088 exact danger-address exclusion |
| 18--20 | CLOSED | MATH-087 exact danger-corridor closure |

MATH-086 independently proves

[
oxed{	ext{actual multi-source one-paid chain has at most 19 macros}.}
]

Equivalently, any compatible 20th one-paid macro is already singleton-resolving.

Therefore the table above covers every possible terminal layer of the canonical one-paid chain.

## 5. Exact implication

Take any canonical one-paid chain in the audited first-cell macro system.

At macro depth 1 it is either

1. one of the 53 initial singletons, now directly closed by MATH-201; or
2. one of the 857 multi-source roots.

If it remains multi-source, MATH-086 guarantees that this cannot persist beyond depth 19.

Whenever a terminal/singleton handoff occurs at depth

[
1le tle20,
]

that depth is covered by the ledger above.

Hence there is no remaining unresolved **one-paid terminal depth**.

We may therefore record

[
oxed{
	ext{canonical one-paid Bellman/address branch: CLOSED}.
}
]

This is a closure statement for the current Bellman/address branch, not an independent theorem that every represented integer has already been materialized and directly iterated.

## 6. Relation to the current r-count program

The one-paid chain depth `t` is not the MATH-065 paid-count layer `r`.

The present closure removes the repeated-`r=1` macro chain as an unresolved branch.

It does **not** imply closure of

[
r=2,ldots,21
]

mixed/multi-paid first-return layers.

MATH-185--193 instead address those layers structurally and reduce any possible Bellman deficit to singleton overshoot/address-carry obligations.

Thus after MATH-201 the proof-facing unresolved Bellman branch is concentrated on

[
oxed{
rge2	ext{ multi-paid / mixed singleton corridor}
}
]

plus the complete first-cell implication-chain audit.

## 7. Relation to MATH-200

MATH-200 shows that generic terminal Pareto records do not merge under the full MATH-096 future-address key.

That negative result does not affect the one-paid closure ledger, because the historical one-paid depth closures used exact phase/address replay and compact carry directly.

It does, however, guide the next multi-paid program:

- use equal-endpoint Hensel dominance for future-complete pruning;
- use terminal Pareto only at actual terminal comparisons;
- do not expect generic future-address collisions to provide the missing theorem.

## 8. Claim boundary

Established:

- exact audit of all 53 depth-1 singleton one-paid cylinders;
- 26 unique targets;
- maximum extra descent 25;
- complete dependency ledger for terminal depths 1--20;
- no unresolved terminal depth in the canonical one-paid Bellman/address chain.

Not established:

- closure of all mixed/multi-paid `r>=2` paths;
- first universal Farey-cell emptiness;
- later-cell coverage;
- the Collatz conjecture.
