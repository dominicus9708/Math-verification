# Two-ended residue core at the next unresolved resonance

Date: 2026-08-09

Status: **DERIVED EXACT BOUNDARY-CORE LEMMA + RATIONAL FINITE CERTIFICATE**

This note adds the 3-adic endpoint side to the project’s existing 2-adic start-residue analysis. The endpoint-residue viewpoint is classical/standard in accelerated Collatz arithmetic and is also used explicitly in Kramer (2026). The project-specific role here is to combine it with the certified first-crossing window, recursive core, and mechanical-defect channel.

## 1. First-crossing affine identity

At

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617,
\]

write

\[
2^\sigma y=3^q x+R,
\qquad
R=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
\]

The rational DK certificate gives

\[
\boxed{x<36,797,925,187,243,805,015,225.}
\]

For a paradoxical first crossing, `y>=x` and

\[
y-x=\frac{S-\delta x}{1+\delta}\le S\le S^*(q)\le U_S.
\]

The same rational certificate has

\[
\lfloor U_S\rfloor=33,068,504,826.
\]

Since `x` is integral and `x<U_cert`, every paradoxical candidate obeys

\[
\boxed{
y\le
36,797,925,187,276,873,520,050.}
\]

Moreover

\[
3^{47}=26,588,814,358,957,503,287,787
<y_{\max}
<3^{48}=79,766,443,076,872,509,863,361.
\]

Thus `48` is the first universal ternary-modulus length at which the candidate endpoint is guaranteed to equal its least residue representative.

## 2. Terminal t-odd core lemma

Reduce the affine identity modulo `3^t`, with `1<=t<=q`. All correction terms with

\[
i<q-t
\]

carry a factor `3^t` and disappear. Hence

\[
\boxed{
2^\sigma y
\equiv
\sum_{i=q-t}^{q-1}2^{d_i}3^{q-1-i}
\pmod{3^t}.
}
\]

Since `2^sigma` is invertible modulo `3^t`,

\[
\boxed{
y\equiv
2^{-\sigma}
\sum_{i=q-t}^{q-1}2^{d_i}3^{q-1-i}
\pmod{3^t}.}
\]

Therefore the endpoint residue modulo `3^t` is determined **only by the last `t` odd-position coordinates**.

If additionally `0<=y<3^t`, then this congruence determines `y` as an ordinary integer exactly.

For the present resonance every paradoxical candidate has `y<3^48`, so the last 48 odd positions form an exact terminal core.

This is the endpoint-dual of the classical start-residue fact that the first `B` parity-time bits determine `x mod 2^B`, and determine `x` itself when `x<2^B`.

## 3. Exact mechanical terminal residue

Let

\[
\kappa_i=\lfloor i\log_2 3\rfloor.
\]

Set the last 48 odd positions to their mechanical caps:

\[
d_i=\kappa_i,
\qquad i=q-48,\ldots,q-1.
\]

The values of all 48 `kappa_i` are certified without floating point by the same rational logarithm intervals used in `rational-dk-next-resonance-certificate.md`. For each candidate integer `kappa`, the verifier checks the strict rational inequalities

\[
\kappa\,\ln2<(q-r)\ln3<(\kappa+1)\ln2
\]

using an upper bound for the left coefficient and lower bound for the right as appropriate.

The exact terminal residue is

\[
\boxed{
y_{\rm mech}^{(48)}=
40,150,856,745,180,969,070,537.}
\]

This exceeds the certified endpoint ceiling by

\[
\boxed{
3,352,931,557,904,095,550,487.
}
\]

Therefore:

\[
\boxed{
\text{the last 48 odd positions cannot all be mechanical caps.}
}
\]

Equivalently every paradoxical candidate at this resonance must have

\[
\boxed{
\#\{i\in[q-48,q-1]:d_i<\kappa_i\}\ge1.
}
\]

This is a deterministic terminal obstruction, not a density heuristic.

## 4. Two-ended core formulation

The present finite window gives two exact boundary cores:

### Start side

Because `x<2^75`, the first 75 parity-time bits determine the ordinary integer `x` exactly.

### Endpoint side

Because `y<3^48`, the last 48 odd-position coordinates determine the ordinary endpoint `y` exactly.

Hence a hypothetical next-resonance candidate can be viewed as a bridge

\[
\boxed{
\text{75-bit start core}
\quad\longleftrightarrow\quad
\text{middle near-critical/defect channel}
\quad\longleftrightarrow\quad
\text{48-odd terminal core}.
}
\]

The nominal `q≈1.375e11` odd-position word need not be represented uniformly at full resolution in order to express both boundary values.

## 5. Relation to the 2–3–infinity diagnostic

Kramer (2026, arXiv:2607.10041) studies odd-to-odd exponent codes and assigns each finite code:

1. real drift;
2. a 2-adic start representative;
3. a 3-adic endpoint representative.

The present two-ended core uses the same classical 2-adic/3-adic residue duality. It should therefore not be described as a new discovery of that duality.

The independent project-specific additions are:

- first-coefficient-crossing rather than generic exponent-code search;
- exact recursive-sufficiency magnitude windows;
- rational Denjoy–Koksma correction certificates;
- mechanical-cap defect budgets;
- exact min-plus/cyclic-successor pruning;
- and the specific finite boundary-core lengths `75` and `48` at the next unresolved resonance.

## 6. What this does and does not prove

The single terminal-defect lower bound is far too small to contradict the global certified upper defect counts. Its significance is structural: the endpoint side supplies a second exact arithmetic boundary condition that is independent of the initial 75-bit reconstruction.

The next useful target is a **terminal sparse-defect residue gap** or a two-sided bridge theorem: prove that simultaneously small start and endpoint representatives force many mechanical-cap defects, or force a late canonical lift, uniformly with the middle coefficient barrier.