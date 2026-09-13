# MATH-131 — r=11 complete-cycle parity-word dynamic program

Status: `MAINLINE FINITE AUDIT / EXACT LOWER BOUND / r=11 OPEN`

Date: 2026-09-14

## Purpose

MATH-129 exactly counted the union of all MATH-125 floor-safe prefix gates through depth 22 over the complete prepared r=11 source, including cyclic remainders. MATH-130 then showed that depth 23 adds a further exact safe subset when complete `2^23` parameter blocks are counted and incomplete remainders are conservatively ignored.

MATH-131 generalizes that complete-block extension through every depth still supported by at least one full parameter cycle in the prepared source.

## Parity-word bijection

For the shortcut Collatz map, MATH-124 gives an exact bijection between length-`D` parity words and source residues modulo `2^D`. Since every prepared AP has odd step `b`, the parameter map

```text
k -> a + b k (mod 2^D)
```

is also a permutation modulo `2^D`.

Therefore every complete `2^D` parameter block of an AP contains every length-`D` parity word exactly once. Complete-block safe counts can be computed on parity words without enumerating ordinary source residues.

## Exact DP state

For a parity prefix of length `d`, let `q_d` be its odd-step count and define the MATH-125 source-maximum gate

```text
L(d,q) = floor((2^d * 2^71 - c_max(d,q))/3^q),
c_max(d,q) = 2^(d-q) * (3^q - 2^q).
```

For one parity word, define

```text
B_d = max_{1<=j<=d} L(j,q_j).
```

A word is newly certified at depth `D` for source maximum `N` exactly when

```text
B_{D-1} < N <= L(D,q_D).
```

Thus the complete-block counting state is only

```text
(q, B)
```

with an integer multiplicity equal to the number of parity words producing that state. Appending even/odd parity updates `q` and `B` exactly. This replaces an explicit `2^D` residue scan by a small exact dynamic program.

## Regression to MATH-130

At `D=23`, the DP gives the additional complete-block safe mass

```text
3,151,665,357
```

which exactly reproduces MATH-130. This is the regression gate for the generalized DP.

## Exact new safe mass by depth

Relative to every earlier prefix gate, the pairwise-disjoint new complete-block contributions are:

```text
D=23   3,151,665,357
D=24  17,456,818,136
D=25  15,350,900,431
D=26   5,512,456,558
D=27  13,125,146,222
D=28   5,153,825,838
D=29   5,433,928,840
D=30   6,978,119,195
D=31     561,706,378
D=32   2,728,613,739
D=33   1,501,750,221
D=34     126,980,183
```

Total additional certified mass from complete cycles at depths 23 through 34:

```text
77,081,911,098
```

Combining this with the exact MATH-129 depth-22 union

```text
3,209,065,424,947
```

gives the conservative exact lower bound

```text
certified safe mass >= 3,286,147,336,045
uncertified tail   <=   133,571,725,515
safe fraction      >= 96.094073135526301%
```

## Why the complete-cycle extension stops at D=34

The prepared MATH-114/MATH-115 representation has maximum piece multiplicity

```text
26,716,555,169.
```

Since

```text
2^34 <= 26,716,555,169 < 2^35,
```

no prepared AP piece contains a complete `2^35` parameter block. Therefore MATH-131 exhausts the **complete-cycle-only** extension. Any further gain must count incomplete cyclic remainders with exact address information, or use the unchanged MATH-108 AP-union engine.

## Claim boundary

The remaining `133,571,725,515` occurrences are not counterexamples. They are only the part not certified by the MATH-125 envelope under the exact depth-22 union plus conservative complete-cycle innovations through depth 34.

MATH-131 does not close `r=11`. The certified multi-paid frontier remains

```text
r>=12 CLOSED
r=11 OPEN
```

until MATH-116 completes or an equivalent exact certificate discharges the remaining tail.
