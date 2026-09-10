# MATH-054 — one exact rational S carries correction, Hensel class, and dyadic root address

Date: 2026-09-10
Status: `EXACT THREE-PROJECTION BRIDGE / FINITE REGRESSION PASS / GLOBAL BAD-PATH EMPTINESS OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note identifies an exact common state variable. It does not by itself exclude all first-cell starts or all infinite trajectories.

## 1. The common rational object

For a length-k shortcut parity word `w`, odd count `q`, and correction `C(w)`,

\[
T_w^k(N)=\frac{3^qN+C(w)}{2^k}.
\]

Define

\[
\boxed{S(w)=\frac{C(w)}{3^q}\in\mathbb Z[1/3].}
\]

Then

\[
\boxed{T_w^k(N)=\frac{3^q}{2^k}\bigl(N+S(w)\bigr).}
\]

The project previously carried correction magnitude, exact Hensel class, and dyadic root address as conceptually separate pieces of information.  They are exact projections of this same rational `S`.

## 2. Real projection: correction and endpoint budget

In the ordinary real ordering, `S` is the normalized correction.  At a coefficient-deficient terminal prefix `3^q<2^k`, write

\[
\delta_{k,q}=\frac{2^k}{3^q}-1>0.
\]

Then

\[
T_w^k(N)\ge N
\iff
\boxed{S(w)\ge\delta_{k,q}N.}
\]

At the first universal crossing cell this is the existing proof-facing terminal correction condition.

MATH-053 further expresses the same real quantity in the coefficient-boundary slack history:

\[
\boxed{
S(w)=\frac13\sum_{r=0}^{q-1}2^{-u_r}\Omega_r,
}
\]

with

\[
\Omega_r=\frac{2^{r+m(r)}}{3^r},
\qquad
m(r)=\lfloor r\log_2(3/2)\rfloor.
\]

## 3. Dyadic projection: the same rational is the root address

Integrality of the k-step endpoint gives

\[
3^qN+C(w)\equiv0\pmod{2^k}.
\]

Since the denominator of `S=C/3^q` is odd, `S` has a well-defined image modulo `2^k`.  Therefore

\[
\boxed{N(w)\equiv-S(w)\pmod{2^k}.}
\]

If the odd positions are

\[
p_0<p_1<\cdots<p_{q-1},
\]

then

\[
S(w)=\sum_{r=0}^{q-1}\frac{2^{p_r}}{3^{r+1}},
\]

so equivalently

\[
\boxed{
N(w)\equiv-
\sum_{r=0}^{q-1}2^{p_r}3^{-r-1}\pmod{2^k}.
}
\]

Using the MATH-053 slack coordinate, immediately before odd event `r` we have

\[
p_r=r+d_r=r+m(r)-u_r,
\]

hence

\[
\boxed{
N(w)\equiv-
\sum_{r=0}^{q-1}
2^{r+m(r)-u_r}3^{-r-1}\pmod{2^k}.
}
\]

Thus the same weighted slack terms that determine the Archimedean correction also determine the 2-adic starting address.  They are not independent filters.

### Important semantic point

This does **not** mean that a coarse real bound on `S` preserves the address.  The exact rational `S` does; an interval, average, upper bound, floating-point approximation, or aggregated descriptor of `S` generally does not.

This reconciles the new bridge with the older audit conclusion that scalar correction-only estimates lose same-integer information.

## 4. Hensel projection: exact classes are S modulo integers

At fixed `q`, two corrections are in the same exact root-Hensel class exactly when

\[
C(F)\equiv C(E)\pmod{3^q}.
\]

Dividing their difference by `3^q` gives

\[
\boxed{
C(F)\equiv C(E)\pmod{3^q}
\iff
S(F)-S(E)\in\mathbb Z.
}
\]

Therefore an exact Hensel class is the class of `S` modulo integer translation.

If

\[
S(F)=S(E)+m,\qquad m\in\mathbb Z_{>0},
\]

then `F` dominates `E` in correction by Hensel translation credit `m`.

The dyadic roots transform simultaneously as

\[
\boxed{N(F)\equiv N(E)-m\pmod{2^k}.}
\]

## 5. Endpoint-fiber translation symmetry

The transformation

\[
\boxed{(N,S)\mapsto(N-m,S+m)}
\]

preserves

\[
\boxed{J=N+S}
\]

and therefore preserves the fixed-(k,q) endpoint:

\[
\frac{3^q}{2^k}(N-m+S+m)
=
\frac{3^q}{2^k}(N+S).
\]

This is the `S`-coordinate form of the endpoint/correction-ordering redundancy already audited in MATH-009.  It is not claimed here as a new independent theorem; MATH-054 identifies the common rational coordinate in which that earlier relation and the MATH-053 slack formula meet.

Consequently, within a fixed endpoint/Hensel fiber, maximizing `S` is the same as minimizing the ordinary root `N` whenever the modular representatives are lifted without wraparound.  The existing root-safe credit bound controls precisely the range in which the smaller-root contradiction is legal.

## 6. DSD information audit

The previous working picture suggested a product state

\[
\text{correction state}\times\text{dyadic-address state}\times\text{Hensel state}.
\]

That would duplicate information if each factor were retained exactly.

The exact common object is instead

\[
\boxed{S\in\mathbb Z[1/3]},
\]

with three projections:

\[
\boxed{
\begin{array}{rcl}
\text{real embedding of }S &\to& \text{correction magnitude / endpoint inequality},\\
S\bmod\mathbb Z &\to& \text{root-Hensel class},\\
-S\bmod2^k &\to& \text{canonical dyadic root address}.
\end{array}}
\]

This is a DSD-safe merge only when `S` is exact.  Replacing it by one of its projections loses the other two.

## 7. First-cell reformulation

At the first universal cell `(A_0,q_0)`, any hypothetical bad prefix must produce an exact rational `S` generated by a coefficient-valid slack path such that simultaneously:

1. its 2-adic projection gives the same ordinary start in the current first-cell window;
2. every root-safe prefix satisfies nested Hensel maximality, equivalently no legal positive integer translate `S+m` supplies a smaller positive same-endpoint root;
3. its real projection has enough terminal correction,
   \[
   S\ge\delta_{A_0,q_0}N;
   \]
4. the parity/slack lineage reaches the designated first crossing rather than an earlier coefficient failure.

Thus the next proof-facing object is not three independent filters.  It is a constrained orbit of one exact rational additive process viewed simultaneously through the real, integer-quotient, and 2-adic projections.

## 8. Reproducibility

Certificate:

`collatz/src/2026_09_10_math054_single_rational_S_bridge_certificate.py`

Finite exact regression includes:

- every parity word of lengths 1..11 (`4094` words): root from `-S mod 2^k` reproduces the word exactly;
- exact endpoint factorization through `(3^q/2^k)(N+S)`;
- `124453` same-(k,q) word-pair comparisons: direct `mod 3^q` class equality agrees exactly with integer translation in `S`;
- `2373` same-class pairs: root translation agrees with `N -> N-m mod 2^k`;
- `3110` coefficient-deficient small prefixes: endpoint nondecrease agrees exactly with the real inequality `S >= delta N`.

These are regression checks of algebraic identities, not evidence substituted for their proofs.

## 9. Next target

The counting problem is no longer primary.  The next target is to compress the **exact rational S process without separating its projections**.

Because the current first-cell ordinary start satisfies `N<2^72`, the 2-adic root is already fixed after 72 parity steps.  Terms added at odd positions `p>=72` vanish modulo `2^72`, while they still contribute to the real correction and Hensel structure.  This creates a natural resolution split:

- first 72 positions: establish the ordinary root address exactly;
- depths 72..195: preserve the frozen root while propagating root-safe Hensel/slack constraints;
- terminal first-cell extension: test whether the remaining real correction budget can reach the endpoint inequality.

The immediate computational question is whether the existing `61+11` address machinery and the universal Hensel/slack transducer can be coupled through this single-rational `S` representation without reintroducing a large address enumeration.

Collatz remains `OPEN`.
