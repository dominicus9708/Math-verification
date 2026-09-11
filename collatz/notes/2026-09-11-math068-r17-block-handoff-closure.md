# MATH-068 — complete closure of the r=17 layer by exact 8-step block handoff

Date: 2026-09-11

Status: `EXACT r=17 CLOSURE / r>=17 CLOSED / 2<=r<=16 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-065 closes every multi-paid layer `r>=18`.
- MATH-067 leaves only the `r=17` medium-multiplicity core `65<=m<=1023`.

## 1. Remaining workload

The exact MATH-067 core contains

\[
\boxed{76,866}
\]

negative-candidate arithmetic-progression cylinders representing

\[
\boxed{14,980,075}
\]

ordinary target occurrences.

The endpoint coefficients are only

\[
3^{38},\quad3^{39},\quad3^{40},
\]

with cylinder counts

\[
8,268,\quad19,445,\quad49,153.
\]

At 8-bit resolution the starting affine classes `(a mod256,b mod256)` collapse to only

\[
\boxed{768}
\]

classes.

## 2. Universal 8-step shortcut block

For each residue

\[
r=n\pmod{256},
\]

the next eight shortcut parities are fixed, hence

\[
\boxed{
T^8(n)=\frac{3^{q(r)}n+C(r)}{256}.
}
\]

Now let one exact target cylinder be

\[
P=\{a+bk:0\le k<m\},
\qquad b\text{ odd}.
\]

For a fixed residue `k0 mod256`, write

\[
k=k_0+256s.
\]

Then `n mod256` is fixed because `b` is odd, and therefore

\[
\boxed{
T^8(a+b(k_0+256s))
=a'+3^{q}b\,s.
}
\]

Thus an 8-step block maps each residue slice of an AP to another exact AP.
No ordinary integer is lost and no density argument is used.

## 3. First block

Applying the exact block to all 76,866 medium-core cylinders gives

\[
\boxed{9,587,872}
\]

target occurrences already at or below the frozen floor

\[
2^{71}.
\]

The remaining multiplicity is

\[
\boxed{5,392,203}.
\]

Crucially, after this one block every surviving AP has multiplicity at most

\[
\boxed{4}.
\]

So the formerly medium-size family problem has already collapsed to tiny families.

## 4. Second block and singleton handoff

Applying the same exact 8-step block once more closes another

\[
\boxed{2,777,528}
\]

occurrences.

Exactly

\[
\boxed{2,614,675}
\]

occurrences remain.
Every surviving family now has multiplicity exactly one.

After removing duplicates these represent

\[
\boxed{1,826,810}
\]

ordinary integers.

This is a valid resolution handoff:

\[
\boxed{
65\le m\le1023
\xrightarrow{16\text{ exact shortcut steps}}
\text{ordinary singleton set}.
}
\]

## 5. Same-integer terminal audit

Every one of the 1,826,810 unique singleton states was continued under the ordinary shortcut Collatz map with exact integer arithmetic and memoization.

All reach

\[
\le2^{71}.
\]

The maximum additional distance after the 16-step handoff is

\[
\boxed{318}
\]

shortcut steps.

Therefore a safe bound measured from the original medium-core target is

\[
\boxed{334}
\]

additional shortcut steps.

Hence the last MATH-067 open core is closed.

## 6. r=17 verdict

Combining MATH-067 and the present block audit:

- `m<=64`: already closed by ordinary same-integer continuation;
- `65<=m<=1023`: closed here by two exact 8-step AP blocks plus singleton continuation;
- `m>=1024`: already closed by MATH-066 AP-family continuation.

Therefore

\[
\boxed{r=17\text{ is completely closed}.}
\]

Together with MATH-065,

\[
\boxed{r\ge17\text{ is closed}.}
\]

The remaining detailed multi-paid frontier is

\[
\boxed{2\le r\le16.}
\]

## 7. DSD audit

### SAFE

1. The 8-step parity word depends only on `n mod256`.
2. Because the AP step is odd, `k mod256` and `n mod256` are in bijection.
3. Every residue slice remains an exact AP after eight shortcut steps.
4. Floor trimming removes only an initial AP segment whose values are already `<=2^71`.
5. After two blocks all unresolved families are singleton.
6. Singleton duplicate removal is safe because subsequent dynamics depend only on the ordinary integer state.
7. Every unique singleton is explicitly continued to the frozen floor.

### OPEN

- `2<=r<=16` multi-paid layers;
- mixed one-paid / remaining multi-paid Bellman problem;
- first universal Farey cell emptiness;
- later strip cells;
- full Collatz conjecture.

### PROHIBITED UPGRADES

- `r>=17` closure `=>` all multi-paid macros are closed;
- finite `r=17` block closure `=>` a universal descent theorem;
- first-cell paid-count pruning `=>` first-cell emptiness.

## 8. Methodological consequence

The useful state-resolution lesson is stronger than the raw multiplicity heuristic from MATH-067.
A medium AP need not be followed as a long binary tree. A short universal low-bit block can first reduce its family size sharply, after which an ordinary singleton handoff becomes cheap.

This suggests the next layers should try block handoff early rather than waiting until multiplicity becomes very large.

## Reproducibility

`collatz/src/2026_09_11_math068_r17_block_handoff_closure_certificate.py`
