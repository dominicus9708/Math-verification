# Constructive Euclidean predecessor-credit growth through length 24,727

Date: 2026-08-13

Status: **exact finite transducer certificate / constructive lower bounds**.  The calculation propagates only integer correction-credit states through neutral U6/U7 base-block transducers.  It does not enumerate the internal parity words of the large return words.  The reported credits are exact witnessed lower bounds, not global maxima.  This is not a proof of Collatz.

## 1. Base neutral transducers

Use the certified neutral blocks

\[
U_6=1010110110101101101,
\qquad (L,Q)=(19,12),
\]

and

\[
U_7=011011011010110110101101101,
\qquad (L,Q)=(27,17).
\]

For a neutral block `B`, an incoming integer collision quotient `D` is sent to

\[
\boxed{
D'
=
\frac{R_h-R_l+2^{L_B}D}{3^{Q_B}}
}
\]

whenever the numerator is divisible by \(3^{Q_B}\).

The U6 and U7 difference-full certificates prove that at least one successor exists for every integer input `D`.

For this finite constructive calculation, the verifier chooses the **largest exact successor available inside the enumerated neutral base fibre** at every U6/U7 step.  Thus composition of these choices produces one explicit valid correction-collision path through every larger return word.

## 2. Return-word composition used by the transducer

The physical return words are represented recursively by

\[
U_9=U_7U_6U_6,
\]

\[
U_{10}=U_6U_9,
\]

\[
U_{15}=U_9U_{10}^5,
\]

\[
U_{17}=U_{10}U_{15}^2.
\]

The partial quotient `23` then gives the semiconvergent chain

\[
\boxed{
V_t=U_{15}U_{17}^t,
\qquad1\le t\le23.
}
\]

Its time lengths are

\[
\boxed{
|V_t|=485+1054t.
}
\]

At `t=23`,

\[
|V_{23}|=24,727.
\]

This is the same continued-fraction scale at which the first-crossing mechanical envelope earlier produced a record resonance.

## 3. Initial credit

Previous exact triangular-collision work gives a fixed one-slack predecessor credit

\[
\boxed{D_0=162}
\]

at the length-1054 return word `U17`.

The present calculation starts from this already certified state and transports it through the neutral Euclidean hierarchy.

## 4. Exact constructive credits along the coefficient-23 chain

The exact transducer gives the following witnessed credits:

\[
\boxed{
\begin{array}{r|r|r}
t&|V_t|&\Delta\text{ lower bound}\\\hline
1&1,539&226\\
2&2,593&382\\
3&3,647&526\\
4&4,701&665\\
5&5,755&801\\
6&6,809&937\\
7&7,863&1,086\\
8&8,917&1,222\\
9&9,971&1,358\\
10&11,025&1,500\\
11&12,079&1,641\\
12&13,133&1,777\\
13&14,187&1,917\\
14&15,241&2,073\\
15&16,295&2,213\\
16&17,349&2,362\\
17&18,403&2,500\\
18&19,457&2,646\\
19&20,511&2,782\\
20&21,565&2,932\\
21&22,619&3,075\\
22&23,673&3,220\\
23&24,727&3,377
\end{array}
}
\]

Every number in the last column is the output of an exact chain of divisibility identities in the neutral correction transducer.  No statistical inference is used.

In particular, the length-24,727 one-slack fibre contains a correction-collision pair with

\[
\boxed{
R_h-R_l=3,377\cdot3^q
}
\]

for its common total odd count `q`.

Therefore a low-correction orientation in that pair, when it occurs at an orbit state `x` of a hypothetical minimal counterexample with minimum `N`, requires

\[
\boxed{x-N\ge3,377}
\]

for minimality.

## 5. Why this is not flat enumeration

The verifier never forms a `2^24727` parity set, nor even the full set of orientations in any large macroblock.

Only the two base neutral fibres are enumerated once:

- U6 neutral orientations;
- U7 neutral orientations.

For each integer input `D`, their exact correction residues determine the best available successor and the result is memoized.  The large continued-fraction word is then evaluated as an ordinary composition of these cached maps.

Thus the state complexity is controlled by the number of distinct integer quotient values actually visited, not by the length of the represented parity word.

This is the intended transition from individual-number/word computation to a structural finite-state aggregation.

## 6. Interpretation of the finite growth

The constructive lower bound increases from

\[
162\quad\text{at }L=1,054
\]

to

\[
\boxed{3,377\quad\text{at }L=24,727}
\]

while the required incoming survival slack remains one.

The finite ratio

\[
3377/24727\approx0.1366
\]

should **not** be extrapolated as an asymptotic linear law.  The calculation proves only existence of this finite sequence of increasing credits.

Its proof-program value is different: the Euclidean hierarchy can carry and amplify integer predecessor credits across four orders of magnitude in represented word length without expanding the state space into individual parity words.

## 7. Remaining coverage problem

An available large credit does not yet eliminate every critical R2 orientation.

The missing theorem is still a coverage statement of the form:

> every sufficiently long aperiodic critical-survivor orientation must either lie in a correction-collision class with credit exceeding its available orbit headroom, or make some other well-founded progress that cannot repeat indefinitely.

The current result proves that large credits exist abundantly enough to be transported structurally; it does not prove that an arbitrary actual candidate orientation is forced to use one.

## 8. Verification

`collatz/src/euclidean_credit_greedy_to_24727_certificate.cpp`:

1. enumerates the exact neutral U6/U7 base fibres;
2. evaluates exact integer divisibility transitions;
3. memoizes the base transducer on visited `D` states;
4. asserts every one of the 23 displayed credits;
5. terminates at the exact length 24,727 with credit lower bound 3,377.

The choice of the largest available base successor is only an optimization heuristic for finding a strong witness; the validity of each resulting transition is exact.
