# First universal cell — Denjoy–Koksma/Ostrowski sharpened start cap

Date: 2026-09-07

Status: **SAFE POSITIVE REDUCTION + SAFE SCALAR-BARRIER SHARPENING.**

This note replaces the earlier 1024-block rotation envelope by an audited Denjoy–Koksma/Ostrowski bound at the exact first-cell odd count. It removes one additional top-11-bit root-address block and simultaneously identifies the exact block-resolution limit of any word-independent scalar correction-max argument.

No Collatz proof is claimed.

---

## 1. First universal cell

The current first coefficient-crossing cell is

\[
(A_0,q_0)
=(114,208,327,604,
72,057,431,991),
\]

with external published verification floor

\[
B_0=2^{71}.
\]

The previous exact 1024-block rotation certificate gave

\[
2^{71}<N<\frac{1365}{1024}2^{71}
=1365\cdot2^{61},
\]

leaving 341 top-11-bit blocks

\[
a=1024,\ldots,1364.
\]

---

## 2. Mechanical correction rotation sum

For the latest admissible mechanical word,

\[
S_*
=\frac13\sum_{n=0}^{q_0-1}2^{-\{n\theta\}},
\qquad
\theta=\log_2(3/2).
\]

The mechanical word is an actual first-crossing-admissible word and termwise maximizes the correction among first-crossing words.

Thus every first-crossing word satisfies

\[
S(w)\le S_*.
\]

---

## 3. Audited Denjoy–Koksma/Ostrowski input

For the periodic BV observable

\[
f(x)=2^{-\{x\}},
\]

we have

\[
\operatorname{Var}(f)=1,
\qquad
\int_0^1 f(x)\,dx=\frac1{2\ln2}.
\]

The exact continued-fraction prefix for

\[
\theta=\log_2(3/2)
\]

contains consecutive convergent denominators

\[
q_{21}=6,586,818,670,
\]

\[
q_{22}=65,470,613,321,
\]

\[
q_{23}=137,528,045,312.
\]

The first-cell odd count has the exceptional two-digit Ostrowski expansion

\[
\boxed{
q_0=q_{22}+q_{21}.
}
\]

Therefore the sum of Ostrowski digits is exactly `2`.

The audited Denjoy–Koksma/Ostrowski theorem gives, for every phase `x`,

\[
\boxed{
\left|
\sum_{n=0}^{q_0-1}2^{-\{x+n\theta\}}
-\frac{q_0}{2\ln2}
\right|
\le2.
}
\]

At the mechanical phase `x=0`,

\[
\boxed{
\frac{q_0}{6\ln2}-\frac23
\le S_*
\le
\frac{q_0}{6\ln2}+\frac23.
}
\]

This is dramatically sharper than accumulating an independent 1024-block maximum over roughly seventy million blocks.

---

## 4. New universal start cap

Put

\[
\delta=A_0\ln2-q_0\ln3,
\qquad
\varepsilon=e^\delta-1.
\]

The exact rational-log certificate proves

\[
\frac{q_0}{6\ln2}+\frac23
<
\varepsilon\frac{1364}{1024}B_0.
\]

Since every first-crossing word has `S(w)<=S_*`, any start satisfying

\[
N\ge\frac{1364}{1024}B_0
\]

has

\[
S(w)<\varepsilon N,
\]

so the first coefficient crossing is an actual descent and cannot belong to a minimal-counterexample trajectory.

Hence

\[
\boxed{
2^{71}<N<\frac{1364}{1024}2^{71}
=1364\cdot2^{61}.
}
\]

At resolution `2^61`, the surviving blocks are therefore

\[
\boxed{
a=1024,1025,\ldots,1363,
}
\]

exactly

\[
\boxed{340\text{ top-11-bit blocks}.}
\]

The previously surviving block `a=1364` is closed.

---

## 5. Exact scalar-correction barrier at the next block

The same theorem gives the lower bound

\[
S_*
\ge
\frac{q_0}{6\ln2}-\frac23.
\]

The exact certificate also proves

\[
\boxed{
\frac{q_0}{6\ln2}-\frac23
>
\varepsilon\frac{1363}{1024}B_0.
}
\]

The explicit mechanical word is first-crossing admissible, so its scalar correction capacity is already sufficient at the lower boundary of block `a=1363`.

Therefore any argument of the form

\[
S(w)\le\text{word-independent scalar maximum}
\]

cannot eliminate all starts in block `1363`, because that maximum must be at least `S_*`.

Thus at `2^61` address resolution,

\[
\boxed{
340\text{ blocks is the exact frontier of the scalar correction-max route}.}
\]

This does **not** assert the existence of a positive-integer candidate in block `1363`; the mechanical word's canonical dyadic address may lie elsewhere. It states only that scalar capacity no longer supplies the missing contradiction.

---

## 6. Consequence for the proof architecture

The source-side problem is now

\[
340\text{ root address blocks}
\longrightarrow
\text{same-integer extension constraints}.
\]

The next elimination step must retain at least two channels simultaneously:

### Address channel

At depth 72,

\[
n_{72}(w)
\equiv-R_{72}(w)3^{-q_{72}}
\pmod{2^{72}}.
\]

Because every remaining candidate satisfies `N<2^72`, this residue is the ordinary integer itself.

### Correction channel

At the giant first crossing,

\[
S(w)=R(w)/3^{q_0}
\]

must satisfy

\[
S(w)\ge\varepsilon N.
\]

### Joint target

For each remaining block

\[
I_a=[a2^{61},(a+1)2^{61}),
\qquad a=1024,\ldots,1363,
\]

show that no one nested word can simultaneously

1. have `n_72(w)` in `I_a`;
2. satisfy coefficient survival and the verified-floor prefix constraints;
3. satisfy root-Hensel maximality through depth 195;
4. first cross at `(A0,q0)`;
5. retain terminal correction `S(w)>=epsilon*n_72(w)`.

This is now the canonical U1 target.

---

## 7. DSD audit

### CLOSED / SAFE

1. Denjoy–Koksma at convergent times is valid for the BV observable used here.
2. Ostrowski decomposition gives the arbitrary-time error bound without independence assumptions.
3. `theta=log_2(3/2)` is irrational.
4. the required continued-fraction cylinder is certified with rational logarithm intervals.
5. `q0=q22+q21` and the Ostrowski digit sum is exactly `2`.
6. the rotation sum differs from its mean by at most `2`.
7. `N < (1364/1024)B0` is certified exactly.
8. block `1364` is eliminated.
9. the scalar lower bound at block `1363` certifies that correction-only pruning has reached its block-resolution frontier.

### OPEN

1. 340 same-integer address blocks remain.
2. address/root-Hensel/terminal-correction coupling remains open.
3. later Farey cells remain open after the first cell.
4. the genuinely aperiodic coefficient-survival branch remains open.

### PROHIBITED UPGRADES

1. Do not treat the mechanical word as an ordinary positive counterexample.
2. Do not infer emptiness of the 340 blocks from their reduced proportion.
3. Do not use the Denjoy–Koksma average as a parity-independence theorem.
4. Do not continue trying to remove block `1363` by a word-independent scalar correction maximum; the lower certificate proves that strategy insufficient.

---

## 8. Reproducibility

External theorem audit:

`collatz/notes/2026-09-07-external-denjoy-koksma-ostrowski-audit.md`

Arithmetic certificate:

`collatz/src/first_universal_cell_denjoy_koksma_start_cap_certificate.py`

Expected terminal output:

```text
PASS
theta CF denominators q21,q22,q23 = 6586818670 65470613321 137528045312
Q0 = q22 + q21; Ostrowski digit sum = 2
Denjoy-Koksma rotation error <= 2; normalized correction error <= 2/3
new start cap: N < (1364/1024)*2^71 = 1364*2^61
remaining top-11-bit blocks = 340 (1024..1363)
scalar correction-only barrier already active at block 1363
```

---

## 9. Next calculation

The scalar route is now intentionally stopped.

The next calculation should preserve the actual `72`-bit ordinary start and classify the remaining root-Hensel-maximal prefixes by their high address block `a`. A useful compression must be proved address-faithful; no grouping of the 340 blocks is permitted merely from similar correction totals or similar low-depth parity statistics.
