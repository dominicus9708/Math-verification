# Renewal nearest-critical-layer reduction

Date: 2026-08-11

Status: **exact global classification of renewal transitions into nearest-critical layers or macroscopic costs**. This does not by itself exclude an infinite renewal chain.

## 1. Setup

For one renewal-floor segment let

\[
H=\text{odd-event count},
\qquad
D=\text{extra-halving count},
\]

and

\[
\alpha:=\log_2(3/2).
\]

The aggregate multiplier is

\[
\boxed{P=2^{D-\alpha H}.}
\]

Because `alpha` is irrational, `D-alpha H` is never zero.

## 2. Subcritical transitions below the nearest layer force floor doubling

Assume

\[
P<1,
\qquad
D<\alpha H.
\]

The exact renewal product has positive correction `Q>1`:

\[
P\frac{N'}N=Q.
\]

Hence

\[
\frac{N'}N>\frac1P=2^{\alpha H-D}.
\]

If

\[
D\le\lfloor\alpha H\rfloor-1,
\]

then

\[
\alpha H-D>1.
\]

Therefore

\[
\boxed{N'>2N.}
\]

Consequently every subcritical renewal satisfying

\[
N'\le2N
\]

must lie on the unique nearest lower critical layer

\[
\boxed{D=\lfloor\alpha H\rfloor.}
\]

## 3. Supercritical transitions above the nearest layer force linear depth

Assume

\[
P>1,
\qquad
D>\alpha H.
\]

The Christoffel renewal-shadow bound gives

\[
0<D-\alpha H
<
H\beta(N'),
\]

where

\[
\boxed{
\beta(N'):=
\log_2\left(1+\frac1{3N'}\right).
}
\]

If

\[
D\ge\lceil\alpha H\rceil+1,
\]

then

\[
D-\alpha H>1.
\]

Thus necessarily

\[
H\beta(N')>1,
\]

or

\[
\boxed{
H>eta(N')^{-1}.
}
\]

As `N'->infinity`,

\[
\boxed{
\beta(N')^{-1}
\sim3(\ln2)N'
\approx2.07944N'.
}
\]

Therefore every supercritical renewal whose odd-event depth is sublinear relative to the next floor must lie on the unique nearest upper critical layer

\[
\boxed{D=\lceil\alpha H\rceil.}
\]

## 4. Four-way renewal classification

Every renewal transition therefore belongs to at least one of the following structural classes:

\[
\boxed{
\begin{array}{ll}
\text{lower critical layer:}&D=\lfloor\alpha H\rfloor,\\[1mm]
\text{upper critical layer:}&D=\lceil\alpha H\rceil,\\[1mm]
\text{macroscopic floor jump:}&N'>2N,\\[1mm]
\text{linear-depth overload:}&H>\beta(N')^{-1}.
\end{array}
}
\]

The classes are not mutually exclusive; the point is that a transition outside the two nearest critical layers must pay one of the two macroscopic costs.

## 5. Accelerated-length form

Since

\[
A=H+D
\]

and `H` is an integer,

\[
H+\lfloor\alpha H\rfloor
=\lfloor H\log_2 3\rfloor,
\]

\[
H+\lceil\alpha H\rceil
=\lceil H\log_2 3\rceil.
\]

Thus the two economical layers are exactly

\[
\boxed{
A=\lfloor H\log_2 3\rfloor
}
\]

and

\[
\boxed{
A=\lceil H\log_2 3\rceil.
}
\]

In other words, an economical renewal transition must choose one of the two integers immediately adjacent to the critical real exponent `H log_2 3`.

## 6. Multiplier form on the two nearest layers

Let

\[
f_H:=\{\alpha H\}\in(0,1).
\]

Then on the lower layer

\[
\boxed{P_-(H)=2^{-f_H}\in(1/2,1),}
\]

while on the upper layer

\[
\boxed{P_+(H)=2^{1-f_H}\in(1,2).}
\]

Hence after removal of macroscopic-cost transitions, the aggregate coefficient is determined completely by the irrational rotation `f_H={alpha H}` and the choice of lower/upper adjacent layer.

## 7. Next theorem target

A unified renewal proof may now separate two tasks:

1. show that macroscopic-cost transitions (`N'>2N` or `H \gtrsim N'`) cannot sustain an infinite exact positive-integer renewal chain without forcing a global progress contradiction;
2. analyze the residual nearest-layer language, where every economical transition is coded by the two adjacent Beatty layers around `H log_2 3`.

The second part is a much thinner arithmetic system than the original Collatz parity space and is a natural target for continued-fraction, Christoffel/Sturmian, and mixed 2-adic/3-adic formation arguments.
