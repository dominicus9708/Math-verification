# Parity recursive-sufficiency repair and global coefficient gate

Date: 2026-08-26

Status: replacement theorem independent of Ansari's disputed ternary induction. Two tiers are recorded:

1. a self-contained finite-prefix certificate through \(10^6\), and
2. a stronger theorem taking Barina's published verification below \(2^{71}\) as a finite external input.

Neither tier proves the Collatz conjecture.

## 1. Shortcut map and odd-prefix count

Use

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Let \(q_j(n)\) be the number of odd terms among

\[
n,T(n),\ldots,T^{j-1}(n).
\]

A positive integer \(n>1\) is recursive if its orbit merges with that of a smaller positive integer. A proper set \(F\subset\mathbb N\) is recursively sufficient (RS) when every member of \(\mathbb N\setminus F\) greater than one is recursive.

## 2. General finite-base parity-RS lemma

Assume every positive integer \(x\le B\) is already known to converge, where \(B\ge3\). Let \(p,d\) be positive integers satisfying

\[
\boxed{(3B+1)^p<2^dB^p.}
\]

For \(m\ge1\), define

\[
V_m(B;p,d)
=
\{n\ge1:d\,q_j(n)>p\,j\text{ for every }1\le j\le m\}.
\]

Then every \(V_m(B;p,d)\) is recursively sufficient.

### Proof

Take \(n>1\) outside \(V_m\), and choose a failing prefix \(j\le m\):

\[
dq_j\le pj.
\]

If \(n\le B\), the finite-base hypothesis gives convergence, hence recursion.

Suppose \(n>B\). If any earlier iterate is already below \(n\), then \(n\) is recursive. Otherwise every iterate in the prefix is at least \(n>B\). For every odd iterate \(x\),

\[
\frac{T(x)}x
=
\frac{3+1/x}{2}
<
\frac{3+1/B}{2},
\]

whereas an even step contributes exactly \(1/2\). Therefore

\[
\frac{T^j(n)}n
<
\frac{(3+1/B)^{q_j}}{2^j}.
\]

Since \(dq_j\le pj\) and

\[
(3+1/B)^p<2^d,
\]

we obtain

\[
(3+1/B)^{q_j}\le
(3+1/B)^{pj/d}<2^j.
\]

Hence \(T^j(n)<n\), so \(n\) is recursive. Thus the complement of \(V_m\) is recursive. \(\square\)

This theorem is entirely in the binary parity domain and does not use the disputed ternary Cantor-core entry theorem.

## 3. Self-contained reproducible tier

The companion certificate

`collatz/src/parity_rs_global_coefficient_gate_certificate.py`

exhaustively verifies every starting value

\[
1\le n\le10^6
\]

against the shortcut dynamics using exact Python integers.

It additionally checks directly that, for every

\[
1\le j\le4700,
\]

one fewer odd step than the coefficient-survival threshold is already contracting under the adjusted multiplier \(3+10^{-6}\).

Consequently, without importing any external verification frontier, a hypothetical minimal counterexample would have to satisfy

\[
\boxed{3^{q_j}\ge2^j\qquad(1\le j\le4700).}
\]

This is a finite machine-certified theorem, not an asymptotic statement.

## 4. Published-frontier tier

Barina (2025) reports exhaustive convergence verification below

\[
B=2^{71}.
\]

Take

\[
p=190537,
\qquad
d=301994.
\]

The companion certificate checks exactly

\[
3^{190537}<2^{301994}
\]

and

\[
\boxed{
(3\cdot2^{71}+1)^{190537}
<
2^{301994}(2^{71})^{190537}.
}
\]

Therefore the sets

\[
V_m=
\{n:301994\,q_j(n)>190537\,j\ \forall j\le m\}
\]

are RS, taking the published \(2^{71}\) verification as the finite input.

## 5. Exact transfer to coefficient survival through depth 301,993

For every

\[
1\le j\le301993,
\]

the certificate checks the exact integer implication

\[
301994q>190537j
\quad\Longrightarrow\quad
3^q\ge2^j.
\]

Equivalently, at each such depth the smallest integer allowed by the RS ballot wall is already at or above the exact coefficient-survival wall.

Hence any hypothetical **minimal** Collatz counterexample, if Barina's finite verification below \(2^{71}\) is accepted, must satisfy

\[
\boxed{
3^{q_j}\ge2^j
\qquad
\text{for every }1\le j\le301993.
}
\]

This conclusion is global with respect to the starting integer. It no longer depends on the m44/m45 ternary selector family.

## 6. What this repairs — and what it does not

### Repaired

The disputed implication

\[
\text{minimal counterexample}
\to
\text{Ansari ternary Cantor core}
\]

is no longer needed to obtain a long coefficient-survival gate.

The new valid chain is

\[
\boxed{
\text{verified finite base}
\to
\text{parity RS wall}
\to
\text{global coefficient survival through a finite depth}.
}
\]

This chain stays in one parity-prefix state space, so there is no ternary-to-binary same-address conversion at this stage.

### Not repaired

This does **not** restore the claim that a minimal counterexample belongs to the ternary \(\{0,1\}\) selector family. Consequently, m44/m45 selector-specific calculations remain conditional on a repaired ternary-core theorem.

It also does not extend coefficient survival to arbitrary depth. The wall is finite. A global proof still needs a mechanism that either extends the gate without bound or forces descent/merge before the finite gate expires.

## 7. DSD logical-chain audit

The corrected dependency graph is

\[
\text{global positive integers}
\xrightarrow{\text{finite verified base + RS}}
\text{binary parity survivor language}
\xrightarrow{\text{exact finite comparison}}
\text{coefficient-surviving prefixes}.
\]

No domain switch occurs inside this chain.

The old ternary branch is retained separately as

\[
\text{explicit ternary selector family}
\to
\text{conditional selector calculations},
\]

with no unconditional edge from a global minimal counterexample until the recursive-sufficiency defect is repaired.

## 8. Immediate next task

Re-audit the existing Stage-4 local/window and whole-prefix maximality lemmas by dependency rather than date:

- results using only coefficient survival / parity prefixes can now be attached to the repaired global branch through depth 301,993;
- results using the ternary selector family stay conditional;
- results using the defective repeated L7/L14 pullback stay diagnostic until separately repaired.

The main question is therefore whether the proof-valid coefficient-survival machinery forces a descent or merge **before depth 301,993**, without reintroducing the invalid ternary-core or pullback assumptions.
