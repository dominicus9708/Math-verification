# MATH-040 — one-sided root-Hensel selection correction

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / SELECTION-SCOPE CORRECTION / FIRST ONE-SIDED HENSEL PRUNING AT DEPTH 6 / FINITE EXACT`

## 1. Scope correction

MATH-037–039 studied **two-sided coefficient-language collisions**: both members of a Hensel class collision were required to satisfy the frozen published-floor coefficient-survival condition.

That is a valid finite subproblem, but it is not the full root-Hensel maximality test.

For a hypothetical minimal-counterexample prefix `w`, the correct asymmetric selection is

\[
\boxed{w\in\mathcal L_{\rm coeff},\qquad u\in\mathcal L_{\rm arbitrary}.}
\]

The actual candidate prefix must satisfy coefficient survival.  A competing prefix `u` only needs to be an arbitrary parity word of the same length and odd count in the same Hensel correction class, together with a legal positive ordinary-start credit.

Therefore the old phrase “first non-vacuous Hensel pruning at depth 34” is withdrawn.  MATH-037 is retained as the **first two-sided coefficient-language Hensel collision**.

## 2. Exact one-sided criterion

For a length-`k`, odd-count-`q` prefix with correction

\[
C=h3^q+r,\qquad 0\le r<3^q,
\]

define the unrestricted class maximum

\[
M_k(q,r)=\max_{u\in\mathcal L_{\rm arbitrary}(k,q,r)}\left\lfloor\frac{C(u)}{3^q}\right\rfloor.
\]

The candidate is root-Hensel maximal at that prefix only if

\[
h=M_k(q,r).
\]

If

\[
M_k(q,r)-h=d>0,
\]

then

\[
C(u)-C(w)=d3^q
\]

and hence

\[
T_u^k(N-d)=T_w^k(N).
\]

Whenever `0<d<N`, minimality excludes the lower-correction candidate prefix.

## 3. First exact pruning event

The one-sided audit is empty through depth 5 and first becomes non-vacuous at

\[
\boxed{k=6}.
\]

The candidate has

\[
q=4,\qquad C=65,
\]

while the unrestricted maximum in the same class is

\[
C_{\max}=146.
\]

Since

\[
146-65=81=3^4,
\]

the credit is exactly

\[
\boxed{d=1}.
\]

The candidate ordinary-start residue is

\[
\boxed{N\equiv15\pmod{64}},
\]

and the competing start is exactly one smaller,

\[
N-1\equiv14\pmod{64}.
\]

Thus every first-cell candidate with low six bits `001111` is excluded by root minimality.

## 4. First-cell ordinary-start consequence

The current first-cell start window contains

\[
340\cdot2^{61}-1
\]

positive ordinary starts.  Because both window endpoints are multiples of `64`, every nonzero residue modulo `64` occurs exactly

\[
340\cdot2^{55}
=\boxed{12{,}249{,}790{,}986{,}447{,}749{,}120}
\]

times.

Therefore MATH-040 already removes that many ordinary starts from the present first-cell window via the single residue class

\[
N\equiv15\pmod{64}.
\]

This is finite exact pruning, not a density theorem and not first-cell emptiness.

## 5. Per-depth direct one-sided audit

The certificate compares every coefficient-surviving candidate prefix with the unrestricted class maximum through depth 26.

Selected rows:

| depth | coefficient candidates | one-sided dominated | max credit |
|---:|---:|---:|---:|
| 5 | 4 | 0 | 0 |
| 6 | 8 | 1 | 1 |
| 10 | 64 | 12 | 1 |
| 16 | 2,114 | 394 | 1 |
| 18 | 7,495 | 1,391 | 3 |
| 20 | 27,328 | 5,084 | 7 |
| 24 | 286,581 | 52,425 | 7 |
| 25 | 573,162 | 105,267 | 15 |
| 26 | 1,037,374 | 189,881 | 15 |

These are per-depth direct comparisons; the dominated sets overlap across depths.  They must not be summed as independent ordinary-start exclusions.

## 6. Exact targeted reverse-Hensel oracle

The certificate does not need to materialize every arbitrary Hensel class.

If the odd positions of a word are

\[
p_1<\cdots<p_q<k,
\]

then

\[
C=3C_{q-1}+2^{p_q}.
\]

For a queried residue `r mod 3^q`, a possible last odd position must satisfy

\[
2^{p_q}\equiv r\pmod3,
\]

and the previous class residue is

\[
\boxed{
r_{q-1}\equiv\frac{r-2^{p_q}}3\pmod{3^{q-1}}.
}
\]

Recursing over the admissible decreasing odd positions enumerates exactly the words in the queried Hensel class and returns its maximum correction.

This targeted oracle reproduces the one-sided counts above without building the entire unrestricted class table.

## 7. DSD interpretation

- `D`: candidate language and competitor language are explicitly separated.
- `R`: exact parity/correction class resolution; no coarse phase replacement.
- `S`: candidate is coefficient-surviving; competitor is arbitrary.
- `E`: candidate is excluded only when a strictly larger class correction yields a legal positive start credit.
- `T`: correction difference is translated back to the exact ordinary-start relation.
- `C`: first event `(k,q,C,Cmax)=(6,4,65,146)` and complete depth-1–26 counts are exact-regressed.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.
- `O`: MATH-037’s “first Hensel pruning” interpretation is superseded; one-sided Hensel pruning starts at depth 6.

## 8. Prohibited upgrades

- one-sided pruning at depth 6 ⇒ first cell empty — **PROHIBITED**;
- dominated count at different depths ⇒ independent exclusions that may be summed — **PROHIBITED**;
- arbitrary competitor ⇒ competitor must also satisfy coefficient survival — **PROHIBITED**;
- two-sided collision absence ⇒ Hensel maximality is vacuous — **PROHIBITED**;
- finite depth-26 audit ⇒ depth-195 theorem — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_one_sided_root_hensel_selection_correction_certificate.cpp`

Certificate commit:

`487adff3f3451fd549b6168571ff8f66d75cc40d`

MATH-037–039 remain valid as two-sided coefficient-language event records, but not as the global first-pruning frontier.
