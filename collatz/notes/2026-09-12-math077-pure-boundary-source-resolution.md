# MATH-077 — exact source resolution of the pure coefficient-boundary path

Date: 2026-09-12

Status: `EXACT PURE-BOUNDARY ELIMINATION / MIXED PATHS OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note removes only the path that never takes an odd shortcut at positive slack.

## 1. Pure boundary policy

Start at

\[
q=d=0,\qquad u=0.
\]

Define the deterministic zero-paid policy:

1. if `u=0`, take the odd shortcut;
2. if the corresponding mechanical increment `epsilon=1` raises `u` to `1`, take one even shortcut immediately to return to `u=0`;
3. never take an odd shortcut at `u>=1`.

Thus this path remains on the coefficient boundary whenever it is at a boundary anchor and accumulates zero paid penalty.

## 2. Exact parity cylinder

For the length-k pure-boundary word let `(q,C)` be its exact odd count and correction. The source integer must satisfy

\[
3^qN+C\equiv0\pmod{2^k},
\]

hence

\[
\boxed{
N\equiv-C3^{-q}\pmod{2^k}.
}
\]

The audited first-cell source window is the strict interval

\[
\boxed{2^{71}<N<1364\cdot2^{61}.}
\]

Therefore the number of ordinary source anchors in the exact residue class is obtained without density or random-parity assumptions by direct arithmetic progression counting.

## 3. Exact source counts near resolution

The certificate gives:

| depth k | source anchors |
|---:|---:|
| 65 | 21 |
| 66 | 10 |
| 67 | 5 |
| 68 | 2 |
| 69 | 1 |
| 70 | 0 |

The residue cylinders are nested exactly: the depth `k+1` residue reduces to the depth-k residue modulo `2^k`.

Hence

\[
\boxed{
\text{the pure zero-paid coefficient-boundary path is empty by depth }70
}
\]

inside the first-cell source window.

At depth 69 exactly one ordinary source anchor remains; its required next pure-boundary parity bit is incompatible with that integer, so the depth-70 cylinder is empty.

## 4. Relation to MATH-058/059

MATH-058/059 found the same resolution scale from the macro side:

- a 69-step zero-cost prefix can still reach a one-paid continuation;
- the L=69 family contains a unique continuation capable of reaching another paid macro;
- L=70 and L=71 one-paid outcomes exist but do not reach another paid macro;
- the zero-cost/pure-boundary source family cannot continue indefinitely.

MATH-077 supplies the direct dyadic-address version of that phenomenon without first taking a paid exit.

## 5. Bellman interpretation

MATH-075 shows that the only negative unit edges under the slack potential are free odd edges at `u=0`.

MATH-077 proves that a path consisting exclusively of those free-boundary choices cannot persist beyond 69 compatible shortcut bits in the audited source window.

Thus the remaining negative language must intermittently leave the boundary and enter a positive-slack excursion.

By MATH-075 every such positive-slack excursion is internally Bellman-safe. Therefore the hard case is not a permanently free boundary path, but a mixed aperiodic sequence

\[
\boxed{
\text{boundary run}\to\text{positive-slack excursion}\to\text{boundary run}\to\cdots
}
\]

subject to exact same-integer address compatibility.

## 6. DSD boundary

Established:

- exact deterministic pure-boundary parity word;
- exact source residue at every depth;
- exact source counts in the first-cell window;
- source multiplicity `2 -> 1 -> 0` at depths `68 -> 69 -> 70`;
- elimination of the purely zero-paid boundary path.

Not established:

- elimination of mixed boundary/paid paths;
- a universal 70-step bound after arbitrary paid excursions;
- post-singleton Bellman closure;
- first-cell emptiness;
- Collatz.

## 7. Next target

Use the exact one-paid composition law of MATH-061 to study mixed paths while applying:

- MATH-075 positive-slack Bellman safety;
- MATH-076 pre-singleton debt bound;
- MATH-074/MATH-052 Hensel comparison quotients;
- immediate singleton handoff when the exact source cylinder collapses.

## Reproducibility

`collatz/src/2026_09_12_math077_pure_boundary_source_resolution.py`
