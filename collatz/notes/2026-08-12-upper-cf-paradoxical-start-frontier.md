# Upper-CF renewal frontier from the paradoxical-start lower bound

Date: 2026-08-12

Status: **finite elimination bridge using an external published/preprint computational theorem plus the exact upper-CF renewal ceiling**. This is not an asymptotic proof.

## 1. External paradoxical-start result

Rozier and Terracol, *Paradoxical behavior in Collatz sequences* (arXiv:2502.00948; Discrete Mathematics 2026), Theorem 1.3, report:

- exactly 593 paradoxical sequences begin with an integer `<=4614`;
- if there are any additional paradoxical sequences, their first term must exceed

\[
\boxed{2.8\times10^{19}}.
\]

Their theorem combines direct computation with previously published large-scale Collatz verification data. It is a finite computational theorem, not a proof that no larger paradoxical sequence exists.

## 2. Why an upper-CF renewal is paradoxical

A primitive upper-CF renewal segment has

\[
\frac{3^H}{2^A}<1
\]

but sends a renewal floor `N` to a strictly larger next floor

\[
N'=N+g>N.
\]

Hence it is an acyclic paradoxical sequence in the sense of Rozier–Terracol.

For sufficiently large `A`, the coefficient-survivor frontier already forces `N>4614`, so the external theorem implies

\[
\boxed{N>2.8\times10^{19}.}
\]

## 3. Internal exact upper-CF ceiling

The first-crossing correction theorem gives

\[
\boxed{
N<\frac{H3^{H-1}}{2^A-3^H}
=\frac{H}{3(P-1)},
\qquad P=\frac{2^A}{3^H}>1.
}
\]

Therefore an upper convergent is eliminated whenever its renewal ceiling lies below `2.8e19`.

## 4. Eliminated upper convergents

The upper convergents of `log_2 3` relevant after the previously audited range include

\[
(A,H)=(301994,190537),
\]

\[
(A,H)=(17087915,10781274),
\]

\[
(A,H)=(272500658,171928773),
\]

and

\[
(A,H)=(630138897,397573379).
\]

Their renewal ceilings are approximately

\[
9.85\times10^{11},
\]

\[
2.94\times10^{14},
\]

\[
3.20\times10^{16},
\]

and

\[
1.25\times10^{18},
\]

respectively.

Each is safely below

\[
2.8\times10^{19}.
\]

Combined with the already established small-start coefficient-frontier exclusions, this yields

\[
\boxed{
\text{no primitive upper-CF renewal can occur for an upper convergent with }
A\le630{,}138{,}897.
}
\]

## 5. First unresolved upper convergent under this bridge

The next upper convergent is

\[
\boxed{
(A,H)=(10{,}439{,}860{,}591,\ 6{,}586{,}818{,}670).
}
\]

Its renewal ceiling is approximately

\[
\boxed{2.17\times10^{20},}
\]

which is larger than the external paradoxical-start lower bound `2.8e19`.

Thus the Rozier–Terracol finite theorem no longer decides this convergent.

## 6. Meaning of the frontier

The gain is not an asymptotic Collatz result. It identifies a very large exact/finite exclusion frontier produced by two independent mechanisms:

1. **internal structure:** first coefficient crossing at a renewal floor forces a small ordinary start;
2. **external computation:** acyclic paradoxical starts in a vast finite interval have already been excluded.

Beyond `A=630,138,897`, the proof must again use structural arithmetic rather than simply extending a finite verification window.

The next asymptotic target remains the tri-place defect / small-formation-residue problem for primitive upper-CF renewals.
