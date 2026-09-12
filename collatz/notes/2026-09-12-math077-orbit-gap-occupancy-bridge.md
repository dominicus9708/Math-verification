# MATH-077 — common orbit-gap threshold for descent, first crossing, and first-cell necessity

Date: 2026-09-12

Status: `EXACT ALGEBRAIC IDENTITY / 190067-CANDIDATE REGRESSION / GLOBAL COLLATZ OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note does not close `2<=r<=13`.

## 1. Universal orbit-gap identity

For a parity word `w` of shortcut depth `k` and odd count `q`,

\[
T^k(N)=\frac{3^qN+C(w)}{2^k}.
\]

Define

\[
S(w)=\frac{C(w)}{3^q},
\qquad
\rho(k,q)=\frac{2^k}{3^q}.
\]

Then

\[
\boxed{
T^k(N)=\frac{N+S(w)}{\rho(k,q)}.
}
\]

Subtracting `N` gives

\[
\boxed{
T^k(N)-N
=\frac{S(w)-N(\rho-1)}{\rho}.
}
\]

This is the common orbit-gap equation.

## 2. Exact descent threshold

Because `rho>0`, the sign of `T^k(N)-N` is exactly the sign of

\[
S-N(\rho-1).
\]

If

\[
\rho\le1,
\]

then `rho-1<=0`, while `S>=0` for a Collatz parity word, so that prefix cannot produce strict descent below its own start.

If

\[
\rho>1,
\]

define the exact real threshold

\[
\boxed{
N_*:=\frac{S}{\rho-1}.
}
\]

Then

\[
\boxed{
T^k(N)<N
\iff
N>N_*.
}
\]

Likewise

\[
T^k(N)\ge N
\iff
N\le N_*.
\]

For an exact dyadic parity cylinder, `N` is restricted to one congruence class. Therefore this threshold does not replace address lineage; it orders the ordinary starts inside that exact cylinder.

## 3. Recovery of the historical first-descent interval result

The earlier first-descent interval audit used, for a fixed parity prefix, the affine lift formula

\[
T^j(r+2^km)-(r+2^km)
=
[T^j(r)-r]+2^{k-j}(3^{q_j}-2^j)m.
\]

The sign of its slope is exactly the sign of

\[
3^{q_j}-2^j,
\]

i.e. the opposite sign of `rho_j-1`.

Thus its two qualitative cases are the same cases of the orbit-gap identity:

- `rho_j<=1`: coefficient-surviving prefix, no eventual descent from increasing lifts at that prefix;
- `rho_j>1`: negative lift slope, equivalently a finite threshold `N_*=S/(rho_j-1)` above which every compatible start descends at that prefix.

The old finite-lift threshold is therefore a lattice version of the same real threshold, not a separate mechanism.

## 4. Recovery of the historical first-crossing occupancy

The first coefficient-crossing audit considered a surviving parent at depth `j` with

\[
2^j<3^q<2^{j+1}
\]

and its even child at depth

\[
k=j+1.
\]

For the child canonical start `n`, it defined correction occupancy

\[
\theta
=\frac{R_{\rm corr}}{n(2^{j+1}-3^q)}.
\]

At child depth `k`,

\[
R_{\rm corr}=3^qS,
\]

and

\[
2^{j+1}-3^q
=3^q(\rho-1).
\]

Hence

\[
\boxed{
\theta
=\frac{S}{n(\rho-1)}
=\frac{N_*}{n}.
}
\]

Therefore the old criterion

\[
\theta<1
\]

is exactly

\[
\boxed{
S<n(\rho-1),
}
\]

which is exactly strict descent at the crossing.

Thus `theta` is not an independent dynamical variable. It is the threshold occupancy ratio `N_*/n`.

## 5. Recovery of the historical integer margin H

The old crossing audit also used

\[
H=2n-z,
\]

where `z` is the actual predecessor immediately before the crossing even step. Since the crossing child endpoint is

\[
T^k(n)=z/2,
\]

we have

\[
H=2(n-T^k(n)).
\]

Using the orbit-gap identity,

\[
\boxed{
H
=\frac{2\,[n(\rho-1)-S]}{\rho}.
}
\]

Therefore `H>0`, `theta<1`, and strict descent are exactly equivalent descriptions of the same positive gap.

## 6. Exact finite regression through depth 26

The companion certificate regenerates the historical first-crossing set through depth 26.

It reproduces exactly

\[
\boxed{190,067}
\]

crossing candidates and the historical per-depth candidate counts.

For every candidate it checks exact rational equality of

\[
\theta
=\frac{S}{n(\rho-1)}
\]

and exact integer equality of

\[
H
=\frac{2[n(\rho-1)-S]}{\rho}.
\]

Results:

- occupancy identity failures: `0`;
- margin identity failures: `0`;
- strict-descent failures: `0`.

The zero finite failures support implementation consistency. The identities themselves are algebraic and do not depend on depth 26.

## 7. Connection to MATH-054 first-cell terminal necessity

At the first universal Farey cell terminal crossing, MATH-054 writes

\[
\delta=\frac{2^{A_0}}{3^{q_0}}-1.
\]

In present notation this is simply

\[
\boxed{\delta=\rho-1}.
\]

A hypothetical non-descending bad terminal path must obey

\[
S\ge\delta N.
\]

Therefore

\[
\boxed{
S\ge N(\rho-1)
}
\]

is not a new first-cell-specific condition: it is the general non-descent side of the universal orbit-gap identity.

This unifies three formerly separate descriptions:

\[
\boxed{
\text{first-descent lift threshold}
\equiv
\text{first-crossing occupancy}
\equiv
\text{first-cell terminal correction threshold}.
}
\]

## 8. Relation to MATH-072 penalty

MATH-072 gives

\[
S=1+\Sigma-\rho
\]

and for a paid odd event

\[
p=\frac{\Omega-\rho}{3}.
\]

Thus the terminal orbit gap and the running paid penalty now live in the same analytic coordinates `(S,rho,Omega)`:

\[
T^k(N)-N
=\frac{S-N(\rho-1)}{\rho}.
\]

This does not yet provide the global Bellman lower bound at `19/503`; it identifies the exact terminal quantity that the Bellman accumulation must defeat.

## 9. DSD claim boundary

Established:

- universal orbit-gap identity;
- exact threshold `N_*=S/(rho-1)` when `rho>1`;
- exact equivalence with the old first-crossing `theta` and integer margin `H`;
- exact equivalence in form with MATH-054 terminal necessity;
- 190,067-candidate depth-26 regression with zero failures.

Not established:

- that every admissible path eventually reaches `rho>1` in a way that forces descent;
- the global `19/503` penalty lower bound;
- first-cell emptiness;
- closure of `2<=r<=13`;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math077_orbit_gap_occupancy_bridge_certificate.py`
