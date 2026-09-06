# Universal first-cell root credit and the depth-195 root-safe core

Date: 2026-09-06

Status: **SAFE ROOT-MINIMALITY LEMMA relative only to the external verified floor `B0=2^71` + exact finite arithmetic certificate.**  No Ansari ternary coverage and no arbitrary later-block Hensel maximality are used.

## 1. Context

The verified-floor/Farey reduction leaves the first universal first-coefficient-crossing cell

\[
(A_0,q_0)
=
(114,208,327,604,
72,057,431,991).
\]

The buffered global co-order theorem gives `B=72`, hence any paradoxical start in this cell obeys

\[
\boxed{2^{71}<N<2^{72}}.
\]

The question is how far root-safe whole-prefix Hensel maximality can be propagated before the first crossing.

## 2. Fixed-(k,q) root credit is much smaller than the universal q=1 envelope

For a length-`k`, weight-`q` parity prefix,

\[
T^k(N)=\frac{3^qN+R(w)}{2^k}.
\]

For two words in one full-Hensel class, the positive merge credit is

\[
\Delta=\frac{R(u)-R(w)}{3^q}.
\]

The root-prefix theorem gives the fixed-`q` envelope

\[
\Delta
<
\frac{R(u)}{3^q}
\le
2^{k-q}\left(1-\left(\frac23\right)^q\right).
\]

The older universal bound `2^(k-1)/3` maximizes this over all `q>=1`.  That maximization is unnecessarily coarse before a first coefficient crossing.

## 3. Coefficient survival supplies a lower bound on q

Before the first crossing,

\[
3^{q_k}\ge2^k.
\]

Put

\[
b(k)=\min\{q:3^q\ge2^k\}.
\]

Then

\[
q_k\ge b(k).
\]

For fixed `k`, the function

\[
f_k(q)=2^{k-q}\left(1-\left(\frac23\right)^q\right)
=2^k(2^{-q}-3^{-q})
\]

is strictly decreasing for `q>=1`.  Indeed,

\[
f_k(q)-f_k(q+1)
=2^k\left(2^{-q-1}-2\,3^{-q-1}\right)>0.
\]

Therefore every coefficient-surviving root prefix satisfies

\[
\boxed{
\Delta<f_k(b(k)).
}
\]

for every possible same-class competitor.

## 4. Exact root-safe depth from B0=2^71

A hypothetical minimal counterexample has

\[
N>B_0=2^{71}.
\]

Thus full-Hensel root maximality is guaranteed whenever

\[
f_k(b(k))<B_0.
\]

The accompanying exact integer certificate evaluates this inequality without logarithms or floating point.

The transition is

\[
\boxed{
\begin{array}{c|c|c}
k&b(k)&f_k(b(k))<2^{71}\\\hline
192&122&\text{yes}\\
193&122&\text{yes}\\
194&123&\text{yes}\\
195&124&\text{yes}\\
196&124&\text{no}\\
197&125&\text{no}
\end{array}}
\]

Hence

\[
\boxed{K_{\rm root-safe}=195.}
\]

For every hypothetical minimal counterexample in the first universal cell, every root prefix through depth 195 must therefore be a maximum-correction representative of its **full** Hensel class.

This is much stronger than the previous q-independent 72--73 bit estimate.

## 5. Same-integer consequence

Because the buffered first-cell bound gives

\[
N<2^{72}<2^{195},
\]

the canonical residue modulo `2^195` of the actual 195-bit parity prefix is not merely a congruence class: it must equal the ordinary start `N` itself.

Therefore the first universal cell reduces to the finite root-global intersection problem

\[
\boxed{
\mathcal R_{195}^{\rm coeff\,+\,nested\ root\text{-}Hensel\ max}
\cap
(2^{71},2^{72})
}
\]

followed by the deterministic requirement that the resulting integer actually reaches the specified first-crossing cell `(A0,q0)`.

No mass-to-emptiness inference is made here.  The target is an exact finite set of ordinary canonical residues.

## 6. Whole-first-crossing admissible-class maximality

There is a separate root-safe statement at the enormous terminal depth `A0`.

For a first-crossing-admissible word, write

\[
S(w)=\frac{R(w)}{3^{q_0}}.
\]

The elementary mechanical pair bound gives

\[
S(w)\le S^*(q_0)\le\frac{7q_0+1}{24}.
\]

Exact integer arithmetic verifies

\[
\boxed{7q_0+1<24B_0.}
\]

Hence if another **first-crossing-admissible** word `u` lies in the same full-Hensel class and has `R(u)>R(w)`, then

\[
0<\Delta
=\frac{R(u)-R(w)}{3^{q_0}}
<S(u)
<B_0<N.
\]

Root minimality would then force a contradiction.  Therefore the actual first-crossing word must satisfy

\[
\boxed{
R(w)=\max\{R(u):u\text{ is first-crossing admissible and }R(u)\equiv R(w)\pmod{3^{q_0}}\}.
}
\]

This is a **SAFE constrained root-class maximality lemma**.  It is not the withdrawn claim that arbitrary later 7-bit blocks are Hensel-maximal.

## 7. Finite diagnostic / caution

Small exact first-crossing enumerations through time depth 29 found no Hensel collisions inside the terminal first-crossing-admissible family.  Thus the constrained terminal-class maximality may be weak or even vacuous unless a structural collision theorem is found.

This finite observation is diagnostic only.  It is not extrapolated to the giant cell.

The depth-195 nested root-max condition is currently the stronger concrete finite target.

## 8. Reproducibility

Source:

`collatz/src/universal_first_cell_root_credit_certificate.py`

Expected output:

```text
PASS
root-safe coefficient-surviving depth = 195
first envelope failure = (196, 124)
first-cell admissible-class credit bound < B0
```

## 9. DSD audit status

### SAFE

- fixed-(k,q) credit envelope;
- monotonic decrease of that envelope in `q`;
- coefficient-survival substitution `q>=b(k)`;
- root-safe maximality through depth 195;
- same-integer reduction because `N<2^72`;
- constrained whole-first-crossing admissible-class maximality.

### FINITE DIAGNOSTIC ONLY

- no terminal admissible Hensel collision observed through depth 29.

### OPEN

Construct an exact compressed transfer for

\[
\mathcal R_{195}^{\rm coeff+nested\ root\text{-}max}
\cap(2^{71},2^{72}),
\]

or derive a symbolic reason that this intersection is empty.  A brute-force extrapolation of the depth-22 root-max survivor exponent is not permitted.
