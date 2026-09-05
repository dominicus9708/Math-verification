# Gate C: terminal barrier and valid closure criteria

Date: 2026-09-06

Status: **SAFE LOGICAL BARRIER + ZERO-TAIL LAW CLOSED + ORIENTATION/RECURRENCE OPEN.**

This note audits the last step of the current Collatz proof program after the Beatty one-child / selector-repair route.

The central warning remains:

\[
\boxed{
\text{polynomial normalized candidate-mass decay alone cannot exclude one integer path.}
}
\]

However, the canonical finite-support formulas close one part that was initially left open: the eventual-zero tail transition itself is exactly the accelerated Collatz map.

---

## 1. Canonical integer condition

The established canonical formation condition is

\[
\boxed{
N\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support}.
}
\]

The exact canonical lift is

\[
\boxed{
\rho_{q+1}=\rho_q+t_q2^{A_q+1},
\qquad
0\le t_q<2^{v_q}.
}
\]

Thus `t_q` is generally a `v_q`-bit block, not a single binary bit.  A fixed positive integer has some support endpoint `q_0` such that

\[
\boxed{t_q=0\qquad(q\ge q_0).}
\]

A hypothetical minimal Collatz counterexample must therefore determine an infinite surviving candidate path whose canonical lift blocks are eventually all zero.

Status: **CLOSED / SAFE.**

---

## 2. Why `mu_L -> 0` is insufficient

Let `S_L` be the finite family of surviving depth-`L` candidate cylinders and let `w_L(C)>0` be the normalized weight of cylinder `C`.

Then

\[
\mu_L=\sum_{C\in S_L}w_L(C).
\]

One exceptional nested path

\[
C_1\supset C_2\supset\cdots
\]

is compatible with `mu_L -> 0` because its own cylinder weight may also tend to zero.

For example, a single depth-`L` cylinder may have weight `2^{-L}` while the total survivor mass decays only like `L^{-gamma}`.  Since

\[
2^{-L}\ll L^{-\gamma},
\]

polynomial normalized mass decay cannot by itself rule out even one surviving path.

Status: **SAFE LOGICAL BARRIER.**

---

## 3. General mass-to-emptiness transfer lemma

Let `I_L subset S_L` be the cylinders that can still represent a finite prefix of an eventually-zero canonical lift, and define

\[
w_L^{\rm int}:=\inf_{C\in I_L}w_L(C)
\]

when `I_L` is nonempty.

If `I_L` contains a survivor, then

\[
\mu_L\ge w_L^{\rm int}.
\]

Hence

\[
\boxed{
\mu_L<w_L^{\rm int}
\Longrightarrow
I_L=\varnothing.
}
\]

More generally,

\[
\boxed{
\mu_L/w_L^{\rm int}\to0
}
\]

would imply eventual emptiness of integer-compatible cylinders.

Status: **SAFE LEMMA.**

The present polynomial contraction does not supply this because a single compatible cylinder may be exponentially light.

---

## 4. `C_tail` is closed: exact zero-tail dynamics

The exact canonical carry recurrence is

\[
\boxed{
2^{v_q}y_{q+1}
=
3y_q+1+2t_q3^{q+1}.
}
\]

The factor `2` multiplying `t_q3^{q+1}` is essential in the general formation law.

Once the canonical lift has reached its support endpoint,

\[
t_q=0,
\]

so

\[
2^{v_q}y_{q+1}=3y_q+1.
\]

The exact digit theorem gives equivalently

\[
\boxed{t_q=0\iff v_q=v_2(3y_q+1).}
\]

Therefore

\[
\boxed{
v_q=\nu(y_q):=v_2(3y_q+1),}
\]

and

\[
\boxed{
y_{q+1}
=T(y_q)
:=
\frac{3y_q+1}{2^{v_2(3y_q+1)}}.}
\]

So an eventually-zero canonical tail follows the ordinary accelerated Collatz map exactly.

If the signed-skew variable is represented by

\[
A_q=\lfloor q\log_2 3\rfloor-s_q,
\]

and

\[
r_q=\lfloor(q+1)\log_2 3\rfloor-\lfloor q\log_2 3\rfloor\in\{1,2\},
\]

then

\[
\boxed{v_q=s_q+r_q-s_{q+1}.}
\]

Hence on the zero tail,

\[
\boxed{
s_{q+1}=s_q+r_q-\nu(y_q).}
\]

The exact zero-tail state update is therefore

\[
\boxed{
(y_{q+1},s_{q+1})
=
\left(
\frac{3y_q+1}{2^{\nu(y_q)}},
\ s_q+r_q-\nu(y_q)
\right).
}
\]

Status: **`C_tail` CLOSED / SAFE.**

This closure does not solve Collatz: the zero-tail map is precisely the accelerated Collatz dynamics whose infinite non-descent must ultimately be excluded.

---

## 5. Exact Beatty boundary orientation in coefficient slack coordinates

The Beatty one-child certificate uses the coefficient-survival slack DP.  At a rise,

- appending coefficient bit `1` preserves the old slack;
- appending coefficient bit `0` decreases the slack by one and is allowed only when the old slack is positive.

Therefore at a rise with boundary slack `s=0`,

\[
\boxed{
\text{append }1\text{ survives},
\qquad
\text{append }0\text{ is killed}.
}
\]

This is an exact local orientation statement in the **coefficient-survival coordinate**.

Status: **SAFE LEMMA.**

It must not yet be identified with a canonical lift block or any one of its binary digits.

---

## 6. New Gate `C_orient`: coordinate identification

A positive integer eventually has

\[
t_q=0,
\]

meaning that every binary bit in the entire variable-length lift block of length `v_q` is zero.

The coefficient DP says that a rise-boundary parent with slack zero accepts only appended coefficient child `1`.

A tempting contradiction would compare the eventual zero canonical lift with the forced coefficient child `1`.  But this is valid only if the two child coordinates are proved to coincide under the exact canonical fibre map.

Thus define

\[
\boxed{
C_{\rm orient}:
\text{identify canonical lift-block coordinates with selector/Beatty coefficient child coordinates.}
}
\]

This is closely related to `F_map`, but it is the terminal pathwise form of that identification.

A valid theorem must explicitly map:

1. canonical lift block `t_q` occupying binary positions `A_q+1,...,A_{q+1}`;
2. parent modulus at the relevant coefficient scale;
3. the two child lifts used by selector counts `C(r)` and `C(r+M)`;
4. the appended bit used by the Beatty slack DP;
5. the index conversion between odd-event index `q` and binary/coefficient scale `L`.

Status: **OPEN.**

### Audit prohibition

Do **not** write

\[
t_q=0\Rightarrow\text{Beatty append-0}
\]

until `C_orient`/`F_map` proves the coordinate and index identification.

---

## 7. New Gate `C_recur`: pathwise boundary recurrence

Even if `C_orient` is proved, aggregate one-child exposure

\[
|D_L|/|R_L|>2/(5L)
\]

does not imply that one particular eventually-zero path ever belongs to `D_L`.

Therefore a second deterministic statement is required.

A direct target is

\[
\boxed{
C_{\rm recur}:
\text{every infinite integer-compatible zero-tail survivor reaches a rise scale with boundary slack }s=0.
}
\]

More generally, it is enough to prove that every such path eventually reaches any exact one-child state whose surviving orientation conflicts with its canonical zero-tail orientation.

Status: **OPEN.**

This is the precise pathwise analogue of the aggregate Beatty-exposure theorem.

---

## 8. Revised terminal contradiction route

If both open terminal gates are closed, the final pathwise contradiction has the form

\[
\boxed{
\begin{array}{c}
N\in\mathbb N_{>0}\text{ counterexample}\\
\Downarrow\\
(t_q)\text{ finite support}\\
\Downarrow\\
t_q=0\text{ eventually}\\
\Downarrow\\
C_{\rm tail}:\text{ exact accelerated Collatz tail}\\
\Downarrow\\
C_{\rm recur}:\text{ future one-child boundary hit}\\
\Downarrow\\
C_{\rm orient}:\text{ canonical/Beatty child identification}\\
\Downarrow\\
\text{forced orientation conflict}\\
\Downarrow\\
\bot
\end{array}
}
\]

This would exclude a single integer path directly and would not rely on `mu_L -> 0 => emptiness`.

Status: **VALID TARGET ARCHITECTURE / OPEN AT `C_orient`, `C_recur`.**

---

## 9. Alternative Gate-C route: absolute integer-compatible count

Let

\[
M_L
:=
\#\{\text{surviving depth-}L\text{ cylinders compatible with an eventually-zero integer tail}\}.
\]

If an exact argument yields

\[
\boxed{M_L<1}
\]

for some large `L`, then `M_L=0` because it is an integer.

A mass estimate could imply this only with a sufficiently strong absolute weight comparison.  The current polynomial normalized mass decay does not do so under exponentially small single-cylinder weights.

Status: **VALID ALTERNATIVE / OPEN.**

---

## 10. Interaction with Gates F and S

The aggregate branch is

\[
\boxed{
F_{\rm map}+F_{\rm unif}
\longrightarrow
\text{Gate S harmonic contraction}
\longrightarrow
\mu_L\to0.
}
\]

The terminal branch is now

\[
\boxed{
C_{\rm form}\;(\text{closed})
\longrightarrow
C_{\rm tail}\;(\text{closed})
\longrightarrow
C_{\rm orient}\;(\text{open})
+ C_{\rm recur}\;(\text{open}).
}
\]

`F_map` and `C_orient` may ultimately be proved by one common exact coordinate-identification theorem.

The two branches must not be merged merely through normalized mass decay.

---

## 11. DSD audit

### CLOSED / SAFE

1. positive integer iff canonical lift blocks have finite support;
2. zero-tail carry evolution equals the accelerated Collatz map;
3. rise-boundary coefficient slack `s=0` has exactly one child: appended `1`;
4. normalized mass tending to zero does not imply set emptiness;
5. mass-to-emptiness requires an absolute atom/count transfer or a pathwise contradiction.

### OPEN

1. `F_map / C_orient`: exact coordinate and index identification;
2. `F_unif`: growing-Q moving-strip control;
3. Gate S: harmonic abundance of good exact-selector rises;
4. `C_recur`: deterministic boundary recurrence for every integer-compatible zero-tail survivor.

### PROHIBITED UPGRADES

1. Do not infer `C_recur` from positive aggregate one-child density/exposure.
2. Do not equate canonical lift block zero with coefficient append-bit zero before the map is proved.
3. Do not infer emptiness from polynomial normalized mass decay.
4. Do not assume the accelerated zero-tail map is simpler than Collatz; it is the same orbit dynamics in odd-state form.

---

## 12. Next terminal calculation

The highest-value terminal target is now the exact coordinate map

\[
\boxed{
\text{canonical lift block/bit}
\leftrightarrow
\text{selector child}
\leftrightarrow
\text{Beatty coefficient child}.
}
\]

If this map identifies the eventually-zero canonical coordinate with the killed Beatty orientation at a rise boundary, then only `C_recur` remains for the pathwise terminal contradiction.

In parallel, the aggregate proof still requires the moving-strip `F_unif` condition and harmonic Gate-S estimate.
