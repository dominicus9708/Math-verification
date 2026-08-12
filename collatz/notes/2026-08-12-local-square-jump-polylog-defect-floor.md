# Local square jump barrier and polylogarithmic defect floor

Date: 2026-08-12

Status: **exact local repeated-block jump lemma + effective polylogarithmic lower bound on mechanical defects in the primitive upper-CF first-crossing branch**. The finite numerical corollary for the current first unresolved upper convergent is explicit. This does not prove Collatz.

## 1. Setup

Put

\[
\gamma:=\log_2 3,
\qquad
\beta:=\gamma^{-1}.
\]

For a primitive upper-CF first-coefficient-crossing renewal segment let

\[
a_q:=\sum_{j<q}v_j,
\qquad
h_q:=\lfloor q\gamma\rfloor-a_q\ge0,
\qquad 0\le q<H.
\]

The coordinate-collapse theorem gives

\[
h_q=s_{q+1},
\]

where `s` is the Christoffel left-displacement staircase.

At every zero-defect odd event,

\[
h_q=0,
\]

we have

\[
e_q=q\gamma-a_q=\{q\gamma\}\in[0,1),
\]

and the exact odd-only orbit formula gives

\[
\boxed{
x_q=(N+c_q)2^{\{q\gamma\}}<2(N+c_q).}
\]

For a proper first crossing every `e_i>0`, hence

\[
c_q=\frac13\sum_{i<q}2^{-e_i}<\frac q3\le\frac H3.
\]

Therefore every zero-defect state obeys the uniform bound

\[
\boxed{
x_q< X_H:=2\left(N+\frac H3\right).}
\]

The established upper-CF first-crossing shadow/linear-form bounds give

\[
N\le \operatorname{poly}(H),
\]

so

\[
\boxed{X_H\le\operatorname{poly}(H).}
\]

## 2. Exact local repeated-block jump lemma

Let `u` be any exact parity word of parity length `L`, with `K` odd symbols, whose affine map is

\[
G(x)=\frac{3^Kx+R_u}{2^L}=ax+b,
\]

where

\[
a=\frac{3^K}{2^L}>1,
\qquad b>0.
\]

Suppose an actual positive integer trajectory realizes the repeated block

\[
\boxed{u^2.}
\]

Let `x_0` be the state at the start of the first copy and

\[
x_1=G(x_0)
\]

be the state at the start of the second copy.

Because `x_0` and `x_1` both realize the same length-`L` parity word `u`, the parity-vector/residue bijection gives

\[
\boxed{x_1\equiv x_0\pmod{2^L}.}
\]

Since `a>1` and `b>0`,

\[
x_1-x_0=(a-1)x_0+b>0.
\]

Thus the positive integer difference is a nonzero multiple of `2^L`, and therefore

\[
\boxed{x_1-x_0\ge2^L.}
\]

In particular,

\[
\boxed{x_1>2^L.}
\]

This is a local statement. It does not require `u^2` to begin at the renewal floor, does not require `x_0` to be the least residue representative, and does not require the auxiliary upper bound `a<sqrt(2)` used in the earlier square-prefix formation argument.

### 3-adic dual

Let

\[
x_2=G(x_1)
\]

be the endpoint of the second copy. Reversing one copy gives

\[
2^Lx_j\equiv R_u\pmod{3^K}
\qquad(j=1,2).
\]

Hence

\[
x_2\equiv x_1\pmod{3^K}.
\]

Again `x_2>x_1`, so

\[
\boxed{x_2-x_1\ge3^K,}
\qquad
\boxed{x_2>3^K.}
\]

Thus the same exact square produces both a dyadic forward jump and a ternary endpoint jump.

## 3. Local square exclusion inside a zero-defect interval

Suppose a reference Christoffel/Sturmian factor contains a square `u^2` with supercritical coefficient `3^K/2^L>1`, and suppose the entire occurrence lies inside a zero-defect interval.

The start of each copy is then a zero-defect odd event, so both copy-start states are bounded by `X_H`.

If

\[
\boxed{2^L>X_H,}
\]

the local repeated-block jump lemma gives

\[
x_1-x_0\ge2^L>X_H,
\]

while `0<x_0,x_1<X_H`, a contradiction.

Therefore no zero-defect interval can contain such a square once its period exceeds the logarithmic state scale.

## 4. Sturmian recurrence turns one square into a window obstruction

The critical parity word is the mechanical/Sturmian word of slope

\[
\beta=\frac1{\log_2 3}.
\]

Let `q_n` be the continued-fraction denominators of `beta`. The classical Morse--Hedlund recurrence formula states that for

\[
q_{k-1}\le n<q_k,
\]

the recurrence function is

\[
\boxed{R_\beta(n)=n-1+q_k+q_{k-1}.}
\]

Hence every factor of the critical word of length `R_beta(n)` contains every critical factor of length `n`.

The previously established standard-word recursion supplies infinitely many supercritical square factors

\[
u_j^2
\]

with parity periods

\[
L_j:=|u_j|\to\infty,
\]

where each `u_j` is a nearby convergent word on the coefficient-expanding side.

The same effective Baker/Matveev lower bound already used in the exact-Christoffel branch implies that neighboring convergent denominators are polynomially related. Consequently the available square scales `L_j` have at most effective polynomial jumps.

Given the polynomial zero-defect state bound `X_H`, choose the first available square scale with

\[
2^{L_j}>X_H.
\]

Because `X_H<=poly(H)` and the square scales have polynomial jumps,

\[
\boxed{L_j\le C_1(\log H)^{D_1}}
\]

for effective constants `C_1,D_1`.

Applying the recurrence formula at factor length `2L_j` and again using polynomial control of neighboring convergent denominators gives

\[
\boxed{R_\beta(2L_j)\le C_2(\log H)^{D_2}}
\]

for effective constants `C_2,D_2`.

Therefore every critical parity factor longer than this polylogarithmic window contains the forbidden square `u_j^2`.

## 5. Polylogarithmic defect-gap theorem

Consider a run of consecutive zero defect coordinates

\[
h_q=h_{q+1}=\cdots=h_{q+m-1}=0.
\]

Their actual odd positions agree exactly with the critical Beatty positions

\[
\kappa_i=\lfloor i\gamma\rfloor.
\]

The exact parity segment from the first to the last such odd event has length at least

\[
\boxed{
\lfloor(m-1)\gamma\rfloor+1.
}
\]

If this length reached `R_beta(2L_j)`, the segment would contain the forbidden square of Section 3.

Hence there are effective constants `C,D` such that every zero-defect run obeys

\[
\boxed{m\le C(\log H)^D.}
\]

Let

\[
r_*:=\#\{q:h_q>0\}.
\]

The `H-r_*` zero positions are split into at most `r_*+1` zero runs. Therefore

\[
H-r_*\le C(\log H)^D(r_*+1),
\]

and in particular

\[
\boxed{
r_*\ge \frac{H}{C'(\log H)^D}-1}
\]

for another effective constant `C'`.

Thus an actual ordinary-integer first-crossing candidate cannot have only finitely many defects, logarithmically many defects, or more generally fewer than `H/polylog(H)` defects.

This is stronger than the earlier qualitative sparse-support statement `r_*=o(H)`.

## 6. Weighted-defect consequence

The exact coordinate collapse gives

\[
\mathfrak D_H=3\eta,
\]

where `eta` is the normalized Christoffel correction defect.

The elementary pointwise estimate gives

\[
\mathfrak D_H>\frac14r_*.
\]

The independently audited defect-run average theorem on the draft branch `agent/collatz-eo-matrix-audit` sharpens this to

\[
\eta\ge\frac5{48}r_*,
\]

hence

\[
\boxed{\mathfrak D_H\ge\frac5{16}r_*.}
\]

Combining with Section 5,

\[
\boxed{
\mathfrak D_H
\ge
\frac{5}{16}
\left(
\frac{H}{C'(\log H)^D}-1
\right).
}
\]

So the residual upper-CF candidate loses at least `H/polylog(H)` of the critical rotation correction mass.

## 7. Explicit finite corollary at the current first unresolved upper convergent

Take

\[
(A,H)=
(10,439,860,591,\;6,586,818,670).
\]

The Denjoy--Koksma first-crossing ceiling gives

\[
N\le
1.5645317540070874\times10^{20}.
\]

Hence every zero-defect state satisfies

\[
X_H=2\left(N+\frac H3\right)
<3.129064\times10^{20}.
\]

The continued fractions of `beta` contain

\[
\frac{41}{65},
\qquad
\frac{53}{84},
\qquad
\frac{306}{485}.
\]

Let `u` be the standard critical factor with

\[
L=84,
\qquad K=53.
\]

Its coefficient is

\[
\boxed{
\frac{3^{53}}{2^{84}}
=1.002090314041086\ldots>1.
}
\]

The next standard word uses partial quotient `5`, so the critical language contains

\[
\boxed{u^2.}
\]

Moreover

\[
2^{84}=19,342,813,113,834,066,795,298,816
>X_H.
\]

For factor length `168=2L`, since

\[
84\le168<485,
\]

the Sturmian recurrence formula gives

\[
\boxed{
R_\beta(168)=168-1+485+84=736.
}
\]

Therefore every critical parity factor of length `736` contains this forbidden `u^2`.

If `465` consecutive odd-event defects vanished, their critical parity span would have length at least

\[
\lfloor464\gamma\rfloor+1=736.
\]

Hence every zero-defect run has at most `464` odd-event positions.

It follows that

\[
H-r_*\le464(r_*+1),
\]

and therefore

\[
\boxed{
r_*\ge14,165,201.}
\]

Using the run-aware defect bound,

\[
\boxed{
\mathfrak D_H
\ge
\frac5{16}r_*
\ge4,426,625.3125.
}
\]

## 8. Refined ordinary-start ceiling

The exact first-crossing correction identity is

\[
(P-1)N+Pg
=c_{chr}-\frac13\mathfrak D_H,
\]

with

\[
P=\frac{2^A}{3^H}>1,
\qquad g\ge4.
\]

Denjoy--Koksma gives

\[
c_{chr}\le\frac{H}{6\ln2}+\frac13.
\]

Hence

\[
\boxed{
N\le
\frac{
H/(6\ln2)+1/3-\mathfrak D_H/3-4P
}{P-1}.
}
\]

At the present pair,

\[
P-1
=1.012312532072859\ldots\times10^{-11}.
\]

Substituting the explicit defect floor yields

\[
\boxed{
N\le
1.5630741589224825\times10^{20}.
}
\]

The previous ceiling was

\[
1.5645317540070874\times10^{20},
\]

so the local-square/recurrence argument removes an additional

\[
1.4575950846049\times10^{17}
\]

from the admissible start window, about `0.0932%` of that ceiling.

The numerical improvement is modest, but the structural result is stronger: it is the first deterministic lower bound forcing defects to occur repeatedly throughout the word rather than merely proving that at least one defect exists.

## 9. Relation to the draft finite terminal calculations

The draft branch independently proves branch-specific terminal facts such as:

- one terminal defect is impossible in the isolated `1000` branch;
- two terminal defects are also impossible there;
- the defect-run average gives `eta >= 5 r_*/48` globally inside the first-crossing defect formalism.

The present theorem is complementary. It is not a terminal-window enumeration and does not depend on the special `1000` branch. It shows that any actual ordinary-integer near-mechanical candidate must place defects at least once per polylogarithmic critical recurrence window.

## 10. Remaining gap

The bound

\[
r_*\gtrsim H/\operatorname{polylog}(H)
\]

still allows zero asymptotic defect density. Therefore it does not yet give a fixed positive linear loss

\[
\mathfrak D_H\ge\eta_0 H.
\]

The next target is to combine the repeated local-square obstruction with the strengthened renewal address / late-lift condition. A defect can destroy a local square combinatorially, but it must also shift the same ordinary integer's dyadic renewal address consistently across all scales. A multi-scale hitting argument should therefore count not merely how many defects are needed, but how many independent dyadic scales their locations must control.

## References / external inputs

- M. Morse and G. A. Hedlund, *Symbolic Dynamics II. Sturmian Trajectories* (1940): Sturmian mechanical coding and recurrence theory.
- P. Rotondo and B. Vallée, *The recurrence function of a random Sturmian word*, arXiv:1610.01479: states the classical recurrence formula `R(alpha,n)=n-1+q_k+q_{k-1}` for `q_{k-1}<=n<q_k`.
- The project note `2026-08-11-christoffel-square-prefix-eventual-finiteness.md`: standard-word square factors and effective Baker/Matveev control of neighboring convergents.
- Draft branch note `2026-08-10-defect-run-average-bound.md`: independently audited run-aware constant `eta>=5 r_*/48`.
