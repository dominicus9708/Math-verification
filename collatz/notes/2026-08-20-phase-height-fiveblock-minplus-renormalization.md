# Phase-height five-block min-plus renormalization

Date: 2026-08-20

Status: **exact decomposition theorem + generalized minimal-survivor diagnostics.** This is not a proof of the Collatz conjecture.

## 1. Generalized survivor state

Let

\[
b_k:=\min\{q:3^q\ge2^k\}=\lceil k\log_3 2\rceil.
\]

For a mechanical phase offset \(s\ge0\), incoming surplus \(h\ge0\), and local horizon \(J\), define

\[
\mathcal S_{s,h}(J)
:=
\left\{x\ge1:
q_j(x)\ge b_{s+j}-b_s-h
\text{ for every }1\le j\le J
\right\}.
\]

Its least positive element is

\[
\boxed{\mu_{s,h}(J):=\min \mathcal S_{s,h}(J).}
\]

The ordinary coefficient-survivor inverse is the special case

\[
\mu(J)=\mu_{0,0}(J).
\]

This is the correct state after cutting a coefficient-surviving path at a nonzero mechanical phase.  The previous four mod-32 branches are exactly phase-height states of this form.

## 2. Exact five-step cylinder decomposition

Fix one five-step parity word \(w\).  Let

- \(r_w\in\{1,\ldots,32\}\) be its least positive canonical start representative;
- \(q_w\) be its number of odd steps;
- \(c_w=T^5(r_w)\).

Every positive integer in this cylinder is uniquely

\[
\boxed{x=r_w+32t,\qquad t\ge0,}
\]

and the parity-vector affine identity gives

\[
\boxed{T^5(x)=c_w+3^{q_w}t.}
\]

Put

\[
Q_s:=b_{s+5}-b_s,
\qquad
h':=h+q_w-Q_s.
\]

Let \(\mathcal W_{s,h}\) be the five-step words whose every local prefix stays above the phase-shifted coefficient barrier.  Then for every \(J\ge0\),

\[
\boxed{
\mathcal S_{s,h}(J+5)
=
\bigcup_{w\in\mathcal W_{s,h}}
\left\{
 r_w+32t:
 c_w+3^{q_w}t\in\mathcal S_{s+5,h'}(J)
\right\}.
}
\]

This is an exact set identity.  It is verified independently by

`collatz/src/phase_height_fiveblock_renormalization_certificate.py`.

The certificate exhaustively checks `s=0..10`, `h=0..2`, `J=10` over all positive canonical representatives through `2^10`.

## 3. The four ordinary depth-five branches

At \((s,h)=(0,0)\), exactly four positive residue cylinders survive through depth five:

\[
\boxed{r\in\{7,15,27,31\}\pmod{32}.}
\]

Their exact affine maps are

\[
\begin{aligned}
T^5(7+32t)&=20+81t, &q_5&=4,\\
T^5(15+32t)&=40+81t, &q_5&=4,\\
T^5(27+32t)&=71+81t, &q_5&=4,\\
T^5(31+32t)&=242+243t, &q_5&=5.
\end{aligned}
\]

Since \(b_5=4\), the first three branches enter phase \(s=5\) at height \(h=0\), while the `31 mod 32` branch enters at height \(h=1\).

Thus the sparse-tail four-channel problem is naturally a two-height phase-shifted problem rather than four unrelated scalar functions.

## 4. Exact generalized best-first solver

`collatz/src/phase_height_minimal_survivor.cpp` computes \(\mu_{s,h}(J)\) exactly by the same nonnegative canonical-lift / Dijkstra principle as the ordinary minimal-survivor solver.

Selected exact values for phase `s=5` are

\[
\begin{array}{c|rr}
J&\mu_{5,0}(J)&\mu_{5,1}(J)\\\hline
100&10087&2463\\
150&60975&60975\\
200&837799&837799
\end{array}
\]

However the equality at 150 and 200 is only temporary.  The exact profiles split again:

\[
\mu_{5,0}(216)=1117065,
\qquad
\mu_{5,1}(216)=837799,
\]

and

\[
\mu_{5,0}(220)=1126015,
\qquad
\mu_{5,1}(220)=1117065.
\]

Therefore one unit of incoming surplus is not permanently consumed.  It acts as a phase credit which can disappear on one plateau and reappear on a later one.

This rules out replacing the `31 mod 32` branch by the ordinary scalar \(\mu\) after a fixed bounded transient without proof.

## 5. Safe scalar branch lower bounds

The set recursion gives immediate but deliberately weak scalar lower bounds.  For example, if global depth is \(K=5+J\), then

\[
\boxed{
\mu_7(K)
\ge
7+32
\left\lceil
\frac{\mu_{5,0}(J)-20}{81}
\right\rceil_+.
}
\]

Analogously,

\[
\begin{aligned}
\mu_{15}(K)&\ge15+32\left\lceil\frac{\mu_{5,0}(J)-40}{81}\right\rceil_+,\\
\mu_{27}(K)&\ge27+32\left\lceil\frac{\mu_{5,0}(J)-71}{81}\right\rceil_+,\\
\mu_{31}(K)&\ge31+32\left\lceil\frac{\mu_{5,1}(J)-242}{243}\right\rceil_+.
\end{aligned}
\]

These are rigorous because every valid suffix endpoint is at least the generalized minimum.

They are not sharp.  At `K=200`, for instance, the scalar endpoint minima give only roughly

\[
3.31\times10^5,\ 3.31\times10^5,\ 3.31\times10^5,\ 1.10\times10^5
\]

for the four branches, while the actual global minimum is \(1126015\).

The missing information is exactly the endpoint congruence

\[
T^5(x)\equiv c_w\pmod{3^{q_w}}.
\]

## 6. Why the next min-plus state needs a ternary syndrome

Replacing the suffix set by only its minimum discards the condition

\[
y=c_w+3^{q_w}t.
\]

Consequently the exact recursion for minima must know the least surviving suffix element in specified ternary residue classes, not only the unrestricted minimum.

This identifies the next state extension as

\[
\boxed{
(\text{mechanical phase},\ \text{height/slack},\ \text{ternary congruence syndrome}).
}
\]

This is the min-plus analogue of the Hensel/formation syndrome already present in the finite renewal graph.  It also explains quantitatively why the naive four scalar branch lower bounds leave a large gap.

## 7. Current role in the proof program

The corrected Stage-4 program now has two complementary exact descriptions:

1. **bulk:** selector/coefficient overlap is controlled by Haar/martingale energy;
2. **sparse tail:** canonical minima obey the phase-height five-block set recursion above.

The remaining bridge is to retain enough ternary syndrome information in the sparse min-plus recursion to prevent the scalar lower bound from losing the cross-base exclusion already seen in the finite formation certificates.
