# First resonance: support-5 local exclusion and global displacement density

Date: 2026-08-26

Status: **exact finite local certificate + exact combinatorial globalization.** No Collatz proof is claimed.

## 1. Local finite quotient

At a base-shell odd state \(d_i=0\), inspect 49 consecutive odd states.  Under the ordering rule

\[
d_{j+1}\le d_j+g_j-1,
\qquad g_j\in\{1,2\},
\]

the companion certificate exhausts every path with at most five positive displacement states in that 49-state window.

Exact quotient sizes are

\[
\boxed{11,642,760}
\]
raw displacement paths,

\[
\boxed{7,607,777}
\]
distinct 73-bit parity words,

\[
\boxed{3,170,816}
\]
canonical ordinary starts in

\[
2^{71}<x<\frac83 2^{71}.
\]

All of them descend below \(2^{71}\).  The largest exact accelerated stopping depth is

\[
\boxed{367}
\]
at

\[
\boxed{2689857621321589958523}.
\]

Therefore every hypothetical first-resonance counterexample satisfies the local rule

\[
\boxed{
d_i=0
\Longrightarrow
\#\{j\in[i,i+48]:d_j>0\}\ge6
}
\]
for every full 49-state window.

## 2. Global double counting

Let \(R=r_*\) be the total number of positive displacement positions and \(Z=Q-R\) the number of zeros.  At most 48 zeros occur too close to the terminal boundary to start a full 49-state window.  Hence at least

\[
Q-R-48
\]
zero positions trigger the local rule.

Count incidences between these zero-start windows and positive positions.  Each triggered window contains at least six positive positions, while one positive position lies in at most 49 such windows.  Therefore

\[
6(Q-R-48)\le49R.
\]

Thus

\[
\boxed{
R\ge
\left\lceil\frac{6(Q-48)}{55}\right\rceil
=7,860,810,758.
}
\]

For

\[
Q=72,057,431,991,
\]
this is a positive-displacement density above 10.909 percent.

## 3. Immediate defect consequence

Every positive displacement contributes strictly more than \(1/12\) to the normalized Christoffel defect lower bound.  Hence

\[
\boxed{
\frac{E}{3^Q}
>
\frac{7,860,810,758}{12}
=
655,067,563.166\ldots
}
\]

This remains below the first-resonance upper budget \(4,314,000,000\), so it does not close the resonance by itself.  Its role is to convert a finite shell quotient into a global positive-density theorem.

## 4. DSD proof-chain role

The reduction is

\[
\text{base-shell state}
\to
\text{finite local quotient}
\to
\text{forbidden low-support pattern}
\to
\text{window incidence count}
\to
\text{global displacement density}
\to
\text{defect reserve}.
\]

The next target is not merely to increase the support cutoff one unit at a time.  The more useful extension is a weighted local Bellman certificate which records the actual charge \(1-2^{-d_j}\) and the ordering debt carried across the window.

Companion certificates:

- `collatz/src/first_resonance_base_shell_support5_local_certificate.cpp`
- `collatz/src/first_resonance_support5_global_density_certificate.py`
