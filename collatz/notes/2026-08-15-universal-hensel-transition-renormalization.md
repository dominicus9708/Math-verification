# Universal Hensel transition renormalization

Date: 2026-08-15

Status: **exact universal recurrence + monotone-credit reduction + single-crossing theorem + asymptotic threshold law + finite exact certificates**.  This compresses the first- and second-return transition-band magnitude calculations into one gate-independent integer orbit.  It does not prove the Collatz conjecture and does not control the full same-state mixed-place fibre beyond the transition-section magnitude obstruction.

## 1. Gate-wide transition target collapses to one universal Hensel orbit

For a gate-wide cube

\[
1^F(01/10)^J0,
\qquad q=F+J,
\]

the normalized Hensel target for an incoming positive predecessor credit `delta` is

\[
T_\delta=-2^{2J+1}\delta\pmod{3^q}.
\]

The balanced lifting recurrence uses

\[
U_0=4^{-(J-1)}T_\delta\pmod{3^q}.
\]

Because

\[
4^{J-1}=2^{2J-2},
\]

the normalization is exact:

\[
\boxed{U_0\equiv-8\delta\pmod{3^q}.}
\]

In the certified no-wrap regime use the ordinary negative representative and write

\[
U_n=-x_n,
\qquad x_n>0.
\]

Let `a_n` be the balanced residue of `x_n` modulo three,

\[
a_n\in\{-1,0,1\},
\qquad a_n\equiv x_n\pmod3.
\]

Then the balanced-Hensel recurrence becomes

\[
\boxed{
x_{n+1}=\frac43(x_n-a_n)
=4\left\lfloor\frac{x_n+1}{3}\right\rfloor,
\qquad x_0=8\delta.
}
\]

This map contains no gate parameter.  The gate enters only through the number of lifts.

At transition width `h`, put

\[
n=J-h.
\]

The required boundary correction magnitude is exactly

\[
\boxed{
T_h(\delta)=2^{3h-2}x_{J-h}(\delta)
}
\]

as long as this is below the least-signed modular wrap threshold.

For all eight currently certified gate sections and every `1<=delta<=397`, the no-wrap inequality holds by hundreds of decimal orders of magnitude at the transition crossing.

## 2. Positive-credit monotonicity theorem

The map

\[
x\mapsto4\left\lfloor\frac{x+1}{3}\right\rfloor
\]

is nondecreasing on the nonnegative integers.

Therefore

\[
\delta_1<\delta_2
\Longrightarrow
x_n(\delta_1)\le x_n(\delta_2)
\quad\text{for every }n.
\]

Hence in every no-wrap gate section,

\[
\boxed{
T_h(1)\le T_h(2)\le\cdots.
}
\]

Consequently, among all positive bounded predecessor credits, the magnitude obstruction is always weakest at

\[
\boxed{\delta=1.}
\]

This explains why `delta=1` was the first non-excluded credit in all earlier first- and second-return scans.  It is not an empirical coincidence.

The previous `397 x h` bounded-credit calculation therefore collapses to one universal `delta=1` orbit.

## 3. Exact boundary capacity and single-crossing theorem

For an arbitrary length-`3h` transition word with exactly `2h` odd symbols, the exact maximal correction-difference magnitude is

\[
\boxed{
M_h=(2^h-1)(3^{2h}-4^h)
=(2^h-1)(9^h-4^h).
}
\]

For `h>=2`,

\[
\frac{M_h}{M_{h-1}}>18.
\]

Indeed this reduces to

\[
4\,9^h>9\,4^h,
\]

which holds for every integer `h>=2`.

Now compare consecutive required targets along the universal orbit.  If `n=J-h`,

\[
\frac{T_h(1)}{T_{h-1}(1)}
=8\frac{x_n}{x_{n+1}}.
\]

Since the `delta=1` orbit starts at `x_0=8` and remains at least eight, residue-class inspection gives

\[
\boxed{
8\frac{x_n}{x_{n+1}}\le7.
}
\]

Therefore

\[
\boxed{
\frac{M_h/T_h(1)}{M_{h-1}/T_{h-1}(1)}
>\frac{18}{7}>1.
}
\]

Thus the transition magnitude ratio is strictly increasing with `h` in the no-wrap regime.

The magnitude barrier therefore has **at most one crossing**:

\[
\boxed{
h_*(J)
:=\min\{h:M_h\ge T_h(1)\}
}
\]

is the unique point after which scalar magnitude alone ceases to exclude the easiest positive credit.

## 4. Universal normalized Hensel constant

Put

\[
y_n:=\left(\frac34\right)^n x_n.
\]

From

\[
x_{n+1}=\frac43(x_n-a_n)
\]

one obtains

\[
\boxed{
y_{n+1}=y_n-a_n\left(\frac34\right)^n.}
\]

Since `|a_n|<=1`, the series is absolutely summable.  Therefore

\[
\boxed{
\kappa(\delta)
:=\lim_{n\to\infty}\left(\frac34\right)^n x_n(\delta)
}
\]

exists, with the exact tail bound

\[
\boxed{
\left|
 x_n(\delta)-\kappa(\delta)\left(\frac43\right)^n
\right|\le4.
}
\]

For the universal minimal positive credit `delta=1`, a 250-step exact rational certificate gives

\[
\boxed{
8.3055829231986668552562870614508422678756
<\kappa_1
<8.3055829231986668552562870614513082892485.
}
\]

No floating-point assumption is used in this interval: it follows from the exact integer `x_250` and the geometric tail bound.

## 5. Asymptotic transition law

Using the previous error estimate,

\[
T_h(1)
=2^{3h-2}x_{J-h}(1)
\]

gives

\[
\boxed{
T_h(1)
=\frac{\kappa_1}{4}
6^h\left(\frac43\right)^J
+E_h,
\qquad |E_h|\le2^{3h}.
}
\]

Also

\[
\boxed{
M_h
=18^h
(1-2^{-h})
\left(1-\left(\frac49\right)^h\right).
}
\]

Ignoring only exponentially small relative corrections, the crossing equation is therefore

\[
18^h
\sim
\frac{\kappa_1}{4}
6^h\left(\frac43\right)^J,
\]

or

\[
3^h
\sim
\frac{\kappa_1}{4}
\left(\frac43\right)^J.
\]

Hence

\[
\boxed{
h_*(J)
=J\log_3\frac43
+\log_3\frac{\kappa_1}{4}
+o(1).
}
\]

Numerically,

\[
\boxed{
\log_3\frac43
=0.2618595071429148741990542287\ldots
}
\]

and

\[
\boxed{
\log_3\frac{\kappa_1}{4}
\approx0.6650513347123352.
}
\]

Thus the first-order threshold depends only on the pair count `J`; the front length `F` matters only through modular-wrap safety and through the gate's critical relation between `F` and `J`.

## 6. Relation to the mechanical critical slope

Let

\[
\alpha:=\log_3 2.
\]

Then

\[
\log_3\frac43
=2\alpha-1.
\]

For critical mechanical gates,

\[
\frac{F+J}{F+2J}\to\alpha,
\]

which implies

\[
\frac{J}{F}	o
\frac{1-\alpha}{2\alpha-1}.
\]

Therefore

\[
\boxed{
\frac{h_*}{F}\to1-\alpha
=\log_3\frac32
=0.3690702464285425629004728857\ldots
}
\]

This explains the approximately `0.3691` ratios observed at `G13/G14`.  The same complementary Beatty slopes reappear inside the transition-width obstruction:

\[
\boxed{
\frac{h_*}{J}\to2\alpha-1,
\qquad
\frac{h_*}{F}\to1-\alpha.
}
\]

## 7. Exact unification of all current gate thresholds

The continuous predictor

\[
H(J)
:=J\log_3\frac43
+\log_3\frac{\kappa_1}{4}
\]

has the following values:

\[
\boxed{\begin{array}{c|c|c|c}
\text{gate/fibre}&J&H(J)&h_*\text{ exact}\\\hline
G_{81}\text{ neutral}&567&149.1393918847\ldots&150\\
G_{81}\text{ one-slack}&568&149.4012513919\ldots&150\\
G_{82}\text{ neutral}&574&150.9724084347\ldots&151\\
G_{82}\text{ one-slack}&575&151.2342679419\ldots&152\\
G_{13}\text{ neutral}&7390&1935.8068091209\ldots&1936\\
G_{13}\text{ one-slack}&7391&1936.0686686280\ldots&1937\\
G_{14}\text{ neutral}&7958&2084.5430091780\ldots&2085\\
G_{14}\text{ one-slack}&7959&2084.8048686852\ldots&2085
\end{array}}
\]

In all eight cases,

\[
\boxed{h_*=\lceil H(J)\rceil.}
\]

The equality for these eight cases is certified by exact integer comparisons at `h_*-1` and `h_*`, plus the single-crossing theorem.  The logarithmic predictor is not used as the proof of those finite values.

## 8. Large-J exact diagnostic

An exact integer scan of the universal threshold function through

\[
2\le J\le200,000
\]

was compared with

\[
\left\lceil
J\log_3\frac43
+\log_3\frac{\kappa_1}{4}
\right\rceil.
\]

The only mismatches found were the small depths

\[
\boxed{J=4,5,28.}
\]

No mismatch occurred for

\[
\boxed{29\le J\le200,000.}
\]

This is computational evidence for eventual exact Beatty-type rounding of the threshold law, not a proof for all `J`.  A global eventual-rounding theorem would require controlling how closely the irrational linear predictor can approach an integer relative to the exponentially small finite-depth errors.

## 9. Strategic consequence for the Collatz proof program

The transition-magnitude branch is now substantially compressed:

1. `delta=1` is provably the only positive credit that needs to be tested for magnitude onset;
2. the boundary-capacity ratio has a unique crossing;
3. the crossing is governed by one universal balanced-Hensel orbit;
4. all current first- and second-return thresholds are unified by the same `J`-law;
5. the observed complementary critical ratios are analytically explained.

Therefore further brute-force extension of the scalar transition-width calculation is low priority.  At larger Euclidean gates the threshold can be predicted and then certified with only local exact checks.

The unresolved Collatz obstruction remains the stronger object already identified previously:

\[
\boxed{
\text{same-word mixed-place joint image / fixed-Hensel dyadic kernel}
}
\]

beyond the scalar magnitude barrier.  A candidate transition block first becomes *large enough* near `h_*(J)`, but it must still satisfy the same survival state, the fixed ternary Hensel target, the dyadic canonical-address target, and the ordinary renewal-gap condition simultaneously.

The next calculation should therefore condition on the universal transition coordinate near `h_*` and determine the dyadic image of the fixed-Hensel transition fibre rather than increase `h` blindly.

## Reproducibility

Exact certificate and optional large-J scan:

`collatz/src/universal_hensel_transition_threshold.py`
