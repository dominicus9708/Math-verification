# Gap-adjusted Christoffel renewal bound

Date: 2026-08-11

Status: **exact consequence of the rational renewal-cycle shadow and the Christoffel extremal bound**. This strengthens the floor-only resonance condition by retaining the integer gap between consecutive renewal floors.

## 1. Setup

Let `N<N'` be consecutive renewal floors connected by an aggregate-supercritical word. Write

\[
H=\text{odd-event count},
\qquad
D=\text{extra-halving count},
\]

\[
\alpha:=\log_2(3/2),
\qquad
\Delta:=D-\alpha H>0,
\]

and

\[
\boxed{g:=N'-N\ge2.}
\]

Let

\[
Z:=2^{H+D}-3^H.
\]

The associated positive rational cycle shadow has minimum

\[
C=N'+\frac{3^Hg}{Z}.
\]

Because

\[
2^{H+D}=3^H2^\Delta,
\]

one has

\[
Z=3^H(2^\Delta-1),
\]

so

\[
\boxed{
C=N'+\frac{g}{2^\Delta-1}.
}
\]

## 2. Gap-adjusted shadow ceiling

The Christoffel extremal theorem applied to the rational shadow minimum gives

\[
C\le
\frac{1}{2^{(H+D)/H}-3}.
\]

Since

\[
2^{(H+D)/H}
=3\,2^{\Delta/H},
\]

we obtain

\[
\boxed{
N'+\frac{g}{2^\Delta-1}
\le
\frac{1}{3\left(2^{\Delta/H}-1\right)}.
}
\]

This is strictly stronger than the floor-only bound

\[
N'<\frac{1}{3(2^{\Delta/H}-1)}.
\]

## 3. Gap ceiling

Solving for the integer floor increment,

\[
\boxed{
g
\le
(2^\Delta-1)
\left[
\frac{1}{3(2^{\Delta/H}-1)}-N'
\right].
}
\]

Because consecutive renewal floors are distinct odd integers,

\[
g\ge2.
\]

Hence every supercritical renewal must also satisfy

\[
\boxed{
N'
\le
\frac{1}{3(2^{\Delta/H}-1)}
-
\frac{2}{2^\Delta-1}.
}
\]

Thus the integer floor gap creates a nonzero forbidden margin below the Christoffel ceiling.

## 4. Exact depth cost

Using

\[
2^x-1\ge x\ln2
\qquad(x>0),
\]

we have

\[
\frac{1}{3(2^{\Delta/H}-1)}
\le
\frac{H}{3\Delta\ln2}.
\]

Therefore

\[
\boxed{
H
\ge
3\Delta\ln2
\left(
N'+\frac{g}{2^\Delta-1}
\right).
}
\]

This is a valid odd-event-depth lower bound derived from the rational shadow. It does not rely on the false assumption that every internal credit state exceeds the next renewal floor.

## 5. Critical-layer specialization

On the minimal supercritical layer,

\[
D=\lceil\alpha H\rceil,
\qquad
\Delta=\delta_H:=\lceil\alpha H\rceil-\alpha H\in(0,1).
\]

For `0<delta<1`, the function

\[
\frac{\delta\ln2}{2^\delta-1}
\]

is greater than `ln 2`. Consequently

\[
\boxed{
H
>
3\delta_H\ln2\,N'
+3(\ln2)g.
}
\]

In particular,

\[
\boxed{
H>3(\ln2)g\approx2.07944\,g.
}
\]

The exact critical-layer floor ceiling is sharpened to

\[
\boxed{
N'
\le
\frac{1}{3(2^{\delta_H/H}-1)}
-
\frac{2}{2^{\delta_H}-1}.
}
\]

## 6. Structural role

The renewal exceptional sector is now constrained simultaneously by four quantities:

- exponent resonance `Delta`;
- odd-event depth `H`;
- next renewal floor `N'`;
- integer floor increment `g`.

A supercritical renewal cannot sit arbitrarily close to the Christoffel upper envelope: its positive integer floor gap forces a definite separation from that extremal rational cycle.

This provides a stronger candidate input for a global renewal budget, especially on the minimal supercritical layer where `Delta<1`.
