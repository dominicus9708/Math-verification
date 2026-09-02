# Terminal 28-gate mod-3 steering collapse

Status: **EXACT / CLOSED for pure target-dominance terminal-residue existence**

## Normalized carry

For the final `L` ranked-one gates, write

\[
A_t=(q-t-1)+D_t,
\qquad
B_t=(q-t-1)+s_t,
\]

with

\[
0\le s_t\le D_t,
\qquad
s_{t+1}\le s_t.
\]

If `z_t` is the target-relative projective carry at remaining precision `m=L-t`, define

\[
w_t=2^{-(q-t-1)}z_t\pmod{3^m}.
\]

Then the exact one-gate law becomes

\[
\boxed{
w_{t+1}
=
\frac{2\left(w_t+2^{D_t}-2^{s_t}\right)}{3}
\pmod{3^{m-1}},
}
\]

whenever the numerator is divisible by 3.

## One forbidden mod-3 class

Modulo 3,

\[
2^n\equiv(-1)^n.
\]

Therefore a legal slack exists at gate `t` iff

\[
(-1)^{s_t}
=
w_t+(-1)^{D_t}
\pmod3.
\]

The right side can equal `+1` or `-1` for exactly two carry classes and is zero for exactly one class.

Hence the unique impossible class is

\[
\boxed{
w_t\equiv(-1)^{D_t+1}\pmod3.
}
\]

For either allowed class the parity of `s_t` is uniquely determined.

## Steering lemma

Fix an allowed `w_t mod 3`.

Among any six consecutive slack integers there are exactly three with the required parity, one in each corresponding residue class modulo 6.

On a fixed parity class, `2^s mod 9` takes three values differing by multiples of 3. Therefore

\[
\frac{2(w_t+2^{D_t}-2^{s_t})}{3}\pmod3
\]

runs through **all three** successor residues as those three slack classes are used.

Thus, whenever the current legal cap `U_t` is at least 5, one may choose `s_t` among the top six legal values and prescribe `w_(t+1) mod 3` arbitrarily, while losing at most five units of ordering cap.

Consequently, if

\[
\min_t D_t\ge5L,
\]

then every initial normalized carry outside the first forbidden class admits a complete `L`-gate suffix: at each nonterminal gate steer the next carry away from the next forbidden class.

Therefore

\[
\boxed{
\text{suffix completion exists}
\iff
w_0\not\equiv(-1)^{D_0+1}\pmod3.
}
\]

## Current right-H specialization

For the synchronized checkpoint window,

\[
L=28,
\qquad
q_H=397{,}573{,}380.
\]

The exact final-rank capacities satisfy

\[
D_0=232{,}565{,}517,
\qquad
\min_tD_t=232{,}565{,}502>5\cdot28.
\]

Also `q_H-1` is odd, so modulo 3

\[
w_0=2z_H.
\]

Since `D_0` is odd, the forbidden normalized class is `w_0=1`. Hence

\[
\boxed{
\text{right-H target-dominance residue completion}
\iff
z_H\not\equiv2\pmod3.
}
\]

## Checkpoint form

The synchronized affine observation is

\[
z_H\equiv2^S Z-C(H_s^*)\pmod{3^{28}}.
\]

For the current constants,

\[
2^S\equiv2\pmod3,
\qquad
C(H_s^*)\equiv1\pmod3.
\]

Therefore

\[
z_H\equiv2Z-1\pmod3.
\]

The forbidden class `z_H=2 mod 3` is exactly `Z=0 mod 3`. Thus

\[
\boxed{
\text{pure right-H target-dominance terminal condition}
\iff
3\nmid Z.
}
\]

## Consequence for the computation plan

This is a **negative compression result for the hoped-for 28-trit checkpoint filter**: pure target dominance does not determine or strongly restrict all 28 ternary digits. It removes only one of the three mod-3 checkpoint classes.

Therefore the synchronized CRT singleton theorem remains valid per supplied pair `(Z mod 2^27, z_H mod 3^28)`, but target dominance alone does not provide a small enough set of `z_H` values to expose ordinary checkpoints one by one.

The next active predicate must contribute additional information: exact pre-bridge correction-language/H-L boundary control, physical defect information, or another certified structural restriction.

## Scope restriction

This theorem does **not** prove:

- full H/L correction-language membership;
- same-orbit connectivity;
- physical closure;
- closure of any 14-root family;
- Route-B or Collatz.

## Certificate

- `../src/A0_s1_routeB_terminal_28gate_mod3_steering_certificate.py`

The small-horizon exhaustive comparisons in the certificate are regression guards only. The theorem is the normalized recurrence + mod-9 steering argument above.
