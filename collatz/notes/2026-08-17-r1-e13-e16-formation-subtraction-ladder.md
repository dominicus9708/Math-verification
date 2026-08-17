# R1 E=13--16 formation-subtraction ladder

Date: 2026-08-17

Status: **exact current-R1 finite formation certificates through total pre-G13 even count E=16**. The four consecutive layers E=13,14,15,16 are empty in the present isolated R1 core. Consequently

\[
\boxed{e_{1539}\ge17}
\]

and the G13 entrance obeys

\[
\boxed{x_{1539}<2^{946}}.
\]

This is not a global proof of Collatz.

## 1. Why this is a change of proof object

The former direct route to E=13 would have enumerated the first-73 nine-zero layer of size

\[
\binom{73}{9}=97,082,021,465.
\]

That route was abandoned. The successful route instead composes three formation constraints:

1. a first-73 dyadic parity/end-point class;
2. a future odd-run divisibility condition forced by the remaining even-event budget;
3. a finite ternary digit automaton for the first-73 affine correction.

The proof object is therefore an intersection of address classes, not a list of ordinary starting integers.

## 2. E=13

Existing first-73 certificates remove every layer with at most eight evens. Run-cover gives at most nine first-73 evens for total E=13, so an unresolved member would have exactly nine.

The tenth even event satisfies p_9>=164. Hence positions 73..163 are 91 consecutive odd steps and

\[
2^{91}\mid U_{73}.
\]

Writing U_73=2^91 v confines the scale to

\[
579\le v\le867.
\]

The normalized nine-rank ternary formation automaton leaves only v=591 through K=20 and none at K=21. Thus E=13 is empty.

## 3. E=14

Run-cover leaves only e_73=9 or 10.

* e_73=10 forces 93 consecutive post-73 odd steps; the scale interval is v=49..72 and the ten-rank formation automaton is empty by K=16.
* e_73=9 gives exactly 94 possible U_73 residues modulo 2^93. Their numerical intersection contains 6,797 endpoint values, all rejected by the nine-rank ternary formation automaton by K=24.

Thus E=14 is empty.

## 4. E=15

The necessary event vector is

\[
[0,1,2,3,4,5,6,7,8,9,71,168,321,561,940].
\]

Only e_73 in {9,10,11} remains. Since rank 11 cannot occur before position 168, the 95-step window 73..167 has at most 11-e_73 evens. The dyadic window is compressed to 4,561 / 96 / 1 residues, whose numerical endpoint intersections are 82,436 / 578 / 2 states. Ternary formation eliminates the three layers by K=27,24,15 respectively.

Thus E=15 is empty.

## 5. E=16

The exact necessary event vector is

\[
[0,1,2,3,4,5,6,7,8,9,12,74,171,323,563,941].
\]

Again only e_73 in {9,10,11} remains. Rank 12 cannot occur before position 171, so the 98-step window 73..170 contains at most 12-e_73 evens.

The resulting U_73 residue counts modulo 2^98 are

\[
156,948,\quad4,852,\quad99,
\]

and their exact numerical endpoint intersections contain

\[
354,821,\quad3,701,\quad33
\]

states.

The same ternary formation automaton gives

\[
\begin{array}{c|c}
e_{73}&\text{last nonzero checkpoint}\quad\to\quad0\\\hline
9&K=27:5\to K=30:0\\
10&K=24:1\to K=27:0\\
11&K=15:2\to K=18:0
\end{array}
\]

Therefore E=16 is empty and

\[
\boxed{e_{1539}\ge17}.
\]

## 6. G13 entrance consequence

The exact relaxed endpoint maxima give floor(log2 U_max)=945 at E=17 and smaller values thereafter. Thus

\[
\boxed{x_{1539}<2^{946}}.
\]

Since

\[
946=49\cdot19+15,
\]

the natural G13 lift chunks obey

\[
\boxed{t_{49}<2^{15},\qquad t_b=0\ (b\ge50)}.
\]

The number of forced high zero address bits is

\[
\boxed{20026-946=19080}.
\]

## 7. Next structural frontier: E=17

The exact necessary even-position vector is

\[
\boxed{[0,1,2,3,4,5,6,7,8,9,10,14,76,173,325,564,942]}.
\]

The first-73 layer is still restricted to e_73 in {9,10,11,12}. A direct length-100 sparse-window list would already introduce roughly four million raw dyadic words in the e_73=9 subcase. That is still finite, but it is no longer the preferred proof object.

The next target is therefore a composed **window-formation transfer automaton** that carries only

\[
(\text{window even budget},\ \text{dyadic endpoint address},\ \text{ternary formation carry})
\]

and subtracts impossible classes before the complete 100-bit sparse word is formed.

This preserves the intended formation/composition proof architecture instead of restarting blind sparse-word enumeration.

## Reproducibility

- `collatz/src/r1_e13_73plus91_formation_obstruction.py`
- `collatz/src/r1_e14_73_future_formation_obstruction.py`
- `collatz/src/r1_e15_73_window_formation_obstruction.py`
- `collatz/src/r1_e16_73_window_formation_obstruction.py`
- `collatz/src/r1_g13_entry_e17_946bit_upgrade_certificate.py`
