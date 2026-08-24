# Stage 4 joint-scaling quantifier audit

Date: 2026-08-25

Status: **logical audit/correction of the Stage 4 asymptotic target.  This is not a proof of the Collatz conjecture.**

## 1. Why the fixed-m limsup is not the right independent bridge

Recall

\[
\Xi_{m,H}
=
\frac{|\mathcal C_m\cap\mathcal L_H|/|\mathcal C_m|}
{|\mathcal L_H|/2^H},
\]

where \(\mathcal C_m\) is the fixed ternary selector layer

\[
\mathcal C_m
=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}
\]

and \(\mathcal L_H\) is the coefficient-surviving, aligned-L7 residue-maximal dyadic language through depth \(H\).

The note `2026-08-19-stage4-strengthened-by-l7-residue-maximality.md` formulated the sufficient target

\[
\limsup_{H\to\infty}
\frac{\log_2\Xi_{m,H}}{H}<\frac7{50}.
\]

If this is read with \(m\) fixed, however, it is essentially an eventual-extinction statement for the finite set \(\mathcal C_m\), not an independent transversality theorem.

Indeed, let

\[
I_{m,H}:=|\mathcal C_m\cap\mathcal L_H|.
\]

The L7 macro theorem gives a uniform exponential language-density loss

\[
\frac{|\mathcal L_H|}{2^H}
\le 2^{-\eta H+O(1)}
\]

for some certified \(\eta>7/50\), after harmless finite prefix/boundary constants are absorbed into \(O(1)\).

If one fixed selector integer survives every depth, then

\[
I_{m,H}\ge1
\]

for every \(H\), and since \(|\mathcal C_m|=2^m\),

\[
\Xi_{m,H}
\ge
2^{-m}\,2^{\eta H-O(1)}.
\]

Therefore

\[
\limsup_{H\to\infty}
\frac{\log_2\Xi_{m,H}}H
\ge\eta>\frac7{50}.
\]

Conversely, if no member of the finite set \(\mathcal C_m\) survives every depth, then each member is excluded at some finite depth.  Taking the maximum of those finitely many exclusion depths gives

\[
I_{m,H}=0
\]

for all sufficiently large \(H\).  With the convention \(\log 0=-\infty\), the fixed-m limsup condition then holds trivially.

Hence the fixed-m statement must not be presented as the missing independent cross-base theorem.

## 2. The recursive-sufficiency scaling is joint, not fixed

The recursively sufficient Cantor-core reduction gives, for a hypothetical minimal first-crossing candidate of order \(\sigma\), the all-range magnitude bound

\[
x=O(\sigma^{14.3}).
\]

Every point in selector layer \(m\) satisfies

\[
x\ge4\,3^m+3.
\]

Consequently

\[
m
\le
\log_3 x+O(1)
\le
\frac{14.3}{\log_2 3}\log_2\sigma+O(1).
\]

Thus the unconditional scale constant is

\[
\boxed{
K_{\rm all}
:=\frac{14.3}{\log_2 3}
\approx9.022295476071843.
}
\]

If the stronger asymptotic linear-form exponent used in the earlier growth note is inserted with an explicit effective threshold, then

\[
x=O(\sigma^{8.616})
\]

gives

\[
\boxed{
K_{\rm asym}
:=\frac{8.616}{\log_2 3}
\approx5.436090756771677.
}
\]

For a hard prefix horizon \(H=\sigma+O(1)\), replacing \(\sigma\) by \(H\) changes only the additive \(O(1)\) term in \(m\).

Therefore the global proof problem only needs uniform control in the joint regime

\[
\boxed{
m\le K\log_2H+C,}
\]

with \(K=K_{\rm all}\) for the unconditional all-range formulation, or the smaller asymptotic constant after its effective threshold has been made explicit.

## 3. Corrected Stage 4 transversality target

A genuinely auxiliary uniform theorem is, for example,

\[
\boxed{
\limsup_{H\to\infty}
\sup_{0\le m\le K\log_2H+C}
\frac{\log_2\Xi_{m,H}}H
<\frac7{50}.
}
\]

A stronger and cleaner sufficient statement is

\[
\boxed{
\sup_{0\le m\le K\log_2H+C}
\Xi_{m,H}=2^{o(H)}.
}
\]

Unlike the fixed-m version, these statements compare an increasing family of ternary selector layers against an increasing dyadic horizon and are not equivalent to finite extinction of one preselected finite set.

The finite m=44 calculations remain useful calibrations and local rigidity certificates, but they must not be promoted by themselves to the joint asymptotic theorem.

## 4. Equivalent formation-floor route

The joint scaling exposes a potentially simpler target.

Let

\[
\rho_H(w)
\]

be the least positive integer realizing a hard parity prefix \(w\), and define

\[
\mu_{\rm L7}(H)
:=
\min\{\rho_H(w):w\in\mathcal L_H\}.
\]

Every selector candidate in the relevant joint regime has polynomial size:

\[
N
<6\,3^m+1
\le
H^{K\log_2 3+o(1)}.
\]

For the unconditional value \(K=14.3/\log_2 3\), this is simply

\[
N\le H^{14.3+o(1)}.
\]

Therefore a theorem of the form

\[
\boxed{
\mu_{\rm L7}(H)>H^{14.3+\varepsilon}
\quad\text{eventually}
}
\]

would eliminate the all-range first-crossing selector window without any generic Fourier-mixing theorem.  More generally it is enough to prove that every hard branch with formation floor bounded by the relevant polynomial window is eliminated.

This is the formation-floor version of the same cross-base obstruction:

\[
\boxed{
\text{hard parity language}
\quad\cap\quad
\text{polynomial ordinary-integer window}
\quad=\varnothing
\text{ eventually}.
}
\]

It is compatible with the exact bounded-formation-floor criterion in `2026-08-11-survivor-prefix-tree-bounded-floor-criterion.md`.

## 5. What changes in the proof program

The previous Stage 4 work remains useful but its role is sharpened:

1. L7 supplies the deterministic exponential language loss \(\eta>7/50\).
2. finite m=44/m45 calculations test the same-integer geometry and identify useful local state variables.
3. the global asymptotic theorem must be uniform for \(m=O(\log H)\), not a fixed selector layer.
4. a direct formation-floor escape theorem can replace the full Fourier-overlap theorem if it outruns the polynomial selector window.
5. local suffix universality and fixed-current-resonance bounds remain auxiliary; they do not by themselves provide this global escape.

## 6. Next exact calculation

Reopen the existing exact minimal-survivor solvers and impose, in addition to coefficient survival, the aligned L7 full-Hensel residue-maximal rule.  Compute

\[
\mu_{\rm L7}(H)
\]

and its minimizing path/state through the largest feasible exact depths.

The computation is diagnostic, not proof.  Its purpose is to determine whether the minimum formation floor displays

- exponential growth, suggesting a finite-state/min-plus closure;
- only polynomial growth, requiring an exponent comparison;
- or long plateaus, showing that the formation-floor route needs additional renewal state.

Any eventual theorem must then be proved symbolically/uniformly rather than inferred from the finite scan.
