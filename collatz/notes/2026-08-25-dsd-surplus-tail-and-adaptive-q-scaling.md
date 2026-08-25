# DSD surplus-tail obstruction and adaptive-Q scaling rule

Date: 2026-08-25

## Status

Safe structural obstruction plus an exact scaling law.

No Collatz proof is claimed.

## 1. Why pathwise boundary recurrence is not available

The current exact minimal-survivor record

\[
n=12,235,060,455
\]

has coefficient stopping time

\[
\tau_c(n)=547.
\]

For its surviving prefix through depth 546, let

\[
d_B=q_B-b(B),
\qquad
b(B)=\min\{q:3^q\ge2^B\}.
\]

The exact audit gives boundary visits `d_B=0` only at

`0, 1, 2, 4, 5, 8, 10, 466, 539, 541, 542, 543, 544, 545, 546`.

In particular:

- the longest run with `d>=1` has length 455, depths 11--465;
- the longest run with `d>=2` has length 286, depths 179--464;
- the longest run with `d>=3` has length 199, depths 261--459;
- the maximum surplus before the crossing is 9.

Therefore a theorem of the form

> every coefficient-surviving path returns to the Beatty boundary within a fixed number of steps

is false.

This explains why the finite average/cylinder contractions cannot be upgraded by a simple pathwise recurrence argument.

## 2. General reverse-potential ceiling

For a reverse odd-to-odd code with `q` inverse odd events and total binary exponent `K`,

\[
\Lambda=\frac{3^q}{2^K}.
\]

Every inverse odd event uses an exponent at least one, so

\[
K\ge q.
\]

At ternary reverse depth `Q`, also `q<=Q`.  Hence

\[
\boxed{
\Lambda\le\left(\frac32\right)^Q.
}
\]

The bound is sharp: for endpoint residue

\[
z\equiv-1\pmod{3^Q}
\]

the inverse exponent `a=1` is admissible at every level and gives

\[
\Lambda=\left(\frac32\right)^Q.
\]

Thus

\[
\boxed{
\Lambda_{Q,\max}=\left(\frac32\right)^Q.
}
\]

The Q7 certificate from the preceding audit is the special case

\[
\Lambda_{7,\max}=\frac{2187}{128}.
\]

## 3. Blind-surplus threshold

A coefficient-surviving endpoint with surplus `d` has

\[
\Theta_B
=
\frac{3^{q_B}}{2^B}
=
\frac{3^{b(B)}}{2^B}3^d
\ge3^d.
\]

Therefore if

\[
3^d\ge\left(\frac32\right)^Q,
\]

then no strict reverse-potential witness at resolution Q can beat that endpoint, for any ternary residue.

Define

\[
d_{\rm blind}(Q)
=
\min\left\{d:\;3^d\ge(3/2)^Q\right\}.
\]

Then every state with

\[
d\ge d_{\rm blind}(Q)
\]

is outside the strict fixed-Q reverse mechanism.

Equivalently, to have even the *possibility* of reverse-potential contraction at surplus d one needs

\[
\left(\frac32\right)^Q>3^d,
\]

or

\[
\boxed{
Q>rac{\log3}{\log(3/2)}d
\approx2.70951129135\,d.
}
\]

For a worst Beatty phase, where the prefactor `3^b/2^B` can approach 3, a sufficient scale for potential coverage is one additional surplus unit:

\[
Q>2.70951129135\,(d+1).
\]

## 4. Exact threshold examples

The first blind surplus values are

- Q1 -> d1
- Q2 -> d1
- Q3 -> d2
- Q4 -> d2
- Q5 -> d2
- Q6 -> d3
- Q7 -> d3
- Q8 -> d3
- Q9 -> d4
- Q10 -> d4
- Q14 -> d6
- Q17 -> d7
- Q20 -> d8.

Thus the observed record excursion reaching surplus 9 cannot be addressed uniformly by a small fixed Q reverse mechanism.

## 5. DSD consequence

The state decomposition now has a genuine scale relation:

\[
\text{surplus resolution }d
\quad\longleftrightarrow\quad
\text{reverse resolution }Q.
\]

A fixed-Q proof must therefore provide a separate theorem that keeps the actual candidate language tight in a bounded surplus strip.

If such a tail-tightness theorem is unavailable, Q must adapt with the surplus, at least at the linear scale

\[
Q\gtrsim2.71d.
\]

This produces two viable proof architectures.

### Architecture A: fixed-Q plus tail tightness

1. Beatty macro Lyapunov controls high surplus in a weighted sense.
2. Prove that the actual integer/candidate language cannot concentrate indefinitely in that weighted tail.
3. Fixed finite `(d,z)` reverse transfer then supplies the low-strip elimination.

### Architecture B: adaptive Q

1. Allow Q to grow with the reachable surplus.
2. Keep `Q(d)` above the blind-threshold scale.
3. Prove that enough ternary-selector mixing remains after this increase in resolution.

The current finite evidence does not yet decide which architecture closes.

## 6. Relation to the minimal-survivor route

The long excursion of the exact record path shows that the next structural target should not be a uniform return-time bound for `d=0`.

A more promising target is:

> large surplus should force the canonical positive residue / minimal surviving integer to grow.

That would connect the Beatty-surplus coordinate directly to the existing min-plus target

\[
\mu(K)=\min\{n:\tau_c(n)>K\},
\]

and would turn the high-surplus escape from an obstruction into a lower-bound mechanism for `mu(K)`.

This is the next calculation line.

## 7. Reproducibility

Source:

`collatz/src/dsd_surplus_tail_obstruction_audit.py`

Expected final line:

`PASS`
