# A0 s=1: position-form ballot theorem and modular prefix decoder

Date: 2026-08-28

Status: **SAFE equivalence / SAFE local decoder / SAFE cardinality pruning / OPEN full bridge.**

This note continues Route B after the ten-block Christoffel threshold compression.
It changes the computational target: an exact correction-language membership
query does not require enumerating the correction language, because the fixed-
`(t,j)` correction map is injective.

## 1. Prefix ballot is exactly a coordinate condition

Let

\[
\alpha=\log_3 2
\]

and let a length-\(h\) parity word have odd positions

\[
0\le a_1<a_2<\cdots<a_q<h.
\]

Write \(Q(n)\) for the number of odd symbols among positions
\(0,\ldots,n-1\).  The pure lower-ballot condition is

\[
Q(n)\ge \lceil \alpha n\rceil
\qquad(0\le n\le h).
\]

The \(r\)-th odd event of the threshold word occurs at

\[
d_r=\left\lfloor\frac{r-1}{\alpha}\right\rfloor.
\]

Therefore

\[
\boxed{
Q(n)\ge\lceil\alpha n\rceil\ \forall n
\iff
a_r\le d_r\ \forall r.
}
\]

The forward direction follows because by prefix \(d_r+1\) the threshold
already contains \(r\) odd events.  The reverse direction follows because
every actual \(r\)-th odd event occurs no later than the corresponding
threshold event.

Since \(a_r\) is an integer,

\[
a_r\le\left\lfloor\frac{r-1}{\alpha}\right\rfloor
\iff
\alpha a_r\le r-1.
\]

Using \(\alpha=\ln2/\ln3\),

\[
\boxed{
2^{a_r}\le3^{r-1}.
}
\]

Hence the full pure-ballot prefix family is equivalently tested by the
coordinate inequalities

\[
\boxed{
2^{a_r}\le3^{r-1}
\quad\text{for every decoded odd position }a_r,
}
\]

together with the terminal count condition

\[
q\ge\lceil\alpha h\rceil.
\]

No scan of all \(h\) prefixes is mathematically necessary once the odd
positions are known.

## 2. Consequence for the correction-language program

At fixed \((t,j)\),

\[
C=\sum_{r=1}^{j}3^{j-r}2^{a_r}
\]

is injective in the ordered odd positions.  The valuation decoder is

\[
a_r=v_2(R_{r-1}),
\qquad
R_r=R_{r-1}-3^{j-r}2^{a_r}.
\]

Therefore a required correction has **at most one** candidate parity word.

The pure-ballot membership problem is not

\[
\text{enumerate every ballot correction and search for }C_{\rm req}.
\]

It is instead

\[
\boxed{
C_{\rm req}
\longrightarrow
\text{unique valuation decode}
\longrightarrow
\{a_r\}
\longrightarrow
2^{a_r}\le3^{r-1}.
}
\]

Additional `C4F` formation predicates are then checked on that same unique
candidate.  They are not removed by this theorem.

## 3. Shallow decoding does not need the endpoint Z

For the A0 s=1 bridge,

\[
2^{t_0}Z=3^{j_0}X+C_{\rm req}.
\]

For every \(h\le t_0\), reduction modulo \(2^h\) gives

\[
\boxed{
C_{\rm req}\equiv-3^{j_0}X\pmod{2^h}.
}
\]

Thus every decoded odd position \(a_r<h\) can be recovered from

\[
X\bmod2^h
\]

alone.  Neither the giant integer \(C_{\rm req}\) nor \(Z\) is needed.

The modular decoder starts with

\[
R_0=(-3^{j_0}X)\bmod2^h
\]

and repeatedly performs

\[
a_r=v_2(R_{r-1}),
\]

\[
R_r=
\left(
R_{r-1}-3^{j_0-r}2^{a_r}
\right)\bmod2^h.
\]

Terms with \(a_r\ge h\) vanish modulo \(2^h\), so the process terminates
exactly after recovering all odd positions below \(h\).

This gives an exact target-aware shallow oracle:

\[
\boxed{
X
\mapsto
\{a_r<h\}
\mapsto
\text{ballot pass/fail}.
}
\]

## 4. Immediate residue consequence

At depths 1 and 2,

\[
\lceil\alpha\rceil=1,
\qquad
\lceil2\alpha\rceil=2.
\]

Hence every admissible pure-ballot bridge begins

\[
\boxed{11}.
\]

For the accelerated Collatz parity address this is exactly

\[
\boxed{
X\equiv3\pmod4.
}
\]

This is a deterministic necessary congruence, not a heuristic.

## 5. Exact 72-prefix cardinality

Because a length-\(h\) parity word determines a unique start residue modulo
\(2^h\), the number of start residues passing the first \(72\) pure-ballot
constraints equals the number of valid length-72 ballot words.

An exact dynamic program, using

\[
\lceil n\log_3 2\rceil
=
\min\{k:3^k>2^n\},
\]

finds

\[
\boxed{
N_{72}=4\,650\,657\,914\,809\,371\,340.
}
\]

Relative to all \(2^{72}\) residues this is

\[
\boxed{
0.098481512006313\%.
}
\]

The strict physical shell

\[
2^{71}<X<2^{72}
\]

contains exactly

\[
2^{71}-1
\]

integers.  Without making any assumption about how the accepted residues
are distributed inside that shell, its intersection can contain no more
than \(N_{72}\) candidates.  Therefore

\[
\boxed{
\frac{\#\{\text{shell candidates passing 72-prefix ballot}\}}
     {2^{71}-1}
\le
0.196963024012626\%.
}
\]

This is a cardinality upper bound.  It is **not** a claim that the accepted
residues are uniformly distributed, and it must not be multiplied by the
independent physical-\(X\) interval fraction as if the filters were
statistically independent.

## 6. DSD audit

### SAFE

- prefix ballot \(\iff\) odd-position coordinate bounds;
- coordinate bounds \(\iff 2^{a_r}\le3^{r-1}\);
- fixed-\((t,j)\) correction injectivity;
- shallow modular decoder from \(X\) alone;
- forced prefix `11` and \(X\equiv3\pmod4\);
- exact 72-prefix ballot-word count;
- at-most `0.196963024012626%` cardinality of the strict physical shell
  surviving the 72-prefix pure-ballot condition.

### REJECTED

- enumerating the full \(10^{11}\)-step ballot correction language merely
  to answer a single target membership query;
- treating the cardinality ratio as a probability;
- multiplying independent-looking pruning percentages without an
  independence proof;
- claiming that a pure-ballot pass automatically satisfies `C4F`;
- claiming same-orbit closure from the shallow prefix oracle.

### OPEN

The unique candidate must still be checked through the complete depth
\(t_0\), including all additional formation conditions.

The remaining computational obstruction is therefore no longer
"represent every correction in the language".  It is

\[
\boxed{
\text{compress the unique target-aware valuation decode far beyond the
72-bit shallow window.}
}
\]

A valid next compression must preserve exact valuations and the decoded
rank \(r\); interval or residue-set merging that can change a future
valuation is forbidden.

## 7. Next gate: block-jump decoder

The next construction should seek a block transfer that maps a symbolic
remainder state

\[
(r,R\bmod2^H)
\]

through many decoded odd events at once, while certifying the same output
positions that repeated one-atom valuation decoding would produce.

The previously certified Christoffel/Stern-Brocot DAG is useful here as a
boundary and transfer skeleton, but the new injectivity result means there
is no need to build a DAG containing **all** interior ballot deviations.
Only the unique target path has to be preserved.

## Companion certificates

- `collatz/src/A0_s1_ballot_position_decoder_certificate.py`
- `collatz/src/A0_s1_modular_prefix_decoder_certificate.py`
- `collatz/src/A0_s1_correction_language_injective_decoder_certificate.py`
- `collatz/src/A0_s1_threshold_tenblock_certificate.py`
- `collatz/src/A0_s1_christoffel_correction_dag_certificate.py`
