# Macroblock arithmetic bridge and one-parameter resonance reduction

Date: 2026-08-11

Status: **exact macroblock normal form + mixed 2-adic/3-adic bridge + one-parameter resonance reduction**. This note does not claim a proof of the Collatz conjecture.

## 1. Macroblock parameters

Use the odd-event dynamics from

`collatz/notes/2026-08-11-frontier-event-budget-critical-resonance.md`.

A maximal macroblock consists of

- \(\ell\ge0\) consecutive credit events with valuation \(a=1\);
- one debit event with valuation \(b\ge2\).

Define

\[
\boxed{h:=\ell+1,\qquad d:=b-1.}
\]

The corresponding accelerated parity block is exactly

\[
\boxed{1^h0^d.}
\]

Its accelerated length is \(h+d\) and its odd-count is \(h\).

---

## 2. Exact normal form of one macroblock

At the beginning of the block, maximality of the credit run gives

\[
\boxed{h=v_2(x+1).}
\]

Hence

\[
\boxed{x+1=2^h u}
\]

for a unique odd positive integer \(u\).

Applying the \(h\) consecutive odd accelerated branches gives

\[
T_1^h(x)+1
=
\left(\frac32\right)^h(x+1),
\]

so after the final odd branch and before the trailing even divisions,

\[
\boxed{y=3^h u-1.}
\]

The number of trailing even steps is

\[
\boxed{d=v_2(3^h u-1).}
\]

and the next odd state is

\[
\boxed{
x'
=
\frac{3^h u-1}{2^d}.
}
\]

Thus one macroblock is represented exactly by

\[
\boxed{
2^h u-1
\longmapsto
\frac{3^h u-1}{2^d},
\qquad
u_2(3^h u-1)=d.
}
\]

---

## 3. Mixed 2-adic and 3-adic alignment

The start of the block satisfies

\[
\boxed{x\equiv-1\pmod{2^h}.}
\]

Exactness of the debit valuation gives

\[
3^h u-1
\equiv
2^d
\pmod{2^{d+1}},
\]

hence

\[
\boxed{
u
\equiv
3^{-h}(1+2^d)
\pmod{2^{d+1}}.
}
\]

Therefore the complete macroblock type \((h,d)\) fixes the current odd state to one residue class modulo

\[
\boxed{2^{h+d+1}.}
\]

On the output side,

\[
2^d x'+1=3^h u,
\]

so

\[
\boxed{
x'
\equiv
-2^{-d}
\pmod{3^h}.
}
\]

If the next macroblock has credit depth \(h'\), then simultaneously

\[
\boxed{x'\equiv-1\pmod{2^{h'}}.}
\]

Thus a transition between two macroblocks is a mixed CRT bridge:

\[
\boxed{
\begin{cases}
x'\equiv-2^{-d}\pmod{3^h},\\
x'\equiv-1\pmod{2^{h'}}.
\end{cases}
}
\]

Since \(2^{h'}\) and \(3^h\) are coprime, this determines a unique residue class modulo

\[
\boxed{2^{h'}3^h.}
\]

This is the natural static aggregate for transitions between critical macroblocks.

---

## 4. State-size cost of credit alignment

Because \(u\ge1\),

\[
\boxed{x\ge2^h-1.}
\]

Similarly,

\[
\boxed{
x'
\ge
\frac{3^h-1}{2^d}.
}
\]

Hence a long credit run requires an exponentially large current odd state in the alignment depth \(h\).

The resource gained from the run, however, is bounded by a geometric series in the multiplier coordinate. This separates state-size cost from headroom credit.

---

## 5. Macroblock multiplier

The multiplier coordinate changes by

\[
\boxed{
M_{h,d}
:=
\frac{\lambda'}{\lambda}
=
\frac{2^{h+d}}{3^h}.
}
\]

Equivalently,

\[
\boxed{
M_{h,d}
=
2^{d-h\theta},
\qquad
\theta:=\log_2\frac32.
}
\]

The exact odd-state map can also be written as

\[
\boxed{
x'
=
\frac{x+1}{M_{h,d}}-2^{-d}.}
\]

Therefore

\[
M_{h,d}>1
\Longrightarrow
x'<x+1.
\]

Since \(x,x'\) are integers,

\[
\boxed{
M_{h,d}>1
\Longrightarrow
x'\le x.
}
\]

Equality corresponds to exact return of the odd state across that macroblock and hence to a periodic closure of that block.

Thus multiplier-noncontracting blocks cannot increase the odd state; multiplier-contracting blocks are the only macroblocks that can produce unrestricted real growth.

---

## 6. Headroom change in h,d variables

From the event-budget identity,

\[
\boxed{
H'-H
=
\frac{\lambda}{n}
\left[
1-\left(\frac23\right)^h
-n\bigl(M_{h,d}-1\bigr)
\right].
}
\]

This form makes the tradeoff with \(M\) explicit.

If

\[
H'-H\ge0
\]

and

\[
M_{h,d}\ge1,
\]

then

\[
0
\le
M_{h,d}-1
\le
\frac{1-(2/3)^h}{n}
<
\frac1n.
\]

Hence

\[
\boxed{
1\le M_{h,d}<1+\frac1n.
}
\]

---

## 7. One-parameter resonance reduction

For an odd unresolved start \(n>1\), necessarily \(n\ge3\), so

\[
1+\frac1n\le\frac43<2.
\]

For fixed \(h\), increasing \(d\) by one doubles \(M_{h,d}\). Therefore if

\[
1\le M_{h,d}<1+\frac1n<2,
\]

then \(d\) must be the unique least integer for which \(M\ge1\):

\[
\boxed{
d=\lceil h\theta\rceil,
\qquad
\theta=\log_2\frac32.
}
\]

Define the upper-integer gap

\[
\boxed{
\delta_h
:=
\lceil h\theta\rceil-h\theta.
}
\]

Because \(\theta\) is irrational,

\[
0<\delta_h<1.
\]

For the unique noncontracting candidate,

\[
M_{h,d}=2^{\delta_h}.
\]

The double-no-loss condition therefore becomes

\[
\boxed{
0<\delta_h
<
\log_2\left(1+\frac1n\right).
}
\]

Thus a potentially persistent macroblock is indexed by one integer \(h\), not two independent integers \((h,d)\), and \(h\theta\) must lie in a narrow interval immediately below an integer.

---

## 8. Interpretation

The original accelerated trajectory branches at every parity step. The odd-event representation groups those steps into blocks. The present reduction then shows:

1. a block is determined arithmetically by a 2-adic credit depth \(h\) and a debit depth \(d\);
2. ordinary blocks lose either headroom or multiplier scale;
3. avoiding both losses forces \(d=\lceil h\log_2(3/2)\rceil\);
4. the remaining candidate depths \(h\) are upper Diophantine approximations to \(\log_2(3/2)\);
5. transitions between such blocks satisfy a mixed CRT condition modulo \(2^{h'}3^h\).

The next target is therefore no longer enumeration of arbitrary parity words. It is the transition graph of the one-parameter critical depths \(h\), with exact CRT realizability and headroom constraints attached.

A proof route would show that no finite positive-integer trajectory can traverse this critical bridge graph indefinitely while preserving \(H\ge0\).
