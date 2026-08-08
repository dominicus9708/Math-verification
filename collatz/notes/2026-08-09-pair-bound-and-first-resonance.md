# Pairwise correction bound and elimination of the first 72-bit resonance

Date: 2026-08-09

Status: proof-oriented derived result for the finite first-coefficient-crossing branch. It does not prove the Collatz conjecture or CST globally.

## 1. Mechanical-boundary correction

At first coefficient crossing with q odd entries, the maximal normalized correction over admissible parity words is attained by the mechanical boundary word. Its odd positions satisfy

\[
d_i^*=\lfloor i\log_2 3\rfloor,\qquad i=0,\ldots,q-1,
\]

and

\[
S^*(q)=\sum_{i=0}^{q-1}\frac{2^{d_i^*}}{3^{i+1}}
=\frac13\sum_{i=0}^{q-1}2^{-\{i\log_2 3\}}.
\]

Write
\[
\beta=\log_2(3/2),\qquad \gamma=1-\beta=\log_2(4/3).
\]
If r={i log_2 3}, then the next fractional part is {r+beta}.

For
\[
u_i=\frac13 2^{-r},
\]
there are two cases.

If 0<=r<gamma,
\[
u_i+u_{i+1}=\frac13 2^{-r}(1+2^{-\beta})
=\frac59 2^{-r}\le\frac59.
\]

If gamma<=r<1,
\[
u_i+u_{i+1}=\frac13 2^{-r}(1+2^{1-\beta})
=\frac79 2^{-r}\le\frac79\,2^{-\gamma}=\frac7{12}.
\]

Hence every consecutive pair satisfies
\[
\boxed{u_i+u_{i+1}\le\frac7{12}}.
\]
Therefore
\[
\boxed{
S^*(q)\le
\begin{cases}
7q/24,&q\text{ even},\\
(7q+1)/24,&q\text{ odd}.
\end{cases}}
\]
A convenient uniform bound is
\[
\boxed{S^*(q)\le(7q+1)/24}.
\]

This is elementary and avoids the earlier Denjoy--Koksma estimate when only a coarse global upper bound is required.

## 2. Consequence for a paradoxical first crossing

Let
\[
\sigma=\lceil q\log_2 3\rceil,\qquad
\delta=\frac{2^\sigma}{3^q}-1>0.
\]
Since
\[
T^\sigma(x)=\frac{x+S(w)}{1+\delta},
\]
a paradoxical first crossing T^sigma(x)>=x requires
\[
x\le\frac{S(w)}{\delta}\le\frac{S^*(q)}{\delta}.
\]
Thus
\[
\boxed{x\le \frac{7q+1}{24\delta}}.
\]

## 3. Updated verified lower bound

Barina (2025) directly verified all starts below 2^71. Ansari (2025), Proposition 3.2 / Remark 3.1, proves a recursive-sufficiency extension: with n=44 this raises the covered interval to
\[
\boxed{L=4\cdot3^{44}+2=3,939,083,608,734,444,931,526}.
\]
Numerically
\[
\log_2 L\approx71.7383500317.
\]

## 4. First 72-bit resonance

The first previously identified strong upper resonance is
\[
q=72,057,431,991,\qquad
\sigma=114,208,327,604.
\]
For this pair,
\[
\delta=\frac{2^\sigma}{3^q}-1
\approx5.5108900957847576\times10^{-12}.
\]
The pair bound gives
\[
S^*(q)\le\frac{7q+1}{24}
=21,016,750,997.416\ldots
\]
and therefore
\[
x\le 3.8136763085680545\times10^{21}.
\]
But
\[
L=3.939083608734445\times10^{21},
\]
so the intervals do not overlap.

Hence this specific first-crossing resonance cannot contain a minimal Collatz counterexample, assuming the cited verified interval and the standard first-crossing majorization setup.

## 5. Numerically stable certification inequality

No gigantic integer 3^q needs to be materialized. The desired inequality
\[
\frac{(7q+1)/24}{2^\sigma/3^q-1}<L
\]
is equivalent to
\[
\boxed{7q+1<24L\left(e^{\sigma\ln2-q\ln3}-1\right)}.
\]
A 100-digit Wolfram interval calculation padded by 10^-90 on ln 2 and ln 3 gives the right-minus-left margin
\[
1.6586540362\times10^{10}
\]
with an interval width negligible compared with the positive margin. A fully formal publication certificate should replace the padded decimal log intervals by explicit rational upper/lower bounds for ln 2 and ln 3.

## 6. Next resonance

The next upper continued-fraction convergent has
\[
q=137,528,045,312,\qquad
\sigma=217,976,794,617.
\]
Here the same pair bound allows a much larger start, about
\[
4.4636\times10^{22},
\]
so the current verified lower bound does not eliminate this resonance.

Thus the proof program advances one Diophantine resonance, but does not close the finite-crossing branch globally.
