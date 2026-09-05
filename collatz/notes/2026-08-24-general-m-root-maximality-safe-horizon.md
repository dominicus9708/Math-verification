# General-m linear safe horizon for whole-prefix root maximality

Date: 2026-08-24

Status: **exact algebraic globalization lemma for root-credit validity.**  The fixed m=45 depth-200 theorem is one instance of a general linearly growing safe horizon.  This does not prove the Collatz conjecture or the remaining selector/dyadic transfer theorem.

## 1. General recursively sufficient family

Use the recursively sufficient depth-m family

\[
N=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Every such root satisfies

\[
\boxed{N\ge N_{\min}(m):=4\cdot3^m+3.}
\]

The m=45 two-affine-block notation used elsewhere is the same family with the top free digit separated as \(a_{44}=b\).

## 2. Universal complete-prefix credit bound

For a length-H word with q odd entries, the largest possible correction is

\[
R_{\max}(H,q)=2^{H-q}(3^q-2^q).
\]

Hence if another complete q-odd word lies in the same Hensel class and has

\[
R'-R=3^q d,
\qquad d>0,
\]

then

\[
\boxed{0<d<2^{H-q}.}
\]

Coefficient survival through H forces

\[
q\ge q_{\min}(H):=\min\{q:3^q\ge2^H\}
=\lceil H\log_3 2\rceil.
\]

Therefore every positive complete-prefix root credit on the coefficient-surviving language obeys

\[
\boxed{
d<2^{H-q_{\min}(H)}.
}
\]

## 3. Exact general safe horizon

Define

\[
\boxed{
H_{\rm safe}(m)
:=\max\left\{H:
2^{h-q_{\min}(h)}<N_{\min}(m)
\text{ for every }1\le h\le H
\right\}.
}
\]

For every recursively sufficient depth-m root and every coefficient-surviving prefix with

\[
H\le H_{\rm safe}(m),
\]

any positive larger complete-prefix correction has root credit \(d<N\).  Thus the smaller root

\[
M=N-d>0
\]

is valid and reaches the same H-step endpoint.

Consequently, a hypothetical minimal counterexample in the depth-m core must be complete-prefix maximum-correction through the entire safe horizon.

Selected exact values are

\[
\begin{array}{c|r}
m&H_{\rm safe}(m)\\\hline
10&48\\
20&92\\
30&135\\
40&178\\
45&200\\
46&203\\
50&222\\
60&265\\
100&436
\end{array}
\]

In particular the previously proved m=45 depth-200 range is exactly recovered.

## 4. Asymptotic slope

Write

\[
\alpha:=\log_3 2.
\]

Since

\[
\log_2N_{\min}(m)
=m\log_2 3+2+o(1)
\]

and

\[
H-q_{\min}(H)
=(1-\alpha)H+O(1),
\]

the safe-horizon definition gives

\[
\boxed{
\frac{H_{\rm safe}(m)}m
\longrightarrow
\rho
:=\frac{\log_2 3}{1-\log_3 2}.
}
\]

Numerically,

\[
\boxed{
\rho\approx4.29447379207261.
}
\]

Thus whole-prefix root maximality is not merely a fixed-m finite tool.  It remains automatically root-valid to a binary horizon **linear in the ternary selector depth m**, with asymptotic coefficient about 4.29447.

## 5. Interaction with terminal propagation

The terminal-propagation theorem states that maximum-correction at a terminal safe horizon implies maximum-correction at every earlier prefix.

Therefore for general m the entire linearly long safe strip collapses to one terminal condition at

\[
H=H_{\rm safe}(m).
\]

A minimal counterexample in the recursively sufficient depth-m core must lie in

\[
\boxed{
\mathcal C_m
\cap
\mathcal S_{H_{\rm safe}(m)}
\cap
\mathcal M_{H_{\rm safe}(m)}.
}
\]

This is the direct globalization of the m=45 terminal-intersection formulation.

## 6. Strategic consequence

The remaining globalization problem should no longer treat root-credit validity as an independent all-H obstruction.  On each depth-m recursively sufficient core there is already a linearly growing interval of binary time on which complete-prefix predecessor arguments are automatically valid.

What remains is to control the same-integer intersection of

1. the ternary selector family \(\mathcal C_m\),
2. coefficient survival to a horizon \(\asymp4.29447m\), and
3. terminal complete-Hensel maximality.

If that terminal intersection can be shown to shrink uniformly in m, the root-credit part of the globalization is already supplied by this lemma.

Certificate:

`collatz/src/general_m_root_maximality_safe_horizon_certificate.py`.
