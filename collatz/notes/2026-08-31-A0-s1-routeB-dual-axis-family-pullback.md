# A0 s=1 Route-B dual-axis family pullback theorem

## Purpose

This note combines the exact parent-channel parameterization with a finite ternary formation-residue predicate.

It gives a family-level CRT pullback: a dyadic future-block condition and a ternary endpoint/formation condition become an exact union of arithmetic progressions in the parent parameter `m`.

This is an exact algebraic theorem. It does **not** identify C4F with the formation-residue predicate unless that factorization is proved separately.

---

## Parent channel

Fix an exact prefix channel

\[
X=r+2^h m,
\qquad
Y:=T^h(X)=y+3^q m.
\]

Fix a future block length \(\ell\). For each binary block \(B\in\{0,1\}^{\ell}\), the exact channel/block partition gives one residue

\[
\mu_B\pmod{2^\ell}
\]

such that

\[
\operatorname{next}_\ell(m)=B
\iff
m\equiv\mu_B\pmod{2^\ell}.
\]

The map \(B\mapsto\mu_B\) is a permutation.

---

## Ternary formation predicate

Fix a ternary depth \(K\ge0\) and a target set

\[
\mathcal T\subseteq\mathbb Z/3^K\mathbb Z.
\]

Consider the predicate

\[
Y\bmod3^K\in\mathcal T.
\]

Since

\[
Y=y+3^q m,
\]

the amount of the parameter `m` visible to this predicate depends on the relative sizes of \(q\) and \(K\).

### Case 1: \(K\le q\)

Then

\[
3^q m\equiv0\pmod{3^K},
\]

so

\[
\boxed{Y\equiv y\pmod{3^K}}
\]

for every `m`.

Hence the ternary predicate is constant on the entire parent channel:

\[
Y\bmod3^K\in\mathcal T
\iff
y\bmod3^K\in\mathcal T.
\]

No ternary subdivision of the parameter family is required.

### Case 2: \(K>q\)

A target residue \(t\in\mathcal T\) can be reached only if

\[
t\equiv y\pmod{3^q}.
\]

For every compatible target residue define

\[
\nu_t
:=
\frac{t-y}{3^q}
\pmod{3^{K-q}}.
\]

This is well defined modulo \(3^{K-q}\). Then

\[
\boxed{
Y\equiv t\pmod{3^K}
\iff
m\equiv\nu_t\pmod{3^{K-q}}.
}
\]

Thus a finite ternary target language pulls back to a finite set of parameter residues modulo \(3^{K-q}\).

---

## Dual-axis CRT theorem

Assume \(K>q\). Fix a future block \(B\) and a compatible formation target \(t\).

The two exact conditions are

\[
m\equiv\mu_B\pmod{2^\ell},
\]

and

\[
m\equiv\nu_t\pmod{3^{K-q}}.
\]

Because

\[
\gcd(2^\ell,3^{K-q})=1,
\]

the Chinese remainder theorem gives a unique residue

\[
\omega_{B,t}
\pmod{2^\ell3^{K-q}}.
\]

Therefore

\[
\boxed{
\operatorname{next}_\ell(m)=B
\ \text{and}\ 
Y\equiv t\pmod{3^K}
\iff
m\equiv\omega_{B,t}
\pmod{2^\ell3^{K-q}}.
}
\]

For a set of accepted blocks \(\mathcal B\) and a ternary target language \(\mathcal T\), the complete accepted parent family is an exact disjoint union of the corresponding CRT residue classes, after duplicate residues are canonically merged.

No independence assumption is involved: this is an exact intersection of two defined observation axes.

---

## Exact interval counting

For a finite parent interval

\[
I=[M_0,M_1]\cap\mathbb Z
\]

and one accepted residue \(\omega\pmod M\), where

\[
M=2^\ell3^{\max(K-q,0)},
\]

the exact count is

\[
\#\{m\in I:m\equiv\omega\pmod M\}
=
\max\left(
0,
\left\lfloor\frac{M_1-\omega}{M}\right\rfloor
-
\left\lceil\frac{M_0-\omega}{M}\right\rceil
+1
\right).
\]

Thus a very large SAFE interval can be filtered and counted family-wise without enumerating individual integers.

---

## Formation-language cardinality handoff

The existing globalization extraction defines the rank/depth formation target language

\[
\mathcal T_{k,K}\subseteq\mathbb Z/3^K\mathbb Z
\]

and proves

\[
\boxed{
|\mathcal T_{k,K}|\le\binom{K+k}{k}.
}
\]

Consequently, at fixed formation rank `k`, the number of ternary residue families needed by the pullback is at most polynomial in `K`, even though the ambient ternary residue space has size \(3^K\).

For one parent channel only targets satisfying

\[
t\equiv y\pmod{3^{\min(q,K)}}
\]

are compatible, so the actual number of pulled-back ternary families can only be smaller.

This does not by itself control the number of admissible dyadic future blocks; that is where ballot/correction/run-hierarchy compression is still needed.

---

## Relation to family closure

The remaining Route-B family problem can now be separated into three exact layers:

1. **source block selection:** residue modulo \(2^\ell\) — CLOSED;
2. **finite formation target selection:** residue modulo \(3^{\max(K-q,0)}\) — CLOSED;
3. **semantic long-membership/C4F factorization:** OPEN.

If C4F can be proved to depend only on a finite formation target state plus a composable source/run state, then the theorem above converts the decision immediately into CRT arithmetic families on every parent interval.

---

## DSD audit

✅ dyadic and ternary axes are constructed independently before intersection;

✅ the parent candidate is not redefined during refinement;

✅ CRT is used only after both residue conditions are already defined;

✅ no probabilistic independence or equidistribution is assumed;

✅ large finite populations are represented by exact arithmetic families;

✅ formation target-language sparsity can be transferred to parameter families;

❌ C4F has not yet been shown to factor through this finite ternary predicate;

❌ run-hierarchy source compression is not yet a complete semantic membership quotient;

❌ no global Route-B or Collatz conclusion is claimed.

## Gate update

Arithmetic family transport is now closed on both relevant number-theoretic axes.

The remaining G4 semantic bottleneck is sharper:

\[
\boxed{
\text{prove a C4F-sufficient state that is composable or hierarchically renewable.}
}
\]

Once that factorization is available, family-level CRT pullback no longer requires singleton enumeration.
