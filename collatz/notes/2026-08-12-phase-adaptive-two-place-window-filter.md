# Phase-adaptive two-place backtrace filter on the `m=44` local language

Date: 2026-08-12

Status: **exact finite phase-cylinder refinement** of the repeated `3`-adic backtrace filter at the current `m=44` R1 resonance. The calculation keeps the full Sturmian factor cylinder rather than substituting the worst-case phase `theta<1`, and raises the universal defect floor to `19.5663%`. This does not close the `m=44` block.

## 1. Setup

Use

\[
A=217,976,794,617,
\qquad
H=137,528,045,312,
\]

and the strategically first remaining recursively sufficient block

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Its lower endpoint is above

\[
V_0:=4\cdot3^{44}+2.
\]

On an R1 segment write

\[
\alpha=\log_2(3/2),
\qquad
\theta_i=\{i\alpha\},
\qquad
h_i=\lfloor i\log_2 3\rfloor-a_i^{\rm cum}.
\]

At a zero-defect endpoint,

\[
h_i=0,
\]

the exact state formula gives

\[
\boxed{x_i=(N+c_i)2^{\theta_i},}
\qquad
c_i<\frac H3.
\]

Therefore every `m=44` candidate satisfies the uniform bound

\[
\boxed{
x_i<\left(N+\frac H3\right)2^{\theta_i}.}
\]

## 2. Phase-adaptive predecessor exclusion

Take a positive odd-to-odd backtrace code of odd-depth `q`, total binary exponent `K`, and endpoint residue class `rho mod 3^q`.

Its positive ancestor obeys

\[
m<\frac{2^K}{3^q}x_i.
\]

A sufficient condition for `m<N` is therefore

\[
\frac{2^K}{3^q}
2^{\theta_i}
\left(N+\frac H3\right)
<N.
\]

Because

\[
\frac{N}{N+H/3}
\]

is increasing in `N`, it is enough to impose the exact lower-floor condition

\[
\boxed{
2^K 2^{\theta_i}(3V_0+H)
<3^{q+1}V_0.
}
\]

Unlike the previous `lambda<1/2` filter, this can reject codes with multiplier much closer to one whenever the rotation phase is low.

Examples include

\[
\lambda=\frac89
\]

at odd-depth two and

\[
\lambda=\frac{16}{27}
\]

at odd-depth three.

## 3. Exact Sturmian phase cylinders

The critical valuation increments are

\[
r_i=1+\lfloor(i+1)\alpha\rfloor-\lfloor i\alpha\rfloor.
\]

A length-47 factor is constant on one of the 48 rotation intervals cut out by

\[
\boxed{b_j:=\{-j\alpha\},\qquad 0\le j\le47.}
\]

Thus the 48 critical factors and the 48 phase cylinders are the same finite partition.

No floating logarithms are required to order the breakpoints. For `j>0`,

\[
2^{\{j\alpha\}}
=
\frac{3^j}{2^{j+\lfloor j\alpha\rfloor}},
\]

and

\[
\lfloor j\alpha\rfloor
=\operatorname{bit\_length}(3^j)-1-j.
\]

Since `2^x` is increasing, two fractional parts are ordered by exact cross multiplication of these rational powers of two and three.

## 4. Exact endpoint phase supremum inside one factor cylinder

Let a factor cylinder have upper breakpoint

\[
b_u=\{-u\alpha\}.
\]

At local endpoint offset `s`, `1<=s<=47`, the phase is

\[
\theta_s=\{t+s\alpha\}
\]

with `t` ranging over the factor interval.

Because the full breakpoint partition contains every wrap point relevant to these 47 offsets, `theta_s` is monotone on the cylinder. Its supremum is therefore obtained at the upper boundary.

If `s=u`, the phase approaches one from below, so

\[
\sup 2^{\theta_s}=2.
\]

Otherwise put

\[
n=s-u.
\]

For `n>0`,

\[
\boxed{
\sup 2^{\theta_s}
=
\frac{3^n}{2^{n+\lfloor n\alpha\rfloor}}.
}
\]

For `n=-k<0`,

\[
\boxed{
\sup 2^{\theta_s}
=
\frac{2^{k+\lfloor k\alpha\rfloor+1}}{3^k}.
}
\]

Hence every phase bound used below is an exact rational number.

## 5. Uniform factor-cylinder rejection

For each critical factor, endpoint offset `s`, reverse depth `q<=8`, and endpoint residue `z mod 3^q`:

1. compute the minimum total binary exponent `K` of a positive `q`-step backtrace code admissible at `z`;
2. compute the exact phase supremum of Section 4;
3. reject that zero-defect endpoint only if

\[
\boxed{
2^K
\left(\sup 2^{\theta_s}\right)
(3V_0+H)
<3^{q+1}V_0.
}
\]

Because the **supremum** phase is used, a rejected local path is impossible for every actual occurrence represented by the entire Sturmian cylinder. No individual one of the `H` rotation phases is inspected.

## 6. Transition-conditioned local DP

As before,

\[
v_i=r_i+h_i-h_{i+1},
\qquad
h_{i+1}\le h_i+r_i-1.
\]

Use length-47 zero-endpoint windows and track

\[
(h,j,z),
\]

where

- `h` is current skew height;
- `j` is the number of positive internal skew coordinates;
- `z` is the endpoint correction residue modulo `3^8=6561`.

The residue update is

\[
\boxed{
z'=(3z+1)2^{-v_i}\pmod{6561}.}
\]

At every zero-defect endpoint, apply the phase-adaptive factor-cylinder rule above.

The first exact local capacities are

\[
\boxed{
\begin{array}{c|r}
j&C_j\\\hline
0&48\\
1&917\\
2&8,670\\
3&54,571\\
4&261,464\\
5&1,039,208\\
6&3,648,409\\
7&11,817,020\\
8&36,218,453\\
9&106,421,013\\
10&302,053,320\\
11&832,527,194\\
12&2,235,808,308\\
13&5,861,901,291\\
14&15,030,454,288\\
15&37,768,158,351\\
16&93,181,056,705\\
17&225,996,617,115\\
18&539,207,029,169\\
19&1,266,583,233,763\\
20&2,932,001,326,061
\end{array}
}
\]

These are smaller than the phase-blind `q<=8` capacities, for example

\[
C_{10}:406,050,905\longrightarrow302,053,320.
\]

## 7. Global overlapping-window threshold

There are `H-47` length-47 window positions.

If

\[
r_*:=\#\{i:0\le i<H,\ h_i>0\},
\]

then at least

\[
E=H-47-2r_*
\]

windows have zero endpoints, while the total internal defect incidence is at most

\[
46r_*.
\]

Let `Phi(E)` be the greedy minimum incidence cost using the capacities of Section 6.

The necessary condition remains

\[
\boxed{
\Phi(H-47-2r_*)\le46r_*.
}
\]

Exact integer evaluation gives the first admissible value

\[
\boxed{r_*=26,909,266,900.}
\]

At the previous integer,

\[
E=83,709,511,467,
\]

\[
\Phi(E)=1,237,826,277,383
>
1,237,826,277,354
=46(26,909,266,899).
\]

At the threshold,

\[
E=83,709,511,465,
\]

\[
\Phi(E)=1,237,826,277,351
<
1,237,826,277,400
=46(26,909,266,900).
\]

Therefore every `m=44` candidate at the current resonance must satisfy

\[
\boxed{
\frac{r_*}{H}
>0.19566385051829158.
}
\]

Thus more than

\[
\boxed{19.5663\%}
\]

of all odd-event coordinates must depart from the critical mechanical cap.

An independent Wolfram exact-integer evaluation reproduces the two threshold inequalities.

## 8. Methodological significance

The refinement uses no enumeration of the `H` orbit positions and no enumeration of the `2^44` ternary starts.

The objects retained are only:

- 48 Sturmian factor cylinders;
- a finite `3`-adic residue channel modulo `3^8`;
- the skew-height transition;
- a finite defect-count cost;
- and exact rational phase bounds.

The inference chain is therefore

\[
\boxed{
\text{finite propositions on factor cylinders}
\Rightarrow
\text{local language deletion}
\Rightarrow
\text{global aggregate incidence lower bound}.}
\]

This is structurally closer to the intended set/proposition/aggregation proof style than a start-by-start scan.

## 9. Limit of further defect-count refinement

Although the phase-adaptive theorem is stricter, the low end of the `m=44` block still has a very large Archimedean correction allowance.

Consequently another small improvement from `q=9,10,...` is unlikely to close this block if its only final use is the scalar defect count `r_*` followed by the run-average estimate.

The stronger object is the two-place potential itself:

\[
\mathcal B_Q(x_i)+h_i+\theta_i+
\log_2\left(1+\frac{c_i}{N}\right)>0.
\]

Future work should preserve this coupled state rather than collapsing it immediately to a single defect count.
