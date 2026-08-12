# `q<=8` repeated backtrace refinement of the `m=44` window bound

Date: 2026-08-12

Status: **exact finite local-minimality refinement** of `2026-08-12-repeated-backtrace-local-minimality-filter.md`. Contracting back-tracing endpoint classes through odd-depth eight are inserted repeatedly at every zero-defect endpoint in the length-47 skew-window automaton. The resulting universal defect floor rises to `19.1825%` at the current `m=44` R1 resonance. This does not close the block.

## 1. Local contracting classes

For an odd-to-odd exponent code of odd-depth `q` and total binary exponent `K`, the ancestor/endpoint multiplier is

\[
\lambda=\frac{2^K}{3^q}.
\]

For each `q<=8`, retain every code satisfying

\[
\boxed{2^{K+1}<3^q,}
\]

so `lambda<1/2`.

At the current `m=44` floor, every zero-defect state obeys

\[
y<2\left(N+\frac H3\right),
\qquad N>V_0=4\cdot3^{44}+2.
\]

The largest retained multiplier for `q<=8` occurs at `q=7`, `K=10`:

\[
\lambda_{\max}=\frac{1024}{2187}<\frac12.
\]

Since the present floor is enormously larger than `H`, the additive correction margin is harmless and every retained class gives a positive ancestor strictly smaller than `N` whenever the zero-defect endpoint lies in its unique `3^q` admissibility class.

## 2. Number of contracting endpoint residues

The exact residue-set cardinalities through depth eight are

\[
\boxed{
\begin{array}{c|rrrrrrrr}
q&1&2&3&4&5&6&7&8\\\hline
|B_q|&0&1&1&5&6&22&85&121
\end{array}
}
\]

where `B_q` is the set of endpoint residues modulo `3^q` admitting at least one retained contracting exponent code.

The `q<=4` rule simplifies to

\[
y\not\equiv8\pmod9,
\qquad
y\not\equiv20,40\pmod{81}
\]

at every zero-defect endpoint.

At `q=6`, after removing classes already caught at smaller depth, five genuinely new residue classes modulo `729` are

\[
\boxed{91,137,319,479,661\pmod{729}.}
\]

The higher-depth automaton uses the full exact residue sets rather than only these displayed representatives.

## 3. Safe low-cost truncation

The overlapping-window incidence optimization fills local defect levels in increasing `j`. At the current threshold it reaches only the low-cost levels near `j=15`.

Therefore the local DP may discard every state with

\[
j>18
\]

without changing any capacity needed by the threshold calculation.

This is a safe truncation, not a heuristic approximation: high-`j` capacities can only be used after every lower-cost capacity is exhausted, while the final greedy optimum is already attained below the retained cutoff.

## 4. Filtered length-47 capacities for q<=8

The length-47 critical language has 48 factors. The DP state is

\[
(h,j,z),
\]

with `z` kept modulo `3^8=6561` and updated by

\[
z'=(3z+1)2^{-v}\pmod{3^8}.
\]

At each zero-defect endpoint, reduction of `z` modulo `3^q` is tested against `B_q` for every `q<=8` for which enough local odd steps have elapsed.

The exact low-cost capacities are

\[
\boxed{
\begin{array}{c|r}
j&C_j\\\hline
0&48\\
1&925\\
2&8,833\\
3&56,438\\
4&276,884\\
5&1,138,178\\
6&4,162,857\\
7&14,079,091\\
8&45,011,466\\
9&137,702,866\\
10&406,050,905\\
11&1,159,424,199\\
12&3,216,270,783\\
13&8,691,294,858\\
14&22,933,288,465\\
15&59,203,841,562\\
16&149,769,375,744\\
17&371,723,912,261\\
18&906,090,977,987
\end{array}
}
\]

The cumulative capacity through `j=14` is

\[
\boxed{36,608,766,796.}
\]

## 5. Exact global threshold

As before, at least

\[
E=H-47-2r_*
\]

length-47 windows have zero endpoints, while their total internal defect incidence is at most

\[
46r_*.
\]

Let `Phi(E)` be the greedy minimum incidence cost using the filtered capacities above. Then

\[
\Phi(H-47-2r_*)\le46r_*
\]

is necessary.

Exact integer evaluation gives

\[
\boxed{r_*\ge26,381,334,316.}
\]

At the previous integer,

\[
E=84,765,376,635,
\]

\[
\Phi(E)=1,213,541,378,516
>
1,213,541,378,490
=46(26,381,334,315).
\]

At the threshold,

\[
E=84,765,376,633,
\]

\[
\Phi(E)=1,213,541,378,486
<
1,213,541,378,536
=46(26,381,334,316).
\]

Therefore

\[
\boxed{
\frac{r_*}{H}
>0.19182512378584718.
}
\]

So more than

\[
\boxed{19.1825\%}
\]

of all odd-event coordinates must depart from the critical mechanical cap.

An independent Wolfram exact-integer calculation reproduces the two threshold inequalities above.

## 6. Progression of the local-minimality hierarchy

The branch-specific defect floors now read approximately

\[
\begin{array}{c|c}
\text{filter}&r_*/H\\\hline
\text{transition only}&16.3833\%\\
q\le4\text{ backtrace classes}&18.5090\%\\
q\le6\text{ backtrace classes}&18.8429\%\\
q\le8\text{ backtrace classes}&19.1825\%
\end{array}
\]

Thus adding exact short predecessor obstructions monotonically shrinks the local language.

## 7. Interpretation and limit

This is much closer to the intended non-enumerative proof style than terminal case scans: a finite family of propositions removes entire local factor classes everywhere along the hypothetical orbit.

However, the real correction allowance at the low end of the `m=44` block is still too large for a `19.18%` defect floor to yield a contradiction by correction mass alone.

The next useful channel should therefore not be merely `q=9,10,...` residue refinement. A stronger step is to add a **forward minimality condition** to the same local automaton: a minimal counterexample may neither admit a smaller back-tracing merge nor have a forward iterate below `N`. This turns the present repeated predecessor filter into a two-sided local-minimum filter.
