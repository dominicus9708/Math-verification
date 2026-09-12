# MATH-087 — exact one-paid danger-corridor closure at macro depths 18--20

Date: 2026-09-12

Status: `EXACT FINITE BELLMAN CLOSURE AT DEPTHS 18,19,20 / DEPTHS 7--17 STILL OPEN`

The first universal cell and the Collatz conjecture remain open.

## 1. Why the calculation is no longer a raw depth search

MATH-086 constructs an address-forgotten phase language that contains every actual same-integer one-paid chain.  At a fixed target macro depth, every phase-only terminal crossing whose lower-envelope Bellman margin is nonnegative is automatically safe for every actual address realization beneath it.

Only phase-only cells whose lower-envelope margin is negative need exact dyadic address restored.

Therefore MATH-087 uses the hierarchy

\[
\text{phase over-approximation}
\to
\text{negative lower-envelope cells}
\to
\text{backward phase corridor}
\to
\text{exact dyadic address replay}.
\]

No phase-negative cell is discarded merely for being negative.

## 2. Depth 20

At macro depth 20, the phase-only lower envelope has only seven negative terminal-crossing cells.

Backward phase reachability reduces these to a very small corridor.  After restoring exact dyadic address, the numbers of exact multi-source states along depths 1--19 are

\[
1,3,5,6,12,16,28,44,48,88,112,144,224,224,352,448,576,896,34.
\]

The final 34 exact parents generate exactly

\[
\boxed{12}
\]

address-compatible singleton terminal children.

All 12 have positive exact current-phase Bellman margin.  The minimum margin is approximately

\[
\boxed{2.6101>0}.
\]

Thus macro depth 20 is Bellman-safe.

## 3. Depth 19

At depth 19 the phase-only negative lower-envelope set is larger, but backward reachability still strongly compresses the exact address calculation.

The exact corridor state counts through depths 1--18 are

\[
10,22,37,78,134,256,408,528,964,1400,2336,3616,4368,7648,10400,16256,24960,6291.
\]

The 6,291 exact depth-18 parents generate

\[
\boxed{2,816}
\]

singleton terminal children.

Every child has positive Bellman margin; the minimum is approximately

\[
\boxed{2.1052>0}.
\]

Thus macro depth 19 is Bellman-safe.

## 4. Depth 18

The exact address corridor counts through depths 1--17 are

\[
20,59,169,357,811,1477,2216,4382,7264,13392,21640,28608,52112,78080,131376,206480,91437.
\]

The final 91,437 exact parents generate

\[
\boxed{50,133}
\]

singleton terminal children.

Again every terminal child has positive Bellman margin.  The minimum is approximately

\[
\boxed{1.9565>0}.
\]

Thus macro depth 18 is Bellman-safe.

## 5. Current one-paid Bellman coverage

Previously established:

- macro depth 2: all terminal handoffs safe after universal/exact-phase/ordinary residual audit;
- macro depth 3: same, with only two ordinary residual trajectories;
- macro depths 4--6: all terminal handoffs safe, now also covered by the stronger `p>1/9` wedge from MATH-086.

MATH-087 adds

\[
\boxed{18,19,20\text{ CLOSED}.}
\]

MATH-086 proves that no actual multi-source one-paid chain can persist beyond depth 19, so depth 20 is the last possible source-resolution layer.

The detailed one-paid Bellman frontier is therefore now

\[
\boxed{7\le t\le17}.
\]

No claim is made here about those eleven intermediate macro depths.

## 6. DSD interpretation

The result demonstrates that the correct state hierarchy is not raw ordinary integers and not phase alone.

The efficient exact hierarchy is

\[
\text{coarse analytic lower bound}
\to
\text{phase danger geometry}
\to
\text{address compatibility only where needed}.
\]

This preserves same-integer lineage while avoiding exhaustive exact-address expansion in regions already certified safe by the phase lower envelope.

## 7. Claim boundaries

Do not infer:

- closure of depths 18--20 `=>` closure of depths 7--17;
- phase-over-approximate positivity `=>` phase determines address;
- Bellman-safe terminal `=>` an independent ordinary-descent theorem;
- one-paid Bellman closure `=>` all paid-count/mixed paths are closed;
- first-cell closure or Collatz.

## Reproducibility

Run separately for each target to avoid unnecessary peak memory:

```text
python collatz/src/2026_09_12_math087_onepaid_danger_corridor_18_20.py --target 18
python collatz/src/2026_09_12_math087_onepaid_danger_corridor_18_20.py --target 19
python collatz/src/2026_09_12_math087_onepaid_danger_corridor_18_20.py --target 20
```

Certificate:

`collatz/src/2026_09_12_math087_onepaid_danger_corridor_18_20.py`
