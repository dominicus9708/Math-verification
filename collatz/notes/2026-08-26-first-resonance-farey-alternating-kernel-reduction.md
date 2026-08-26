# First resonance: Farey alternating-kernel reduction

Date: 2026-08-26

Status: **exact arithmetic reduction.** This note rewrites the mechanical sign/weight system on an almost exact rational grid. The remaining Hensel-sign correlation estimate is not yet proved. This is not a proof of the Collatz conjecture.

## 1. Farey coordinates

At the repaired first resonance,

\[
(A,Q)=(114208327604,72057431991),
\]

with lower Farey neighbour

\[
(A_-,Q_-)=(103768467013,65470613321),
\]

we have

\[
\frac{A_-}{Q_-}<\gamma:=\log_2 3<\frac AQ,
\qquad
AQ_- - A_-Q=1.
\]

For

\[
0\le n<Q,
\qquad
r_n:=nA\pmod Q,
\]

Farey adjacency gives

\[
\boxed{\lfloor n\gamma\rfloor=\left\lfloor\frac{nA}{Q}\right\rfloor.}
\]

Because \(A\) is even and \(Q\) is odd, writing

\[
nA=Qb_n+r_n
\]

immediately gives

\[
\boxed{b_n\equiv r_n\pmod2.}
\]

Thus the mechanical parity sign is exactly alternating in the Farey residue coordinate:

\[
\boxed{(-1)^{b_n}=(-1)^{r_n}.}
\]

Also

\[
AQ_-\equiv1\pmod Q,
\]

so

\[
\boxed{A^{-1}\equiv Q_-\pmod Q.}
\]

Hence the inverse permutation is explicit:

\[
n(r)=Q_-r\pmod Q.
\]

## 2. Mechanical weight becomes an almost-geometric grid

Let

\[
\Delta:=\frac AQ-\gamma>0.
\]

For \(n<Q\),

\[
\{n\gamma\}
=
\frac{r_n}{Q}-n\Delta.
\]

The normalized single-displacement weight is

\[
c_{n+1}
=
\frac16\,2^{-\{n\gamma\}}.
\]

Therefore

\[
\boxed{
c_{n+1}
=
\frac16\,2^{-r_n/Q}\,2^{n\Delta}.
}
\]

Define the ideal rational-grid weight

\[
\bar c_r:=\frac16\,2^{-r/Q}.
\]

Farey adjacency yields

\[
0<\Delta<\frac1{QQ_-},
\]

and therefore

\[
1<2^{n\Delta}<2^{1/Q_-}.
\]

Using an exact rational enclosure of \(\ln2\), the companion certificate proves that for **any choice of signs** the total signed-correlation error caused by replacing all true weights by \(\bar c_r\) is less than one:

\[
\boxed{
\sum_{n=0}^{Q-1}
\left|c_{n+1}-\bar c_{r_n}\right|<1.
}
\]

This error is negligible compared with the current correlation margin, which is tens of millions.

## 3. Exact ideal mechanical kernel

Since \(Q\) is odd, put

\[
x=2^{-1/Q}.
\]

Then \(x^Q=1/2\) and

\[
\frac16\sum_{r=0}^{Q-1}(-1)^r2^{-r/Q}
=
\frac16\sum_{r=0}^{Q-1}(-x)^r
=
\boxed{\frac1{4(1+x)}}.
\]

Numerically this is near \(1/8\), i.e. bounded independently of \(Q\). The huge mechanical weighted system therefore has essentially zero intrinsic alternating bias after the Farey permutation.

This does **not** by itself control the Hensel signs; it only removes the mechanical side as a complicated object.

## 4. Correlation target in residue coordinates

Let \(\varepsilon_n\in\{\pm1\}\) be the zero-target Hensel sign required when the ordinal corresponding to n is prepended. The true weighted correlation from the previous note is

\[
\mathcal C
=
\sum c_{n+1}\,(-1)^{b_n}\varepsilon_n.
\]

Under the Farey permutation this becomes, up to total error less than one,

\[
\boxed{
\mathcal C_0
=
\frac16
\sum_{r}
(-1)^r2^{-r/Q}
\varepsilon_{\,Q_-r\bmod Q}.
}
\]

For the actual zero-target range the final 46 ordinals are omitted; their total possible weight is at most

\[
46/6.
\]

The exact threshold note showed that a surviving first-resonance candidate needs actual positive correlation above roughly \(3.5\times10^7\). Because the irrational-to-grid error is <1, it is enough to prove, for example,

\[
\boxed{\mathcal C_0\le34,999,999.}
\]

This is deliberately a slightly stronger round target.

## 5. What remains nontrivial

The Hensel signs are not arbitrary independent signs. They are generated recursively by the terminal zero-target carry:

\[
c_m+2^{\widehat B_0-A-d}\equiv0\pmod3.
\]

The dangerous situation is precisely that the permuted Hensel sign sequence

\[
\varepsilon_{Q_-r\bmod Q}
\]

tracks the alternating pattern \((-1)^r\) with a positive weighted bias above about \(0.4\%\).

Thus the first resonance has been reduced from a \(10^{11}\)-step parity-word problem to a **weighted transversality/correlation problem between two deterministic codings**:

\[
\boxed{
\text{Farey/Sturmian alternating code}
\quad\text{vs}\quad
\text{3-adic Hensel carry code}.
}
\]

## 6. DSD audit interpretation

The DSD contribution here is the reorganization of previously separate descriptors:

- mechanical position,
- correction cost,
- terminal Hensel carry,
- terminal defect support.

After the reorganization the proof chain is

\[
\boxed{
\text{Farey residue }r
\to
\text{mechanical sign }(-1)^r
\to
\text{Hensel sign comparison}
\to
\text{forced displacement}
\to
\text{correction budget}.
}
\]

Every arrow is an ordinary arithmetic statement. DSD is therefore methodological here, not an extra truth assumption.

## 7. Next target

The next proof-level task is to derive a structural recurrence for the permuted Hensel signs and show that their weighted correlation with the alternating kernel cannot sustain the required positive bias.

A useful non-circular state is the mechanical-scaled Hensel carry. If \(K_m\) denotes the higher ternary carry and \(B_m\) the earliest mechanical position, define

\[
X_m:=2^{A-B_m}K_m.
\]

Then a lift with mechanical gap \(g\in\{1,2\}\) and displacement d satisfies

\[
\boxed{
X_{m+1}=\frac{2^gX_m+2^{-d}}{3}.
}
\]

Unlike scaling by the actual earliest position, this state retains the mechanical defect and does not simply reproduce the ordinary backward Collatz map. The next audit should determine whether this recurrence admits a bounded-discrepancy/correlation theorem strong enough to beat the \(0.4\%\) threshold.

Companion certificate:

`collatz/src/first_resonance_farey_alternating_kernel_certificate.py`.
