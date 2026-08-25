# First global resonance: terminal low-support ladder through six defects

Date: 2026-08-26

Status: **exact finite theorem** in the repaired first-global-resonance branch. The result is a deterministic extension of the terminal 3-adic address. It does not use the ternary recursively-sufficient selector, repeated L7/L14 pullback, random sampling, or an independence assumption. It does not prove the Collatz conjecture.

## 1. Definition

For \(m\ge46\), let

\[
D_{\rm tail}(m)
=
\#\{j:Q_0-m+1\le j\le Q_0,\ a_j<b_j\}
\]

be the number of displaced odd ordinals among the final \(m\) odd ordinals of the repaired first resonance

\[
(A_0,Q_0)=(114208327604,72057431991).
\]

For a final-m window, number its mechanical positions from earliest to latest as

\[
B_t=b_{Q_0-m+1+t},\qquad0\le t<m,
\]

and write

\[
\delta_t=B_t-a_{Q_0-m+1+t}\ge0.
\]

The endpoint is exactly

\[
\boxed{
y=2^{-A_0}\sum_{t=0}^{m-1}3^{m-1-t}2^{B_t-\delta_t}
\pmod{3^m}.}
\]

Because every candidate endpoint satisfies \(y<2^{72}<3^{46}\), every admissible residue for \(m\ge46\) is the ordinary endpoint itself.

The t-th displacement is visible only modulo

\[
2\cdot3^t,
\]

and ordering gives

\[
\delta_t\le\delta_{t-1}+(B_t-B_{t-1})-1.
\]

These two facts make every fixed low-support layer finite.

## 2. Last 50: three defects are forced

Exact enumeration at \(m=50\) gives

\[
\begin{array}{c|r|r}
\text{exact support size}&\text{finite residue classes}&\text{admissible classes}\\\hline
0&1&0\\
1&31&0\\
2&502&0\\
3&5828&1
\end{array}
\]

The unique three-defect class is

\[
\boxed{
\operatorname{supp}(\delta)=(0,18,45),
\qquad
\delta_0=\delta_{18}=\delta_{45}=1,
}
\]

with endpoint

\[
\boxed{y=2697452540596458587755.}
\]

Therefore

\[
\boxed{D_{\rm tail}(50)\ge3.}
\]

This unique equality class extends mechanically through the newly prepended ordinal at \(m=51\), but its endpoint congruence fails modulo \(3^{52}\). Since any hypothetical support-three class at \(m=52\) would already have to contain the unique three defects inside the last 50, no other support-three extension exists. Hence

\[
\boxed{D_{\rm tail}(52)\ge4.}
\]

## 3. Last 52: four-defect equality is unique

At \(m=52\), exact support four has

\[
\boxed{72305}
\]

finite residue classes and exactly one admissible class:

\[
\boxed{
(11,12,41,51),
\qquad
\delta=(1,1,1,1),
}
\]

with endpoint

\[
\boxed{y=2704820911452840622043.}
\]

It extends mechanically through \(m=53,54,55\) and fails modulo \(3^{56}\). Therefore

\[
\boxed{D_{\rm tail}(56)\ge5.}
\]

## 4. Last 56: five-defect equality is unique

At \(m=56\), exact support five has

\[
\boxed{2886114}
\]

finite residue classes and again exactly one admissible class:

\[
\boxed{
(0,15,16,45,55),
\qquad
\delta=(1,1,1,1,1),
}
\]

with the same endpoint

\[
\boxed{y=2704820911452840622043.}
\]

It extends mechanically through \(m=57\) and fails modulo \(3^{58}\). Thus

\[
\boxed{D_{\rm tail}(58)\ge6.}
\]

Collecting the ladder,

\[
\boxed{
D_{\rm tail}(50)\ge3,
\quad
D_{\rm tail}(52)\ge4,
\quad
D_{\rm tail}(56)\ge5,
\quad
D_{\rm tail}(58)\ge6.
}
\]

## 5. Combination with the early 72-step boundary

The independently certified early boundary gives

\[
D_{72}\ge11.
\]

The earliest ordinal among the final 58 odd ordinals is \(Q_0-57\), and every j-th odd step satisfies \(a_j\ge j-1\). Hence

\[
a_{Q_0-57}\ge Q_0-58>72.
\]

The two support sets are therefore disjoint. Every remaining first-resonance candidate must satisfy

\[
\boxed{r_*\ge11+6=17.}
\]

Since every displaced odd ordinal contributes strictly more than \(1/12\) to the normalized correction defect,

\[
\boxed{E/3^{Q_0}>17/12.}
\]

The structural lower bound \(r_*\ge17\) is the important result; the correction increment itself is small.

## 6. DSD audit interpretation

The terminal address is no longer a single endpoint constraint. As the 3-adic resolution is raised,

\[
3^{46}\to3^{50}\to3^{52}\to3^{56}\to3^{58},
\]

the same global transport vector is asked to remain compatible with successively finer terminal descriptions. Low-support descriptions repeatedly collapse to one class and then fail at a slightly finer resolution.

Thus the current first-resonance state has a genuine two-ended formation requirement:

\[
\boxed{
D_{72}\ge11
\;\big|\;
\text{Beatty transport bridge}
\;\big|\;
D_{\rm tail}(58)\ge6.
}
\]

No independence between the two ends is asserted; they are disjoint projections of the same ordinal-transport state.

## 7. Next step

Brute-force exact support six at \(m=58\) is no longer the right implementation. If the initial positive run has length six, the triangular periods alone contain

\[
\prod_{t=0}^{5}(2\cdot3^t)
\]

residue combinations, so direct Cartesian enumeration grows sharply.

The next certificate should instead split the terminal address into two triangular blocks and use a meet-in-the-middle / Hensel join:

1. enumerate low-support contributions in an early terminal block;
2. enumerate low-support contributions in the late block;
3. join only sums whose exact residue lies in the ordinary endpoint band;
4. retain the ordering condition at the block interface;
5. classify the exact six-defect equality layer without scanning the full Cartesian residue product.

Companion certificate for the ladder through support five:

`collatz/src/first_resonance_terminal_low_support_ladder_certificate.py`.
