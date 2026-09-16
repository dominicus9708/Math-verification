# E/O plane and affine-matrix audit

Date: 2026-08-09

Status: **THEOREM (external) + DERIVED LEMMA + COMPUTATIONAL CHECK + SCOPE CORRECTION**

This note records how the current two-channel `even/odd` picture fits the existing Collatz verification program.  It is intentionally conservative: the parity-vector affine formula and its extremal remainder order are treated as known mathematics, while only the reformulation and exact finite checks are project-derived.

## 1. Accelerated map and two-channel projection

Use

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a parity word `w=(v_0,...,v_{h-1})`, let

\[
e(w)=\#\{i:v_i=0\},\qquad q(w)=\#\{i:v_i=1\},\qquad h=e+q.
\]

The map

\[
\pi(w)=(e,q)
\]

is only a coarse count-plane projection.  It forgets order.  The coefficient character

\[
\chi(w)=2^{-e}(3/2)^q=\frac{3^q}{2^h}
\]

depends only on this projection.

Thus the temporary E/O plane is best interpreted as the **abelianized coefficient plane**, not as a replacement for the parity word.

## 2. Exact affine matrix lift

Introduce homogeneous coordinates and the two generators

\[
M_E=\begin{pmatrix}1/2&0\\0&1\end{pmatrix},\qquad
M_O=\begin{pmatrix}3/2&1/2\\0&1\end{pmatrix}.
\]

If the time-ordered word is `w=v_0...v_{h-1}`, then

\[
M_w=M_{v_{h-1}}\cdots M_{v_0}
=\begin{pmatrix}
3^q/2^h&R(w)/2^h\\
0&1
\end{pmatrix},
\]

where, if the odd positions are

\[
0\le d_1<\cdots<d_q<h,
\]

then

\[
\boxed{R(w)=\sum_{i=1}^q 2^{d_i}3^{q-i}.}
\]

Hence

\[
\boxed{T^h(n)=\frac{3^q n+R(w)}{2^h}.}
\]

This is the classical parity-vector affine formula in matrix form.  The diagonal entry is the E/O count channel; the upper-right entry is the order-sensitive correction channel.

## 3. Cocycle law

Write an affine state as `(chi,beta)` with

\[
F_w(n)=\chi(w)n+\beta(w),\qquad \beta(w)=R(w)/2^h.
\]

For a time concatenation `uv` (first `u`, then `v`),

\[
\chi(uv)=\chi(v)\chi(u),
\]

\[
\boxed{\beta(uv)=\chi(v)\beta(u)+\beta(v).}
\]

Therefore the correction is not an independent third coordinate: it is a positive affine cocycle over the count-plane coefficient character.

## 4. Matrix proof of the local parity-order inequality

The generator commutator is

\[
M_O M_E-M_E M_O
=\begin{pmatrix}0&1/4\\0&0\end{pmatrix}.
\]

Let two words have the same prefix `p` and suffix `s`, but differ locally by `EO` versus `OE`.  Then

\[
M_s(M_O M_E-M_E M_O)M_p
=\begin{pmatrix}0&\chi(s)/4\\0&0\end{pmatrix}.
\]

Since \(\chi(s)>0\), moving an odd step one place to the **right** (`OE -> EO` in time order) strictly increases the final correction.

Repeated adjacent swaps recover the standard extremal order for fixed `(h,q)`:

\[
R_{\min}=3^q-2^q
\]

at the time word `O^q E^e`, and

\[
R_{\max}=2^e(3^q-2^q)
\]

at the time word `E^e O^q`.

This is equivalent to the remainder ordering proved by Rozier--Terracol; the matrix commutator gives a compact derivation of the adjacent-swap step.

## 5. First coefficient crossing as a constrained fiber

Let a **first coefficient crossing** occur at length \(\sigma\) with `q` odd entries:

\[
3^{q_k}\ge2^k\quad(1\le k<\sigma),
\qquad
3^q<2^\sigma.
\]

Then necessarily

\[
\boxed{\sigma=\lceil q\log_2 3\rceil.}
\]

For zero-based odd positions `d_i` (`i=0,...,q-1`), prefix admissibility is equivalent to

\[
\boxed{d_i\le\lfloor i\log_2 3\rfloor.}
\]

Because shifting an odd step to the right increases `R`, the maximal correction in this constrained first-crossing fiber is attained by the mechanical boundary word

\[
\boxed{d_i^*=\lfloor i\log_2 3\rfloor.}
\]

This connects the E/O count plane directly to the existing `mechanical-boundary` and `buffered-core` notes.

## 6. Crossing coordinates

Define

\[
\delta=\frac{2^\sigma}{3^q}-1>0,
\qquad
S(w)=\frac{R(w)}{3^q}.
\]

Then the crossing matrix gives

\[
\boxed{T^\sigma(x)=\frac{x+S(w)}{1+\delta}.}
\]

Therefore non-descent at the first coefficient crossing is equivalent to

\[
\boxed{x\le\frac{S(w)}{\delta}.}
\]

The coarse E/O plane controls \(\delta\); the parity-order fiber controls \(S\).  This is the cleanest two-channel decomposition for the current proof program.

## 7. Scope correction: what one boundary path can and cannot prove

The mechanical boundary word is sufficient to maximize the correction **for a fixed first coefficient crossing**.  It therefore gives a valid worst-case upper bound for a hypothetical paradoxical first crossing.

It does **not** represent all coefficient-surviving parity words.  At an intermediate depth

\[
a_h=\lceil h\log_3 2\rceil,
\qquad
s_h=q_h-a_h\ge0,
\]

surviving words can occupy positive slack layers `s_h>0`.  Those layers are essential for the infinite-coefficient-survival branch and for exact minimal-survivor calculations.  They are already tracked in:

- `logarithmic-slack-reduction.md`;
- `minimal-survivor-minplus-status.md`;
- `slack_transfer.py` and the minimal-survivor solvers.

Accordingly, a computation following only the single mechanical boundary must be labelled as a **first-crossing extremal check**, not as a global enumeration of all surviving paths or as a proof of growth of the minimal-survivor function \(\mu(k)\).

## 8. Independent exact finite checks

Two independent calculations were performed on 2026-08-09:

1. exact Python integer enumeration (see `collatz/src/eo_matrix_audit.py`);
2. Wolfram Language exact enumeration for `q=1,...,8`.

For each `q`, Wolfram found that the mechanical first-crossing word is admissible and has the maximal `R` among all first-crossing words:

| q | sigma | admissible words | max R |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 1 | 5 |
| 3 | 5 | 2 | 23 |
| 4 | 7 | 3 | 85 |
| 5 | 8 | 7 | 319 |
| 6 | 10 | 12 | 1085 |
| 7 | 12 | 30 | 3767 |
| 8 | 13 | 85 | 13349 |

The Python verifier additionally checks the parity-residue bijection and the fixed-cell global extrema.

## 9. Finite 20,000-step first-crossing check

For the mechanical first-crossing extrema with \(\sigma\le20000\), exact integer comparison against the peer-reviewed Barina verification threshold \(2^{71}\) gives

\[
R^*(q)<2^{71}(2^\sigma-3^q)
\]

for every first-crossing pair in this finite range.

The largest ratio encountered is at

\[
\boxed{\sigma=19457,\qquad q=12276,}
\]

with

\[
\frac{R^*}{2^\sigma-3^q}
\approx1.2483181513\times10^7
\quad(\log_2\approx23.57348).
\]

Thus a **minimal Collatz counterexample larger than \(2^{71}\)** cannot have its first coefficient crossing at any depth \(\sigma\le20000\): if it did, even the maximal admissible correction would force descent below the starting value.

This is a finite derived consequence, not an asymptotic theorem and not a statement that all coefficient-surviving words through depth 20,000 have starting value above \(2^{71}\).

## 10. Proof-program consequence

The E/O matrix picture should be retained as a front-end organization layer:

\[
\boxed{
\text{count plane }(h,q)
\;\longrightarrow\;
\text{slack }s
\;\longrightarrow\;
\text{correction fiber }R
\;\longrightarrow\;
\text{canonical residue }r.
}
\]

The existing stronger machinery should remain authoritative for the hard steps:

- first-crossing extremum: mechanical boundary / remainder majorization;
- finite-crossing reduction: buffered core and core reconstruction;
- infinite coefficient survival: minimal-survivor / slack-transfer program;
- arithmetic realization: canonical residue and cross-base constraints.

The next useful matrix work is therefore **not** to collapse the slack fibers to one path, but to build a block transfer operator whose state retains `(slack, carry/residue, correction interval)` while using the E/O count plane only as the coarse coordinate.

## References used for the audit

- R. Terras, *A stopping time problem on the positive integers*, Acta Arithmetica 30 (1976).
- O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948 (2025), especially the parity-vector remainder order and extrema.
- D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI 10.1007/s11227-025-07337-0.
