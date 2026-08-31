# A0 s=1 Route-B — reduced control and finite-resolution DAG bound

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Coordinate reduction

At absolute parity depth `h`, define the ballot endpoint discrepancy

\[
\delta=q-\left\lfloor\frac{Rh}{J}\right\rfloor.
\]

The source-channel projective quotient was

\[
Q_d=(Y,G)
=
\left(y\bmod2^d,\;3^q\bmod2^d\right).
\]

But at a fixed layer `h`,

\[
\boxed{
q=\delta+\left\lfloor\frac{Rh}{J}\right\rfloor.
}
\]

Therefore

\[
\boxed{
G=3^{\delta+\lfloor Rh/J\rfloor}\bmod2^d
}
\]

is determined by `(h,delta,d)` and need not be stored independently.

Likewise the ballot endpoint phase

\[
r_h=Rh\bmod J
\]

is determined entirely by the layer.

Thus a layered source+ballot state may store

\[
\boxed{
(Y,\delta,b,g)
}
\]

where `b` is the ballot minimum and `g` is the critical phase.  If a certificate needs the literal critical prefix index, replace `g` by that index; the counting bound below is unchanged because only the fixed parent critical point or one of the new prefix positions can be selected.

At fixed correction resolutions `(K,L)`, append

\[
C_2=C\bmod2^K,
\qquad
C_3=C\bmod3^L.
\]

A reduced layered control state is therefore

\[
\boxed{
\mathcal C=(Y,\delta,b,g,C_2,C_3),
}
\]

with absolute depth and remaining precision supplied externally by the DAG layer.

---

## 2. Exact one-bit update

Let the next parameter bit be `eta in {0,1}`.  Reconstruct

\[
q=\delta+\left\lfloor\frac{Rh}{J}\right\rfloor,
\qquad
G=3^q\bmod2^d.
\]

Then the parity output is

\[
\beta=(Y+\eta)\bmod2.
\]

The projective source endpoint update is

\[
Y'=
\begin{cases}
(Y+G\eta)/2,&\beta=0,\\
(3(Y+G\eta)+1)/2,&\beta=1,
\end{cases}
\pmod{2^{d-1}}.
\]

Let

\[
\Delta_h=
\left\lfloor\frac{R(h+1)}J\right\rfloor
-
\left\lfloor\frac{Rh}J\right\rfloor
\in\{0,1\}.
\]

Then

\[
\boxed{
\delta'=\delta+\beta-\Delta_h.
}
\]

The new endpoint discrepancy `delta'` is exactly the candidate added to the ballot-minimum scan at phase

\[
R(h+1)\bmod J.
\]

Correction residues update by

\[
C'=
\begin{cases}
C,&\beta=0,\\
3C+2^h,&\beta=1,
\end{cases}
\]

reduced modulo `2^K` and `3^L`.

Hence all omitted coordinates are reconstructed exactly when needed.

---

## 3. Finite implementation audit

`collatz/src/A0_s1_routeB_reduced_source_ballot_control_certificate.py` checks:

- every parity parent prefix of length `0,...,4` (`31` parents);
- future precision `1,...,6`;
- every future parameter residue at each tested precision;
- fixed correction audit resolution `(K,L)=(8,6)`.

It performs:

- 186 coefficient-reconstruction checks;
- 3,906 complete future-residue path checks;
- 19,902 exact reduced-vs-full transition checks.

The regression is an implementation guard.  Coordinate redundancy follows algebraically from the displayed identities.

---

## 4. Layerwise state-count theorem

Fix one parent family and a future horizon `D`.  Let `i` be the number of future parameter/parity bits already consumed, so the remaining source precision is

\[
d=D-i.
\]

At layer `i`:

### Source coordinate

\[
Y\bmod2^{D-i}
\]

has at most

\[
2^{D-i}
\]

values.

### Endpoint discrepancy

The future block has between `0` and `i` ones.  With the parent fixed, `delta` therefore has at most

\[
i+1
\]

values.

### Ballot minimum

The current minimum is either the fixed parent minimum or one of the `i` newly exposed endpoint discrepancies.  Hence at most

\[
i+1
\]

values occur.

### Critical phase/index

The selected critical point is either the fixed parent critical point or one of the `i` new prefix positions.  Hence there are at most

\[
i+1
\]

possibilities.

### Correction coordinates

At fixed resolutions,

\[
C_2\in\mathbb Z/2^K\mathbb Z,
\qquad
C_3\in\mathbb Z/3^L\mathbb Z,
\]

contribute at most

\[
2^K3^L
\]

states.

Therefore the reduced control/classifier state count at layer `i` satisfies

\[
\boxed{
N_i^{\rm control}
\le
2^{D-i+K}3^L(i+1)^3.
}
\]

The interval four-state cylinder theorem contributes at most a factor `4`, so the full family-state count obeys

\[
\boxed{
N_i^{\rm family}
\le
4\,2^{D-i+K}3^L(i+1)^3.
}
\]

Of course only `2^i` raw parameter prefixes exist.  Thus the sharper layer bound is

\[
\boxed{
n_i
\le
\min\left(
2^i,
4\,2^{D-i+K}3^L(i+1)^3
\right).
}
\]

This is an exact counting upper bound for the finite-resolution product state described here.

---

## 5. Forced-merging criterion

If

\[
2^i
>
4\,2^{D-i+K}3^L(i+1)^3,
\]

then there are more raw residue prefixes than available exact product states.  Hence at least two prefixes must merge into the same continuation state.

Equivalently,

\[
\boxed{
2^{2i-D-K-2}
>
3^L(i+1)^3
\Longrightarrow
\text{state merging is forced at layer }i.
}
\]

For fixed `K,L`, the crossing occurs after roughly half the horizon plus logarithmic corrections.  This is a pigeonhole consequence, not a heuristic.

---

## 6. Whole-DAG upper bound

Let

\[
A=4\,2^K3^L.
\]

Using

\[
\min(x,y)\le\sqrt{xy},
\]

we obtain

\[
n_i
\le
\sqrt{
2^i\cdot A2^{D-i}(i+1)^3
}
=
2^{D/2}\sqrt A\,(i+1)^{3/2}.
\]

Summing over all layers `i=0,...,D` and using

\[
\sum_{i=0}^D(i+1)^{3/2}
\le
(D+1)^{5/2},
\]

gives

\[
\boxed{
N_{\rm DAG}
\le
2^{D/2}\sqrt A\,(D+1)^{5/2}.
}
\]

Since

\[
\sqrt A=2^{1+K/2}3^{L/2},
\]

\[
\boxed{
N_{\rm DAG}
\le
2^{D/2}
\,2^{1+K/2}3^{L/2}
(D+1)^{5/2}.
}
\]

For **fixed** correction resolutions `(K,L)`, this replaces the naive `2^D` full-leaf upper bound by a square-root-exponential bound times a polynomial factor.

This is not yet polynomial-time closure.

---

## 7. DSD audit

### Exact / closed

- `G=3^q mod 2^d` is redundant once layer `h` and endpoint discrepancy `delta` are known;
- `q` itself is recoverable from `(h,delta)`;
- the ballot length phase is layer-determined;
- the reduced source+ballot transition is exact;
- fixed-resolution layer state count has the displayed upper bound;
- interval payload adds at most a constant factor `4`;
- finite-resolution DAG size has the displayed square-root-exponential upper bound.

### Finite regression only

- the short-prefix/future-residue certificate validates the implementation but is not the proof.

### Still open

1. whether the required correction resolutions `K,L` can remain bounded, grow sublinearly, or be recursively renormalized in the universal Route-B membership problem;
2. additional exact identities that reduce the remaining `2^{D/2}`-type source-coordinate growth;
3. proof of enough A/B closures for all surviving long families;
4. global Collatz obligations.

---

## 8. Updated bottleneck

At fixed resolution the exponential leaf explosion has been rigorously reduced but not eliminated:

\[
2^D
\quad\leadsto\quad
O\!\left(2^{D/2}\operatorname{poly}(D)\right)
\]

up to the fixed `(K,L)` factor.

The next target should therefore be the remaining source-coordinate factor

\[
Y\bmod2^{D-i},
\]

and, in parallel, the growth law actually required for `(K,L)`.  Any further exact localization or hierarchical reuse of `Y` can potentially push the bound below the current square-root-exponential barrier.
