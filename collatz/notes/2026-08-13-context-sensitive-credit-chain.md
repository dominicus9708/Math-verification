# Context-sensitive Euclidean predecessor-credit chain

Date: 2026-08-13

Status: **exact correction arithmetic on a finite set of identified Sturmian/Euclidean factor contexts; context discovery is a finite diagnostic, not yet an asymptotic substitution theorem**. This does not prove Collatz.

## 1. Why block phase must be retained

The same length and mechanical odd count do not determine predecessor-credit behavior. Different conjugate/phase types have different correction-position geometry.

At length 46, the two concatenation types built from the certified length-19 and length-27 macroblocks behave differently:

- `U27 U19`: strongest newly generated cross-credit in the tested `(0,-1)` split is `17`, below the inherited credit `19`;
- `U19 U27`: an exact cross-collision gives credit `22`.

Therefore the renormalized state must retain the return-word type/phase in addition to `(Sigma,M,q)` and the 3-adic correction state.

## 2. Exact level-46 collision

For the favorable length-46 type `U19 U27`, two one-slack orientations have corrections

\[
R_1=73,753,304,060,593,
\]

\[
R_2=577,042,738,069,735,
\]

with

\[
R_2-R_1=22\cdot3^{28}.
\]

Thus the scalar right-block credit is

\[
\boxed{\delta_{46}=22.}
\]

## 3. Actual left context to length 73

A length-27 neutral factor can precede this length-46 type in the investigated Sturmian factor context. Applying the exact cross-block congruence

\[
D_U+2^{27}\delta_{46}\equiv0\pmod{3^{17}}
\]

gives

\[
\boxed{\delta_{73}=28.}
\]

Only the neutral length-27 correction classes are searched; the length-46 interior is represented solely by the certified scalar credit `22`.

## 4. Actual length-19 context to length 92

The identified immediate left length-19 context of the investigated length-73 factor is

\[
\boxed{A_{19}=0110110110101101101.}
\]

It has mechanical odd count `12`. Using its neutral correction classes with incoming credit `28` gives

\[
\boxed{\delta_{92}=30.}
\]

Thus along this concrete context chain the certified credits are

\[
\boxed{22\to28\to30.}
\]

## 5. Two predecessor context types at the next extension

For the investigated length-92 factor, finite Sturmian-factor diagnosis finds two possible immediate length-19 predecessor types:

\[
A_{19}=0110110110101101101,
\]

\[
B_{19}=1010110110101101101.
\]

Exact correction arithmetic for incoming credit `30` gives

\[
\boxed{\mathcal A_{A_{19}}(30)=33,}
\]

\[
\boxed{\mathcal A_{B_{19}}(30)=32.}
\]

Hence on the two identified predecessor contexts,

\[
\boxed{\delta_{\rm next}\ge32>30.}
\]

This is the first finite context set in the current calculation for which every identified immediate predecessor type amplifies the incoming credit.

## 6. Repetition obstruction

The length-27 factor satisfies a strict finite repetition constraint in the diagnosed Sturmian language:

\[
U_{27}^2\text{ occurs,}
\qquad
U_{27}^3\text{ does not.}
\]

Moreover the particular context `U27^2 U46` needed to freely iterate the map `22 -> 28 -> 33` is not an allowed factor in the finite diagnosis.

Therefore the local amplification map cannot be iterated independently of the return-word substitution. This prevents an invalid proof by free concatenation.

## 7. Revised renormalized state

The exact state required for further work is therefore at least

\[
\boxed{
(\text{return-word type},\Sigma,M,q,\text{3-adic correction carry},\Delta).
}
\]

The next target is a finite substitution automaton on return-word types whose edges carry certified credit-amplification lower bounds.

If every sufficiently long path in that substitution automaton has positive accumulated credit drift, and critical-return headroom can be bounded below that drift, the aperiodic R2 branch would acquire a genuine well-founded obstruction.

The present finite chain establishes only the local arithmetic ingredients, not that global theorem.