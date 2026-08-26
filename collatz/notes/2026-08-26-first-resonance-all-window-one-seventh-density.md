# First resonance: all-window closure and one-seventh displacement density

Date: 2026-08-26

Status: **exact local certificate + exact combinatorial globalization.** This does not prove the Collatz conjecture.

## 1. Local certified input

The support-6 base-shell certificate proves that whenever a full 49-odd-state block starts at a base-shell position

\[
d_i=0,
\]
then that block cannot contain six or fewer positive displacements. Hence

\[
\boxed{
d_i=0
\Longrightarrow
\sum_{j=i}^{i+48}\mathbf 1_{\{d_j>0\}}\ge7.
}
\]

## 2. Zero-start window closure lemma

Let \(s_j\in\{0,1\}\). Suppose every length-\(L\) window beginning with \(s_i=0\) contains at least \(m\) ones.

Then **every** length-\(L\) window contains at least \(m\) ones.

Proof.  Suppose a window

\[
W=[i,i+L-1]
\]
begins with one but contains at most \(m-1\) ones.  Let \(j>i\) be the first zero in the window and put \(r=j-i\).  The first \(r\) positions are ones, so the overlap

\[
[j,i+L-1]
\]
contains at most \(m-1-r\) ones.  But the zero-start window

\[
W'=[j,j+L-1]
\]
must contain at least \(m\) ones.  Its new tail

\[
[i+L,j+L-1]
\]
has only \(r\) positions, yet would need at least

\[
m-(m-1-r)=r+1
\]
ones, impossible.  If the original window contains no zero, it already contains \(L\ge m\) ones.  Therefore the claim follows.

This lemma is independent of Collatz dynamics.

## 3. Application to the first resonance

Take

\[
L=49,
\qquad m=7.
\]

The local certified rule therefore upgrades to

\[
\boxed{
\text{every full 49-odd-state window contains at least 7 positive }d_j.
}
\]

Let

\[
R=r_*:=\#\{0\le j<Q:d_j>0\}.
\]

There are \(Q-48\) full 49-state windows.  Summing their positive counts gives at least

\[
7(Q-48).
\]

A fixed positive position occurs in at most 49 windows, hence

\[
7(Q-48)\le49R.
\]

With

\[
Q=72,057,431,991,
\]
we obtain

\[
\boxed{
R\ge10,293,918,849.
}
\]

Thus more than 14.285714 percent of all first-resonance odd ordinals must lie above the base dyadic shell.

## 4. Defect reserve

Every positive displacement contributes strictly more than \(1/12\) to the normalized Christoffel defect lower bound. Therefore

\[
\boxed{
\frac{E}{3^Q}
>
\frac{10,293,918,849}{12}
=
857,826,570.75.
}
\]

This is still below the certified upper budget

\[
4,314,000,000,
\]
so further structure is required.  But the previous lower bound \(r_*\ge22\) has now been replaced by a global density theorem of order \(Q\).

## 5. DSD logic chain

The chain is now

\[
\boxed{
\text{dyadic shell }d=0
\to
\text{finite 49-state quotient}
\to
\text{zero-start forbidden pattern}
\to
\text{all-window closure}
\to
\text{global }1/7\text{-scale shell-escape density}
\to
\text{defect reserve}.
}
\]

The next proof target is to replace the binary indicator \(\mathbf1_{d>0}\) by a weighted local potential which retains the actual displacement charge \(1-2^{-d}\), Hensel alignment credit, and ordering debt.  That is the natural route toward the remaining first-resonance Bellman gap.

Companion certificates:

- `collatz/src/first_resonance_base_shell_support6_local_certificate.cpp`
- `collatz/src/first_resonance_all_window_density_certificate.py`
