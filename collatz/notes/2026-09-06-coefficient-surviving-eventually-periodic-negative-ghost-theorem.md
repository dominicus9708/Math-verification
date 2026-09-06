# Coefficient-surviving eventually-periodic paths are negative rational ghosts

Date: 2026-09-06

Status: **SAFE EXACT TERMINAL THEOREM.**  This strengthens the existing eventually-periodic parity/renewal collapse by adding the coefficient-survival sign information.  It does not prove Collatz; it removes the eventually-periodic part of the symbolic survivor boundary from the positive-natural hard core.

---

## 1. Setup

Use the shortcut Collatz map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a finite parity word `p` of length `H` and odd count `S`, write

\[
\boxed{
T_p^H(x)=\frac{3^Sx+C(p)}{2^H},
}
\]

where

\[
C(p)>0
\]

whenever `S>0`.

The standard `2`-adic parity-vector map is a bijective conjugacy with the shift.  Hence a periodic parity tail of period `p` determines a unique `2`-adic state `x` at the beginning of the period and satisfies

\[
\boxed{T^H(x)=x.}
\]

This parity-conjugacy input is already recorded in `2026-08-11-eventually-periodic-renewal-code-collapse.md`.

---

## 2. Exact periodic fixed point

The period equation is

\[
\frac{3^Sx+C(p)}{2^H}=x.
\]

Therefore

\[
\boxed{
(2^H-3^S)x=C(p)
}
\]

and hence

\[
\boxed{
x=\frac{C(p)}{2^H-3^S}.}
\]

This is an ordinary rational number as well as a `2`-adic number.

---

## 3. Coefficient survival forces the denominator negative

Let an infinite parity path be eventually periodic with period `(H,S)` and suppose it is coefficient-surviving in the asymptotic hard-core sense

\[
3^{q_k}\ge2^k
\]

at arbitrarily late/full prefixes, in particular along complete repetitions of the eventual period.

After `m` complete periods the asymptotic multiplicative factor contributed by the periodic tail is

\[
\left(\frac{3^S}{2^H}\right)^m.
\]

If

\[
3^S<2^H,
\]

then sufficiently many repetitions would force the full-prefix coefficient below one, contradicting persistent coefficient survival.

Therefore

\[
3^S\ge2^H.
\]

Equality is impossible for positive integers `H,S`, since powers of `2` and `3` are multiplicatively independent. Hence

\[
\boxed{3^S>2^H.}
\]

Consequently

\[
2^H-3^S<0.
\]

Since `C(p)>0`, Section 2 gives

\[
\boxed{x<0.}
\]

Thus the state at the beginning of the periodic tail is a negative rational number.

---

## 4. A finite preperiod cannot restore positivity

Suppose the full parity path has a finite preperiod `a` of length `K`, odd count `Q`, and correction `C(a)>=0`, followed by the periodic tail state `x<0`.

Then the original start `N` satisfies

\[
\frac{3^QN+C(a)}{2^K}=x.
\]

Hence

\[
\boxed{
N=\frac{2^Kx-C(a)}{3^Q}.
}
\]

The numerator is strictly negative because

\[
x<0,
\qquad
C(a)\ge0.
\]

Therefore

\[
\boxed{N<0.}
\]

So an eventually-periodic coefficient-surviving infinite parity sequence cannot be the parity sequence of a positive ordinary integer.

---

## 5. Examples

### All-odd ghost

For period `1`,

\[
(H,S,C)=(1,1,1),
\]

so

\[
x=\frac1{2-3}=-1.
\]

### `110` ghost

For

\[
p=110,
\]

we have

\[
(H,S,C)=(3,2,5),
\]

so

\[
\boxed{x=\frac5{8-9}=-5.}
\]

This is the periodic hard-core example found in the root-`11`, no-`00` audit.

---

## 6. Terminal split

The infinite coefficient-survivor boundary now separates cleanly into

\[
\boxed{
\begin{array}{ll}
\text{eventually periodic path}
&\Longrightarrow\text{negative rational ghost — CLOSED},\\[2mm]
\text{genuinely aperiodic path}
&\Longrightarrow\text{same-integer / ordinary-integer problem — OPEN}.
\end{array}
}
\]

In particular, a proof does **not** need finite-level survivor-tree emptiness.  Infinite symbolic paths are permitted provided they are shown to converge to nonpositive/non-natural `2`-adic states.

---

## 7. DSD audit

### SAFE

1. Periodic parity tail implies an exact periodic `2`-adic state by parity conjugacy.
2. Its fixed point is `C/(2^H-3^S)`.
3. Persistent coefficient survival forces `3^S>2^H` on an eventual period.
4. Therefore the periodic tail state is negative.
5. Any finite preperiod pulls that state back to a negative original rational start.

### OPEN

1. Genuinely aperiodic coefficient-surviving paths.
2. Excluding positive ordinary integers from that aperiodic boundary.
3. General root-`11`, no-`00` Hensel class-maximality.

### PROHIBITED UPGRADES

1. Do not infer that every infinite survivor is eventually periodic.
2. Do not treat the existence of negative periodic ghosts as a Collatz counterexample.
3. Do not infer finite-level emptiness from this terminal theorem.

---

## 8. Proof-program consequence

The correct terminal target is no longer

\[
\text{survivor tree becomes empty at some finite depth}.
\]

It is the weaker and more appropriate statement

\[
\boxed{
\text{every infinite survivor path is non-natural.}
}
\]

The periodic part of that statement is now closed.  Only the genuinely aperiodic same-integer branch remains.
