# A0/J0 activation ladder and negative macro budget

Date: 2026-08-27

Status: **SAFE LEMMA + exact rational/Worley-Dujella certificate inside the repaired finite-crossing branch.** No ternary Cantor-core entry and no repeated-local pullback is used. This is not a proof of the Collatz conjecture.

## 1. Starting promoted strip

Write

\[
G=2^{33}.
\]

After two consecutive `J0/R0` debits, the repaired branch has a future endpoint

\[
X=N+d,
\qquad N>2^{71},
\qquad 0\le d<2G.
\]

The promoted first possible coefficient-subcritical scale is

\[
(A_0,Q_0)
=(114208327604,72057431991).
\]

For every genuine first crossing at this pair, the mechanical first-crossing envelope gives a uniform gap-credit bound

\[
\boxed{
 d'-d<a_A,
\qquad
a_A<0.5023G.
}
\]

The exact certificate gives the sharper value

\[
a_A/G\approx0.50220738937.
\]

## 2. Two A0 returns reach only a 3.005G strip

If two consecutive local first crossings both occur at `A0/Q0`, then

\[
d_2<2G+2a_A<3.005G.
\]

The question is then: which coefficient-subcritical pair can occur next before another `A0` depth?

At this enlarged gap the near-survival inequality gives a Worley-Dujella constant

\[
K<2.195,
\]

hence

\[
rs<2K<4.39.
\]

Thus only the finite adjacent-convergent family with integral

\[
rs\le4
\]

can contain a subcritical pair below `A0`.

The exact certificate enumerates 28 primitive lower-side candidates.  For each candidate it checks every allowed positive multiple below `A0`, using concavity of the exact lower deficit minus the linear gap allowance.

All are excluded except one:

\[
\boxed{
(J_0,R_0)
=(10439860591,6586818670).
}
\]

Even the multiples

\[
2(J_0,R_0),\ldots,10(J_0,R_0)
\]

are still excluded at this stage.

Therefore, after two consecutive promoted `A0` returns, the finite-crossing branch has the exact trichotomy:

1. the next first coefficient crossing before `A0` is exactly `J0/R0`;
2. no crossing occurs before `A0`, and the next crossing is again `A0/Q0`;
3. the coefficient survives through `A0`, entering the later/infinite-survivor gate.

There is no fourth sub-`A0` resonance hidden between these cases.

## 3. A0,A0,J0 is strongly gap-negative

For a genuine `J0/R0` first crossing, the previous exact local wall gives a uniform debit

\[
\boxed{
 d-d'>a_J,
\qquad
a_J>2.527G.
}
\]

Hence

\[
2a_A-a_J
<2(0.5023G)-2.527G
<-1.522G.
\]

Starting from `d<2G`, an actual macro

\[
A_0\to A_0\to J_0
\]

therefore satisfies

\[
\boxed{
 d_{\rm out}<0.478G.
}
\]

The exact certificate gives

\[
d_{\rm out}/G<0.477394.
\]

Thus the first opportunity for the lower resonance to re-enter does not merely stop gap growth.  If it is actually taken, it nearly resets the endpoint to the root strip.

## 4. One J0 debit dominates five A0 credits

The exact constants satisfy

\[
\boxed{
5a_A<a_J.
}
\]

More quantitatively,

\[
a_J-5a_A>0.015G.
\]

Therefore any segment made only of these two certified transition types and containing at most five `A0` crossings per `J0` crossing has strictly negative gap drift.

This is a deterministic weighted-budget statement, not a density heuristic.

The only way an `A0/J0` transition language can avoid this immediate negative drift is to become **A0-dominant**, with more than five `A0` returns per primitive `J0` debit on average, or to escape into a different/later coefficient-survival scale.

## 5. Multiplicity ladder below A0

Because

\[
10J_0<A_0<11J_0,
\]

the only positive multiples of the `J0` denominator that can occur before `A0` are

\[
mJ_0,
\qquad1\le m\le10.
\]

For the first crossing pair

\[
(mJ_0,mR_0),
\]

the exact generic correction bound yields a debit

\[
D_m
>
2.526mG
\qquad(1\le m\le10).
\]

Consequently

\[
\boxed{
5m\,a_A<D_m
}
\]

for every multiplicity in the entire pre-`A0` range.

Starting from `d<2G`, an `A0`-only run has the envelope

\[
d_k<2G+k a_A.
\]

The certificate compares this with each exact `D_m` and finds the first index at which the multiple can cease to be automatically forbidden:

\[
\boxed{
 k_m=5m-3.
}
\]

Thus the activation ladder is

\[
\begin{array}{c|cccccccccc}
m&1&2&3&4&5&6&7&8&9&10\\
\hline
k_m&2&7&12&17&22&27&32&37&42&47
\end{array}
\]

Interpretation:

- primitive `J0` cannot re-enter before two promoted `A0` returns;
- `2J0` cannot re-enter before seven `A0` returns;
- `3J0` cannot re-enter before twelve `A0` returns;
- and so on, with an exact five-return spacing between successive multiplicity scales.

This is the first explicit finite **resonance activation ladder** produced by the gap-budget variable.

## 6. DSD state compression

The relevant state is now naturally

\[
\boxed{
(\text{current gap band},\text{active resonance multiplicities})
}
\]

rather than an unrestricted parity word.

The formation of a new resonance scale is controlled by a quantitative threshold:

\[
\text{gap credit accumulation}
\longrightarrow
\text{activation threshold}
\longrightarrow
\text{available CF resonance}
\longrightarrow
\text{gap debit if used}.
\]

The activation spacing and debit/credit weights agree numerically in the decisive direction:

\[
5a_A<a_J.
\]

So the arithmetic scale needed to activate a lower resonance costs slightly more gap than five promoted `A0` blocks can replenish.

## 7. What is and is not closed

### SAFE

- two `A0` returns from `d<2G` imply `d<3.005G`;
- below `A0`, the only nonexcluded first-crossing pair at that point is the primitive `J0/R0`;
- `A0,A0,J0` forces the gap below `0.478G`;
- one primitive `J0` debit dominates five `A0` credits;
- for every `1<=m<=10`, `mJ0` debit dominates `5m` `A0` credits;
- the exact activation indices are `k_m=5m-3`.

### OPEN

- a trajectory may coefficient-survive the activated `J0` scale instead of using it;
- it may also survive through `A0` and enter a later/infinite coefficient-survivor regime;
- therefore the activation ladder is not yet a global termination theorem.

The next proof target is consequently sharper than before:

> control an A0-dominant run that repeatedly survives every activated `mJ0` gate, or prove that such repeated survival necessarily enters the already isolated infinite coefficient-survivor/naturalness branch.

Companion certificate:

`collatz/src/A0_J0_activation_ladder_certificate.py`
