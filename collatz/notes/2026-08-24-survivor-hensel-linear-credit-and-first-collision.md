# Coefficient-survivor Hensel collisions have linear root credit

Date: 2026-08-24

Status: **general algebraic lemma + exact first-collision diagnostic.**  This removes exponential growth from the Hensel/endpoint multiplicity channel among coefficient-surviving root prefixes.  It does not by itself control the remaining ternary-selector / dyadic same-address correlation and is not a proof of the Collatz conjecture.

## 1. Correction bound for every coefficient-surviving word

Take a length-H parity word with q odd positions

\[
0\le k_1<\cdots<k_q\le H-1
\]

and affine correction

\[
R=\sum_{j=1}^q3^{q-j}2^{k_j}.
\]

If the word survives the coefficient barrier at every prefix, then immediately before its j-th odd event there have been j-1 odd events.  Hence

\[
2^{k_j}\le3^{j-1}.
\]

Therefore every summand satisfies

\[
3^{q-j}2^{k_j}\le3^{q-1},
\]

and consequently

\[
\boxed{R\le q\,3^{q-1}.}
\]

For q>0 the inequalities cannot all be simultaneously extremal in a way that affects the strict difference estimate below; the coarse displayed upper bound is sufficient.

## 2. Linear credit between surviving Hensel siblings

Let two distinct coefficient-surviving length-H words have the same q and the same complete Hensel residue,

\[
R'\equiv R\pmod{3^q},
\qquad R'>R.
\]

Write

\[
R'-R=3^q d,
\qquad d\in\mathbb Z_{>0}.
\]

Since both corrections lie in the interval

\[
0<R,R'\le q3^{q-1},
\]

we obtain

\[
3^q d=R'-R<q3^{q-1},
\]

hence

\[
\boxed{0<d<\frac q3.}
\]

This is much stronger than the unrestricted whole-word estimate

\[
d<2^{H-q}.
\]

The improvement comes entirely from requiring both words to remain inside the coefficient-surviving language.

## 3. Minimal-counterexample consequence

For a hypothetical minimal counterexample N, if

\[
q<3N,
\]

then every positive survivor-sibling credit automatically obeys

\[
d<N.
\]

The smaller root

\[
M=N-d>0
\]

reaches the same H-step endpoint because

\[
R'-R=3^qd.
\]

Thus at every horizon satisfying q<3N, a minimal counterexample must be the maximum-correction representative **among coefficient-surviving words** in its fixed (q,R mod 3^q) class.

For the current m=45 core,

\[
N>2^{73},
\]

so this condition is valid throughout any proof horizon remotely comparable with the current Euclidean gates (hundreds or thousands of steps); the formal threshold q<3N is astronomically larger.

This statement does not require the unrestricted alternate word used by the stronger whole-prefix maximality filter to remain coefficient-surviving.

## 4. Endpoint/Hensel multiplicity becomes polynomial

Fix H and an endpoint y.  For a fixed q, two coefficient-surviving preimages of y satisfy

\[
2^Hy=3^qN_i+R_i.
\]

If there are several such states, the one with larger correction has smaller root start.  By the linear-credit lemma above, throughout q<3N only that maximum-correction surviving representative can remain a minimal-counterexample candidate.

There are at most

\[
H-\lceil H\log_3 2\rceil+1=O(H)
\]

terminal q-values compatible with coefficient survival.  Therefore the relevant survivor Hensel/endpoint fibre has at most O(H) Pareto candidates and contributes only

\[
\boxed{O(\log H)=o(H)}
\]

information bits.

Thus this channel has zero exponential rate without needing all-H injectivity of the raw survivor Hensel code.

## 5. Exact first raw survivor-Hensel collision

Direct exact scans show raw injectivity of

\[
w\mapsto(q,R(w)\bmod3^q)
\]

for every coefficient-surviving word through H=33.

At H=34 the first collision appears in the minimum terminal layer q=22.

Exact counts:

\[
\boxed{39,993,895}
\]

coefficient-surviving q=22 words, with exactly

\[
\boxed{5}
\]

Hensel residue pairs colliding.

All five collision pairs satisfy exactly

\[
\boxed{R'-R=4\,3^{22}},
\]

so their root credit is

\[
\boxed{d=4}.
\]

The next checked layers q=23 and q=24 at H=34 remain raw-injective.

This first failure is therefore not an exponential multiplicity event; it is a five-pair resonance carrying a tiny linear credit.

## 6. Relation to the remaining Stage-4 obstruction

The result separates two questions that were previously mixed together.

1. **Hensel/endpoint multiplicity among surviving binary histories:** now polynomially compressed by the q/3 credit theorem.
2. **Whether the fixed ternary selector family keeps landing on the surviving dyadic addresses:** still unresolved and genuinely cross-base.

Thus the remaining exponential obstruction is not an uncontrolled proliferation of Hensel syndrome states.  It is the selector-to-address correlation itself.
