# Euclidean correction-collision fibres and minimality headroom credit

Date: 2026-08-13

Status: **exact local rewrite theorem + explicit first Euclidean collision fibres**.  The result connects the Euclidean survival-state multiplicities to integer alternate predecessors.  It does not prove Collatz.

## 1. Local same-coefficient rewrite

Let `w` and `u` be two parity words of the same time length `L` and the same odd count `q`:

\[
T_w^L(x)=\frac{3^qx+R_w}{2^L},
\qquad
T_u^L(z)=\frac{3^qz+R_u}{2^L}.
\]

Assume

\[
\boxed{R_u-R_w=3^q\Delta}
\]

for an integer

\[
\Delta>0.
\]

Then

\[
3^q(x-\Delta)+R_u=3^qx+R_w,
\]

so

\[
\boxed{T_u^L(x-\Delta)=T_w^L(x).}
\]

The canonical residues satisfy the same identity modulo `2^L`:

\[
r_u-r_w\equiv-\Delta\pmod{2^L}.
\]

Therefore, whenever the integer `x` realizes `w`, the integer `x-Delta` realizes `u` provided it is positive.  The two ordinary trajectories merge at the block endpoint.

Call `Delta` the **integer predecessor credit** of the rewrite `w -> u`.

## 2. Minimal-counterexample headroom inequality

Let `N` be a hypothetical minimal positive counterexample and let

\[
x=T^k(N)
\]

be the ordinary orbit state at the beginning of a local block.

If the actual local word is `w` and there is a rewrite `w -> u` with credit `Delta`, then `x-Delta` reaches the same later point of the nonconvergent orbit.

If

\[
0<x-\Delta<N,
\]

this is impossible by minimality.  Hence, whenever `x>Delta`, a necessary condition is

\[
\boxed{x-N\ge\Delta.}
\]

Thus every correction-collision orientation carries a **headroom floor**.  It is stronger than a pure survival-state condition: two local words can have exactly the same future coefficient-survival possibilities but different minimality credits.

At the global minimum itself (`k=0`, `x=N`), every positive credit eliminates the corresponding initial cylinder immediately.

## 3. Exact context invariance

The local rewrite survives arbitrary common prefix and suffix contexts.

Let `p` be a common prefix of length `k` and odd count `q_p`, and `v` a common suffix with `q_v` odd symbols.  Compare

\[
pwv
\quad\text{and}\quad
puv.
\]

The total correction difference is

\[
\boxed{
R_{puv}-R_{pwv}
=3^{q_v}2^k(R_u-R_w)
=3^{q_v}2^k3^q\Delta.
}
\]

The total odd count is `q_p+q+q_v`, so the corresponding initial rational displacement is

\[
\boxed{
\frac{R_{puv}-R_{pwv}}{3^{q_p+q+q_v}}
=\frac{2^k}{3^{q_p}}\Delta.
}
\]

Under the common prefix `p`, this rational displacement is multiplied by the prefix coefficient `3^{q_p}/2^k` and becomes exactly the integer gap `Delta` at the entrance to the local block.

Hence a local integer predecessor credit is not destroyed by surrounding context.  A common prefix merely transports it backward as a rational 2-adic displacement, and a common suffix preserves the later merge.

This is the local/context version of the denominator-invariance theorem in the binary alternate-predecessor sieve.

## 4. First Euclidean level: no integer collision in the neutral fibre

The first Euclidean block is

\[
A=01.
\]

Its two neutral orientations are

\[
01,\qquad10.
\]

Both have one odd symbol and survival state

\[
(\Sigma,M)=(0,0).
\]

Their corrections are

\[
R_{01}=2,
\qquad
R_{10}=1.
\]

The difference is only

\[
1,
\]

which is not divisible by `3^1`.  Thus the first two-way neutral orientation fibre does **not** yet contain an integer alternate-predecessor collision.

## 5. Second Euclidean level: first integer collision

The second-level composite is

\[
BA=101.
\]

The survival-state fibre

\[
(\Sigma,M)=(-1,-1)
\]

contains the three orientations

\[
001,\qquad010,\qquad100.
\]

Each contains one odd symbol.  Their corrections are

\[
R_{001}=4,
\qquad
R_{010}=2,
\qquad
R_{100}=1.
\]

Therefore

\[
\boxed{R_{001}-R_{100}=3=3^1.}
\]

The low-correction orientation `100` has the exact local rewrite

\[
\boxed{100\longrightarrow001}
\]

with predecessor credit

\[
\boxed{\Delta=1.}
\]

Explicitly,

\[
\boxed{
T_{001}^3(x-1)=T_{100}^3(x).
}
\]

Thus the new three-way Euclidean multiplicity fibre is already a genuine 3-adic correction-collision fibre.

## 6. Third Euclidean composite: neutral collision

Continue the return-word grouping.  With

\[
C:=BA=101,
\qquad
D:=A=01,
\]

the next paired macroblock is

\[
\boxed{E:=DC=01101.}
\]

Its mechanical orientation `01101` and the orientation `11100` have the same number of odd symbols,

\[
q=3,
\]

and both have exact relative survival state

\[
\boxed{(\Sigma,M)=(0,0).}
\]

Indeed the cumulative relative displacement of `11100` against `01101` is

\[
1,1,1,1,0,
\]

so it never falls below zero and returns to the same terminal slack.

The exact corrections are

\[
R_{01101}=46,
\qquad
R_{11100}=19.
\]

Hence

\[
\boxed{
46-19=27=3^3.
}
\]

Therefore

\[
\boxed{
T_{01101}^5(x-1)=T_{11100}^5(x).
}
\]

This is the first explicit **neutral Euclidean survival fibre** in the hierarchy that contains an integer predecessor rewrite.

The distinction from the first-level `01/10` fibre is structural: higher return-word composition has aligned the correction difference with the full odd multiplier `3^q`.

## 7. Inheritance at the next composite

At the next Euclidean step one of the larger blocks is

\[
G=E\,C=01101101.
\]

Append the common suffix `C=101` to the neutral pair from the preceding section:

\[
01101\,101,
\qquad
11100\,101.
\]

The corrections are

\[
R_{01101101}=638,
\qquad
R_{11100101}=395.
\]

The total odd count is

\[
q=5,
\]

and

\[
\boxed{
638-395=243=3^5.
}
\]

Thus the unit predecessor credit is inherited exactly:

\[
\boxed{
T_{01101101}^8(x-1)
=T_{11100101}^8(x).
}
\]

This is the suffix-invariance mechanism in concrete Euclidean form.

## 8. Correction-residue extension of the state monoid

The existing Euclidean survival state

\[
(\Sigma,M,\text{multiplicity})
\]

can be augmented at a fixed 3-adic resolution `J` by the correction residue

\[
\rho_J:=R\bmod3^J.
\]

For two actual orientations `x` on a block of length `L_x` and `y` on the following block, with odd counts `q_x,q_y`, concatenation satisfies

\[
\boxed{
R_{xy}
=3^{q_y}R_x+2^{L_x}R_y.
}
\]

Together with

\[
\Sigma_{xy}=\Sigma_x+\Sigma_y,
\]

\[
M_{xy}=\min(M_x,\Sigma_x+M_y),
\]

this gives an exact finite-resolution product on

\[
\boxed{
(\Sigma,M,q,R\bmod3^J,\text{multiplicity}).
}
\]

At fixed `J`, equal states can therefore be aggregated without enumerating all internal parity words.

As `J` increases, the residue classes form a 3-adic trie.  For two distinct words `u,w`, the last trie level at which they remain in the same correction class is exactly

\[
\boxed{v_3(R_u-R_w).}
\]

Hence the trie directly records the denominator-clearing depth used by the alternate-predecessor theorem.

## 9. What the unit-credit examples do and do not give

A unit credit at an interior orbit state only forces

\[
x\ge N+1,
\]

which is already automatic for a nonperiodic orbit after it leaves its minimum.  Thus the examples above are not by themselves an R2 contradiction.

Their significance is that the Euclidean multiplicity hierarchy now has a proved arithmetic refinement: some equal-survival fibres carry integer predecessor credits.

The useful asymptotic quantity is therefore not merely the number of equal-state orientations.  For an actual orientation `w`, define its available local dominance credit

\[
\boxed{
\Delta_U(w)
:=
\max_{u}
\left\{
\frac{R_u-R_w}{3^q}:
R_u>R_w,
\ R_u\equiv R_w\pmod{3^q},
\ u\text{ lies in the same survival-state fibre}
\right\},
}
\]

with value zero when the set is empty.

Whenever `Delta_U(w)>0` and the block starts at orbit state `x`, minimality requires

\[
\boxed{x-N\ge\Delta_U(w)}
\]

provided `x>Delta_U(w)`.

## 10. Next target

The next multiscale target is a **headroom-credit growth theorem**:

> along the Euclidean / continued-fraction hierarchy, prove that every sufficiently long critical survivor orientation either leaves the critical strip or contains a correction-collision rewrite whose predecessor credit exceeds the available orbit headroom.

The harmonic-correction identity makes this target quantitative.  At an odd-event checkpoint with discrepancy `D_i` and correction `c_i`,

\[
x_i=2^{-D_i}(N+c_i),
\]

while the existing nonperiodic bound gives `c_i=O_N(i^{1/9})`.  Therefore a return to a fixed critical strip has headroom at most a fixed multiple of `N` plus a sublinear correction term.

A Euclidean credit that grows without bound, and eventually faster than the headroom permitted at the required return scales, would convert the present local rewrite system into an R2 exclusion mechanism.

The current note establishes the exact algebraic interface needed for that program; growth or full coverage of the credits remains open.
