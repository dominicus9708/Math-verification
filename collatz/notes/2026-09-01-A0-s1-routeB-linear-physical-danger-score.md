# A0 s=1 Route-B — linear physical danger score

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Result

The general adaptive state may require a Pareto frontier in source lower
endpoint and defect.

For the **specific certified physical real-envelope rejection predicate**, that
frontier collapses exactly to one scalar Bellman label.

This removes the joint-frontier-width obstruction for this predicate.

Source:

`collatz/src/A0_s1_routeB_linear_physical_danger_score_certificate.py`

---

## 2. Directed physical inequality

Use the already certified directed quantities on the fixed-point scale

\[
Q=2^{256}.
\]

They satisfy

\[
\lambda
\ge
\frac{m_{lo}}Q,
\]

\[
\delta
\ge
\frac{\delta_{lo}}Q,
\]

and

\[
c_{th}
\le
\frac{c_{hi}}Q.
\]

Also

\[
L_-\le L_{max}.
\]

For a target-dominance candidate with normalized defect \(\eta\),

\[
c_{cand}
\le
c_{th}-\lambda\eta.
\]

The bridge identity gives

\[
\delta X
=L_-+c_{cand}.
\]

Therefore

\[
\frac{\delta_{lo}}Q X
\le
L_{max}
+
\frac{c_{hi}}Q
-
\frac{m_{lo}}Q\eta.
\]

If a whole source family satisfies

\[
X\ge X_{lo},
\]

then it is impossible whenever

\[
\boxed{
m_{lo}\eta+\delta_{lo}X_{lo}
>
L_{max}Q+c_{hi}.}
\]

Define

\[
\boxed{B=L_{max}Q+c_{hi}.}
\]

This is a direct directed-rational closure test.  It does not require the
intermediate fixed-point flooring used by the older `x_upper_from_eta`
implementation.

---

## 3. Integer score

From the integer defect coordinate

\[
N=3^q\eta,
\]

multiply the closure inequality by \(3^q\):

\[
m_{lo}N
+
\delta_{lo}3^qX_{lo}
>
B3^q.
\]

Define the physical danger score

\[
\boxed{
P
=
m_{lo}N
+
\delta_{lo}3^qX_{lo}.
}
\]

The whole family closes exactly under this directed gate when

\[
\boxed{P>B3^q.}
\]

For histories in one exact future-control state, \(q\) is common, so the
history with the smallest \(P\) is the hardest one to reject.

---

## 4. Source interval update

Write the current source family as

\[
X=r+2^h m,
\qquad
m\in[L,U].
\]

Thus

\[
X_{lo}=r+2^hL.
\]

Expose the next parameter bit

\[
\epsilon\in\{0,1\}
\]

and write

\[
m=\epsilon+2k.
\]

The child quotient interval has lower endpoint

\[
L'
=
\left\lceil\frac{L-\epsilon}{2}\right\rceil.
\]

The source residue becomes

\[
r'=r+\epsilon2^h.
\]

Hence

\[
X'_{lo}-X_{lo}
=
2^h\left(\epsilon+2L'-L\right).
\]

Put

\[
\boxed{
\chi
=
\epsilon+2L'-L
\in\{0,1\}.}
\]

Then

\[
\boxed{X'_{lo}=X_{lo}+\chi2^h.}
\]

The source lower endpoint either stays fixed or rises by exactly one current
source modulus unit.

---

## 5. Scalar Bellman transition

### Emitted parity `0`

Here

\[
q'=q,
\qquad
N'=N.
\]

Therefore

\[
\boxed{
P'
=
P
+
\delta_{lo}3^q\chi2^h.
}
\]

This is

\[
P'=P+\text{common constant}.
\]

### Emitted parity `1`

Let the new ranked target one be at \(a_{q+1}\).

Then

\[
N'
=
3N+2^{a_{q+1}}-2^h,
\]

and

\[
q'=q+1.
\]

Hence

\[
\boxed{
P'
=
3P
+m_{lo}\left(2^{a_{q+1}}-2^h\right)
+
\delta_{lo}3^{q+1}\chi2^h.
}
\]

Thus

\[
P'=3P+\text{common constant}.
\]

In either branch, the coefficient of the old score is positive.

---

## 6. Exact scalar dominance

Suppose two histories share

- the same exact future-control key;
- the same exact parameter-interval payload;
- scores \(P_1\le P_2\).

Every common next parameter bit maps them by the same affine function

\[
P\mapsto P+c
\]

or

\[
P\mapsto3P+c.
\]

Therefore

\[
P_1\le P_2
\Longrightarrow
P_1'\le P_2'.
\]

The ordering is permanent through every common future suffix.

Consequently all histories except

\[
\boxed{P_{min}}
\]

may be discarded for this physical gate.

The previous Pareto frontier

\[
\mathcal F_{r,N}
\]

is still the correct general state if \(r\) and \(N\) are queried separately
elsewhere.  But the physical defect gate itself sees only their positive linear
combination \(P\).

---

## 7. State-count consequence

For the restricted active predicates

1. source transition;
2. strict ballot;
3. exact interval payload;
4. physical defect rejection;

use the key

\[
(Y,q,\text{payload})
\]

and one scalar label \(P_{min}\).

At future layer \(i\),

\[
(Y,q)
\]

has at most

\[
2^{D-i}(i+1)
\]

values.

The exact interval theorem contributes at most four payload states.

Therefore

\[
\boxed{
n_i
\le
\min\left(
2^i,
4\,2^{D-i}(i+1)
\right).}
\]

Again the danger score is a label, not a state dimension.

Using the square-root bound,

\[
\boxed{
N_{DAG}
\le
2^{D/2+1}(D+1)^{3/2}.
}
\]

This remains exponential in half the future depth, but the earlier joint
source/defect Pareto-width factor has disappeared completely for the physical
defect predicate.

---

## 8. Regression

The certificate uses first-defect shapes

\[
f=2,5,8,
\]

the parameter interval

\[
3\le m\le200,
\]

and eight future parameter bits.

At every layer and every exact control/payload key it compares

1. every raw history's directly reconstructed \((r,N)\);
2. the corresponding direct physical score \(P\);
3. the recursively propagated minimum scalar score.

The scalar DP equals the direct minimum in every tested state.

It also verifies that

\[
P_{min}>B3^q
\]

is equivalent to **all raw histories in that key** satisfying the same directed
physical closure test.

---

## 9. DSD audit

### EXACT / CLOSED

- the directed real-envelope gate is one positive linear inequality in
  \((X_{lo},\eta)\);
- after integer normalization it becomes the scalar score \(P\);
- common source refinements map \(P\) by an order-preserving affine function;
- one minimum score per exact control/payload state is sufficient;
- the joint Pareto frontier is unnecessary for this active predicate;
- adaptive source refinement remains available because the interval lower
  endpoint contribution is included directly in \(P\).

### SCOPE LIMIT

The scalarization is predicate-specific.

If another active theorem separately queries

- source residue \(r\);
- defect numerator \(N\);
- correction/projective residue;
- checkpoint/C4F information;

those coordinates must remain in the exact key or in an appropriate companion
state.

### NOT INFERRED

- closure of all 14 roots;
- bounded growth after adding all remaining membership predicates;
- Collatz.

---

## 10. Updated bottleneck

The source + physical-defect part is now reduced to

\[
\boxed{
(\text{exact active control},\text{interval payload},P_{min}).
}
\]

The next step is no longer a source/defect frontier problem.

It is to add the **smallest exact projective/checkpoint observation coordinate
that can force additional defect or reject a family**, and measure whether that
augmented state still merges fast enough across the 14-root forest.
