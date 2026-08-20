# Ternary-syndrome min-plus bridge

Date: 2026-08-20

Status: **exact ternary-congruence refinement of the phase-height minimal-survivor solver, closing the first five-block scalar-loss gap.** This is not a proof of the Collatz conjecture.

## 1. Problem left by the phase-height scalar recursion

The five-block decomposition gives, for a surviving first block `w`,

\[
x=r_w+32t,
\qquad
T^5(x)=c_w+3^{q_w}t.
\]

The scalar lower bound retained only the unrestricted suffix minimum
\(\mu_{5,h'}(J)\), but the actual suffix is constrained by

\[
T^5(x)\equiv c_w\pmod{3^{q_w}}.
\]

That discarded congruence is exactly why the previous branch lower bounds were much smaller than the true global minimum.

## 2. Ternary-syndrome survivor minimum

For phase offset \(s\), incoming surplus \(h\), horizon \(J\), and a ternary syndrome \((a,c)\), define

\[
\boxed{
\nu_{s,h}^{(a,c)}(J)
:=
\min\left\{
 x\in\mathcal S_{s,h}(J):
 x\equiv c\pmod{3^a}
\right\}.
}
\]

The ordinary generalized minimum is the special case

\[
\mu_{s,h}(J)=\nu_{s,h}^{(0,0)}(J).
\]

## 3. Exact monotone CRT key

A depth-\(k\) parity cylinder has all starts

\[
x=r+2^k t,
\qquad t\ge0,
\]

where \(r\) is its least positive canonical representative.

Because

\[
\gcd(2^k,3^a)=1,
\]

there is exactly one \(t\pmod{3^a}\) such that

\[
r+2^k t\equiv c\pmod{3^a}.
\]

Hence the least member of the cylinder carrying the requested ternary syndrome is

\[
\boxed{
\kappa_{a,c}(k,r)
=
 r+2^k
 \left[(c-r)(2^k)^{-1}\right]_{3^a}.
}
\]

If a child cylinder is contained in its parent cylinder, then its syndrome-compatible set is also a subset. Therefore

\[
\boxed{
\kappa_{a,c}(k+1,r_{\rm child})
\ge
\kappa_{a,c}(k,r_{\rm parent}).
}
\]

This gives an exact nondecreasing best-first key.

Consequently, Dijkstra/best-first search over the ordinary parity-cylinder tree, ordered by \(\kappa_{a,c}\), returns \(\nu_{s,h}^{(a,c)}(J)\) exactly at the first popped depth-\(J\) node.

Certificate:

`collatz/src/ternary_syndrome_minimal_survivor.py`.

## 4. Exact reconstruction of the four depth-five branches

At ordinary phase \((s,h)=(0,0)\), the four depth-five surviving cylinders are

\[
(r_w,q_w,c_w,h')
\in
\{(7,4,20,0),(15,4,40,0),(27,4,71,0),(31,5,242,1)\}.
\]

For global depth \(K=5+J\), the exact branch minimum is now

\[
\boxed{
\mu_w(K)
=
 r_w
+32\,
\frac{
\nu_{5,h'}^{(q_w,c_w)}(J)-c_w
}{3^{q_w}}.
}
\]

The quotient is an integer by construction.

Therefore

\[
\boxed{
\mu(K)=\min_w\mu_w(K).
}
\]

This is an exact identity, not merely a lower bound.

## 5. Exact finite checks

The new syndrome solver was checked against the direct ordinary best-first solver. It reproduces the same global minimum at every tested depth.

### K = 105

\[
\begin{array}{c|r|r}
r_w&\mu_w(105)&\nu_{5,h'}^{(q_w,c_w)}(100)\\\hline
7&35655&90254\\
15&60975&154345\\
27&57115&144575\\
31&37503&284795
\end{array}
\]

Hence

\[
\boxed{\mu(105)=35655.}
\]

### K = 155

\[
\begin{array}{c|r|r}
r_w&\mu_w(155)&\nu_{5,h'}^{(q_w,c_w)}(150)\\\hline
7&362343&917183\\
15&608111&1539283\\
27&543515&1375775\\
31&270271&2052377
\end{array}
\]

Hence

\[
\boxed{\mu(155)=270271.}
\]

### K = 200

\[
\begin{array}{c|r|r}
r_w&\mu_w(200)&\nu_{5,h'}^{(q_w,c_w)}(195)\\\hline
7&6079559&15388886\\
15&4053039&10259257\\
27&6631675&16786430\\
31&1126015&8550683
\end{array}
\]

Hence

\[
\boxed{\mu(200)=1126015.}
\]

The previous scalar endpoint bounds at this depth were only of order
\(3.31\times10^5,3.31\times10^5,3.31\times10^5,1.10\times10^5\).
The ternary syndrome therefore removes precisely the cross-base information loss identified in the earlier note.

### K = 220

\[
\begin{array}{c|r|r}
r_w&\mu_w(220)&\nu_{5,h'}^{(q_w,c_w)}(215)\\\hline
7&13421671&33973607\\
15&21677295&54870655\\
27&6631675&16786430\\
31&1126015&8550683
\end{array}
\]

Thus

\[
\boxed{\mu(220)=1126015.}
\]

Again this agrees exactly with the direct solver.

## 6. General affine-progression state

A residue modulo \(3^a\) is enough for the first five-block bridge because each first-block endpoint \(c_w\) is already the least nonnegative representative of its progression.

For repeated block renormalization, the safe exact state is slightly stronger:

\[
\boxed{
(A,a):\quad x=A+3^a u,\qquad u\ge0.
}
\]

Intersect this progression with a five-step parity cylinder

\[
x=r_w+32t.
\]

Since \(32\) and \(3^a\) are coprime, their intersection is either empty or, here, a unique progression

\[
\boxed{x=x_0+32\,3^a u.}
\]

Writing

\[
t_0=\frac{x_0-r_w}{32},
\]

the five-step affine map sends it to

\[
\boxed{
y=y_0+3^{a+q_w}u,}
\qquad
 y_0=c_w+3^{q_w}t_0.
\]

Thus the exact block renormalization closes on the state

\[
\boxed{
(\text{mechanical phase},\ \text{height},\ A,\ a).
}
\]

This is the precise ternary-affine syndrome state anticipated by the earlier phase-height note.

## 7. Consequence for the corrected Stage 4 program

The sparse-tail side of the bulk/sparse bridge is now stronger:

1. the phase-height decomposition is exact;
2. the missing ternary congruence can be retained by a monotone CRT key;
3. the four ordinary depth-five branch minima are reconstructed exactly rather than bounded weakly;
4. repeated five-block renormalization has a closed affine-progression state.

The next sparse-tail target is therefore no longer to identify the missing state. It is to compress the affine-progression state space sufficiently to prove a uniform growth lower bound for the least surviving natural start.

That lower bound can then be combined with the existing Haar-controlled bulk estimate to attack the unconditional coefficient-only Stage 4 closure.
