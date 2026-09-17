# MATH-180 — joint paid-count first-return transducer

Date: 2026-09-17

Status: `EXACT RECURRENCE DESIGN / PROOF-PRESERVING COMPRESSION / NO NEW CLOSURE CLAIM`

This note continues MATH-179. The aim is to remove the target-`r` outer loop from the MATH-065/115 paid-layer calculation and replace it by one exact first-return tree carrying every paid-count layer `1<=r<=21` at once.

## 1. Fixed common phase cell

Take one paid-exit source

\[
(L,R,E_0,q_0,I_0),
\qquad I_0=(\omega_-,\omega_+).
\]

Refine `I_0` once by all exact future phase cuts

\[
\tau_{q_0+1},\ldots,\tau_{q_0+21}.
\]

On each resulting cell the full future epsilon word through paid count 21 is fixed.

Let `varpi` denote the normalized entry phase on such a cell. By MATH-179,

\[
E_j(\varpi)=m(j)+\mathbf 1_{\{\varpi\le\tau_j\}},
\]

\[
\varepsilon_j=E_{j+1}(\varpi)-E_j(\varpi),
\]

and the first-return local length for terminal paid count `r` is

\[
\boxed{h_r=r+1+E_r(\varpi).}
\]

No target-specific phase recursion is required.

## 2. Exact affine address state

At local step depth `h` after exactly `j` paid odds, write the surviving source parameter and endpoint as

\[
\boxed{
t=a+2^h s,
\qquad
y=Y+3^{q_0+j}s.
}
\]

The state variables needed by the exact same-integer branch are therefore

\[
\boxed{(j,u,h,a,Y,C)},
\]

where

- `j` = paid odd count already taken,
- `u` = current paid-macro slack,
- `h` = local dyadic depth,
- `a mod 2^h` = exact source address,
- `Y` = exact affine endpoint intercept,
- `C` = accumulated paid penalty/cost.

The coefficient does not need to be stored independently: it is always exactly

\[
\boxed{3^{q_0+j}.}
\]

This follows because an even shortcut leaves the affine coefficient unchanged, while every paid odd multiplies it by 3.

Initial state:

\[
(j,u,h,a,Y,C)=(0,1,0,0,E_0,0).
\]

## 3. Even transition

The even branch is allowed only after the opening paid odd (`j>0`), exactly as in MATH-065.

Choose the unique bit

\[
b_E\equiv-Y\pmod2,
\qquad b_E\in\{0,1\}.
\]

Then

\[
a'=a+2^h b_E,
\]

\[
Y'=\frac{Y+3^{q_0+j}b_E}{2},
\]

and

\[
\boxed{
(j,u,h,a,Y,C)
\xrightarrow{E}
(j,u-1,h+1,a',Y',C).
}
\]

The branch is retained only if the new congruence class `t=a' (mod 2^(h+1))` meets the exact source interval.

## 4. Paid-odd transition

For `j<21`, choose the unique odd bit

\[
b_O\equiv1-Y\pmod2,
\qquad b_O\in\{0,1\}.
\]

Then

\[
a'=a+2^h b_O,
\]

\[
Y'=\frac{3(Y+3^{q_0+j}b_O)+1}{2},
\]

\[
u'=u+\varepsilon_j,
\qquad
j'=j+1,
\qquad
h'=h+1.
\]

The exact paid penalty at entry slack `u>=1` is

\[
\boxed{
c_j(u)=\frac{1-2^{-u}}{3}\,\varpi_j,
}
\]

or, on a phase interval, the rigorous lower endpoint version used by MATH-065.

Thus

\[
\boxed{
(j,u,h,a,Y,C)
\xrightarrow{P}
(j+1,u+\varepsilon_j,h+1,a',Y',C+c_j(u)).
}
\]

Again the source congruence is tested exactly before the branch is retained.

## 5. First-return terminal rule

Whenever an even transition reaches

\[
u=0,
\]

the current branch terminates immediately.

If the current paid count is `j=r`, this branch belongs to paid layer `r`. It is not extended into a larger paid layer, because MATH-065 defines `u=0` before the requested target count as an earlier return.

Therefore one joint tree partitions its leaves by the first-return paid count automatically:

\[
\boxed{
\mathcal L
=\dot\bigcup_{r=1}^{21}\mathcal L_r.
}
\]

Every leaf in `L_r` has the MATH-179 local depth

\[
h_r=r+1+m(r)+\mathbf 1_{\{\varpi\le\tau_r\}}.
\]

## 6. Joint proof-neutral future lower bound

Let

\[
\underline\varpi_i
\]

be the exact lower phase bound for the current common phase cell at future paid index `i`.

Since every future paid odd has slack at least one,

\[
c_i(u)\ge c_i(1)=\frac{\underline\varpi_i}{6}.
\]

For a current state at paid count `j`, define the target-independent future potential

\[
\boxed{
\Psi_j(C)
=
\min_{r\in\{\max(1,j),\ldots,21\}}
\left[
C+
\frac16\sum_{i=j}^{r-1}\underline\varpi_i
-
\lambda(L+h_r)
\right],
}
\]

with

\[
\lambda=\frac{19}{503}.
\]

If

\[
\boxed{\Psi_j(C)\ge0,}
\]

then for every possible future terminal paid count `r<=21`, the actual cost is already bounded below by the corresponding closure threshold. The branch can therefore be pruned for all target layers simultaneously.

This is the exact joint analogue of the target-specific `future[j]` lower bound in MATH-065.

It is proof-neutral: it never removes a branch unless every possible future target layer is safe under a rigorous lower bound.

## 7. Terminal negative-candidate test

At a first-return leaf with paid count `r`, compare the exact accumulated cost to

\[
\lambda(L+h_r).
\]

Only if

\[
C<\lambda(L+h_r)
\]

is the exact AP source cylinder materialized as a remaining negative candidate for layer `r`.

Thus one traversal produces a tagged stream

\[
(r,\text{target}_0,\text{odd step},\text{multiplicity})
\]

for all `1<=r<=21`.

## 8. Relation to global depth 2..41

The paid-cluster local depth `h` above is not the MATH-051 global prefix depth `k`.

The global channel remains

\[
u_H=m(q)-(k-q),
\qquad
k=q+m(q)-u_H,
\]

with its own bounded Hensel carry.

The intended final product state is therefore a product transducer:

\[
\boxed{
\text{MATH-051 depth/Hensel channel}
\times
\text{MATH-180 paid/address first-return channel}.
}
\]

The two carry channels remain separate. Only exact affine source/address coordinates and the common Beatty scale clock may be shared without a new equivalence theorem.

## 9. Immediate computational consequence

The present MATH-115 design exports one layer at a time. MATH-180 shows that the outer `--r` loop is not mathematically required.

A joint executor can instead:

1. refine each source once to the 21-cut common phase partition;
2. construct one exact dyadic first-return tree;
3. tag terminal leaves by `r`;
4. use `Psi_j` for all-layer-safe pruning;
5. aggregate all layers in one run;
6. regress the resulting `r=2..12` tagged workloads against MATH-115 and the already closed high-r layers before any new closure claim.

This note derives the recurrence only. No new paid layer, first universal cell, or Collatz claim is made.
