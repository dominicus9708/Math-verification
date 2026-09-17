# MATH-186 — exact boundary-transfer dichotomy for multi-paid macros

Date: 2026-09-17

Status: `EXACT STRUCTURAL LEMMA / MULTI-SOURCE TRANSFER SAFE OR SINGLETON / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-185 proves that every multi-paid cluster `r>=2` has strictly positive local reduced-cost drift at the MATH-060 slope

\[
\lambda=\frac{19}{503}.
\]

MATH-061 proves exact closure of arithmetic-progression cylinders under macro composition, and MATH-074 proves exact source-resolution consumption under a compatible dyadic macro congruence.

The remaining question is how the zero-cost prefix immediately preceding a multi-paid cluster transfers across the Bellman potential without resetting the accounting origin.

This note gives the exact dichotomy.

No paid-count layer, first cell, or Collatz theorem is closed here.

## 2. Current exact cylinder

Let the current same-integer source family have `M>=1` ordinary anchors and resolution height

\[
R=\lceil\log_2 M\rceil,
\qquad R(1)=0.
\]

Let the next compatible zero-cost prefix have shortcut length `L>=0`.

By the MATH-061 composition law, compatibility of a length-`L` parity/macro factor fixes one residue class of the current source parameter modulo `2^L` because the target parameter coefficient is an odd power of three and is therefore invertible modulo `2^L`.

Let the compatible child multiplicity be `M'` and

\[
R'=\lceil\log_2 M'\rceil.
\]

MATH-074 gives the exact resolution inequality

\[
\boxed{R'\le\max(0,R-L).}
\]

## 3. Resolution potential

Use the MATH-074 potential

\[
\boxed{H_R=-\lambda R.}
\]

The zero-cost prefix contributes reduced cost

\[
-\lambda L+H_{R'}-H_R
=-\lambda L+\lambda(R-R').
\]

Hence

\[
\boxed{
-\lambda L+H_{R'}-H_R
\ge-\lambda(L-R)_+.
}
\]

In particular, if

\[
L\le R,
\]

then

\[
\boxed{-\lambda L+H_{R'}-H_R\ge0}
\]

and moreover, for `L>=1`,

\[
\boxed{R'\le R-L<R.}
\]

Thus every nontrivial zero-cost prefix that fits inside the unresolved source resolution is both Bellman-safe and strictly resolution-contracting.

## 4. Append a multi-paid cluster

Let the following exact paid cluster contain `r>=2` paid odd events and residual shortcut length `h_r`, with accumulated penalty `P_r`.

Define its local surplus

\[
\boxed{\epsilon_r:=\mathcal P_r-\lambda h_r.}
\]

MATH-185 proves

\[
\boxed{\epsilon_r>0\qquad(r\ge2).}
\]

If the resolution potential is evaluated immediately before the zero-cost prefix and immediately after the prefix compatibility cut, the combined prefix-plus-paid reduced-cost balance is

\[
\Delta\mathcal B
=\mathcal P_r-\lambda(L+h_r)+H_{R'}-H_R.
\]

Therefore

\[
\boxed{
\Delta\mathcal B
=\epsilon_r-\lambda L+\lambda(R-R')
}
\]

and the resolution inequality yields

\[
\boxed{
\Delta\mathcal B
\ge
\epsilon_r-\lambda(L-R)_+.
}
\]

This is the exact boundary-transfer lower bound.

## 5. Safe-or-singleton dichotomy

There are only two structural cases.

### Case A — `L<=R`

Then

\[
\Delta\mathcal B\ge\epsilon_r>0.
\]

Hence the whole zero-cost-prefix plus multi-paid transfer is strictly Bellman-positive without ordinary-source enumeration.

If `L>=1`, the child resolution also satisfies

\[
R'<R.
\]

So a legal multi-source transfer cannot remain at the same unresolved resolution height while carrying a nontrivial zero-cost prefix.

### Case B — `L>R`

Then the exact resolution inequality gives

\[
\boxed{R'=0.}
\]

Thus the compatible child contains at most one ordinary source anchor before the unresolved overshoot can cause any Bellman deficit.

The possible negative amount is localized to

\[
\boxed{
\lambda(L-R)-\epsilon_r,
}
\]

when this quantity is positive.

Therefore every possible deficit of a multi-paid boundary transfer is a **singleton overshoot obligation**.

Equivalently,

\[
\boxed{
\Delta\mathcal B\le0
\Longrightarrow
R'=0.
}
\]

This is stronger than saying merely that low-paid AP workloads are finite: it removes all genuinely multi-source negative transitions from the theorem target.

## 6. Consequence for the low-paid frontier

MATH-185 already removes the paid count `r>=2` as the source of local negative drift.

The present lemma removes unresolved multi-source zero-cost prefixes as a source of negative transfer: while a prefix fits in the current source resolution, the resolution potential pays for it exactly enough, and the paid cluster adds a strict surplus.

Hence the remaining theorem target is

\[
\boxed{
\text{exact singleton overshoot / terminal-address closure}
}
\]

rather than separate `r=10`, `r=9`, ..., `r=2` source enumerations.

The paid count remains relevant to transition legality and to the positive surplus `epsilon_r`, but not to the existence of a multi-source Bellman deficit.

## 7. Relation to MATH-183

MATH-183 remains useful at a `rho>1` terminal handoff because its orbit-gap midpoint test can delete a descending suffix and reduce resolution without enumerating ordinary anchors.

However the present transfer theorem shows that, for zero-cost-prefix transitions themselves, a separate `kappa>=1` theorem is not needed in the `L<=R` regime: exact congruence consumption already gives

\[
R'\le R-L.
\]

MATH-183 is therefore best viewed as an additional contraction mechanism at the terminal orbit-gap stage, not as the sole source of well-founded resolution decrease.

## 8. Correct bookkeeping warning

The `R` in this theorem is the resolution height of the **current cylinder before the next prefix congruence is imposed**.

It is invalid to take the multiplicity of a standalone MATH-065 source that has already been selected by its length-`L` parity prefix and then retroactively use that post-selection multiplicity as the pre-prefix `R`.

The transfer theorem must be applied along the exact MATH-061 composition lineage, carrying `M` (or an exact equivalent source interval/count) from boundary to boundary.

This distinction prevents double-counting resolution credit.

## 9. Finite well-foundedness consequence

Under the pre-first-cell audited anchor ceiling, MATH-074 gives

\[
R\le73.
\]

Every compatible nontrivial zero-cost prefix with `1<=L<=R` strictly decreases the nonnegative integer `R`.

Thus an aperiodic exact lineage cannot contain infinitely many such multi-source prefix transfers without eventually reaching `R=0`.

The remaining infinite-path issue must therefore either use zero-length prefix transitions, which are locally paid-positive by MATH-185, or reach the singleton terminal-address regime.

This is a structural well-foundedness reduction; it is not yet a global closure theorem.

## 10. Claim boundary

Established:

- exact boundary-transfer identity
  \[
  \Delta\mathcal B=\epsilon_r-\lambda L+\lambda(R-R');
  \]
- exact lower bound
  \[
  \Delta\mathcal B\ge\epsilon_r-\lambda(L-R)_+;
  \]
- for every multi-paid cluster `r>=2`, `L<=R` implies strict positive transfer;
- every possible nonpositive transfer implies `R'=0`, hence a singleton overshoot obligation;
- nontrivial multi-source zero-cost prefixes strictly decrease resolution.

Not established:

- uniform singleton overshoot closure;
- a theorem for every possible zero-length/singleton boundary cycle beyond existing periodic-ghost results;
- closure of `r=10` or lower paid layers;
- first universal Farey-cell emptiness;
- the Collatz conjecture.
