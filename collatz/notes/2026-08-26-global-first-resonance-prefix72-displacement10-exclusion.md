# First global resonance: exact exclusion through prefix-72 displacement count 10

Date: 2026-08-26

Status: **exact finite theorem** in the repaired global binary branch. This supersedes the earlier `D_72<=8` finite certificate. It does not prove the Collatz conjecture.

## 1. Setting

At the first possible global coefficient resonance

\[
(A_0,q_0)=(114208327604,72057431991),
\]

every hypothetical minimal-counterexample start lies in

\[
2^{71}<N<\frac43\,2^{71}<2^{72}.
\]

Hence its first 72 parity bits expose the whole ordinary integer address.

Let `b_j` be the odd positions of the first-crossing mechanical word and `a_j` those of the actual word. Prefix coefficient survival implies

\[
a_j\le b_j.
\]

Define

\[
D_{72}:=\#\{j:a_j<72,\ a_j\ne b_j\}.
\]

Any additional odd ordinal entering the first 72 positions beyond the 46 mechanical odd ordinals is automatically counted because its mechanical position is at least 72.

## 2. Complete finite scan

The companion certificate enumerates **every** coefficient-surviving length-72 ordinal-position vector with

\[
D_{72}\le10.
\]

For every canonical residue in the strict first-resonance band, it follows the exact ordinary shortcut orbit until its actual first coefficient crossing.

The exact counts are

\[
\begin{array}{c|r|r|r}
D_{72}&\text{prefixes}&\text{band starts}&\text{latest first crossing}\\\hline
0&1&0&-\\
1&26&7&81\\
2&351&40&140\\
3&3275&541&134\\
4&23725&3913&184\\
5&142153&23583&265\\
6&732947&122732&278\\
7&3341257&557068&308\\
8&13733231&2290462&379\\
9&51650827&8608590&357\\
10&179812491&29964365&471
\end{array}
\]

Thus the scan covers

\[
\boxed{249,440,284}
\]

prefixes and

\[
\boxed{41,571,301}
\]

distinct ordinary starts in the first-resonance band.

Every one of those starts has a first coefficient crossing whose endpoint is strictly below the start. There are

\[
\boxed{0}
\]

paradoxical first crossings in the complete certified family.

The latest first crossing in the family occurs at only

\[
\boxed{471}
\]

shortcut steps.

## 3. Proof-level consequence

A genuine first-resonance minimal-counterexample candidate must therefore satisfy

\[
\boxed{D_{72}\ge11.}
\]

Through the exact defect bound

\[
\frac{E}{3^{q_0}}
>\frac16\sum_j(1-2^{-s_j}),
\]

this implies the coarse numerical corollary

\[
\boxed{E/3^{q_0}>11/12.}
\]

The numerical correction loss is not yet the important part: the structural statement is that a candidate must already use at least eleven nonmechanical ordinal channels before the 72-bit ordinary address has finished forming.

## 4. Why brute-force extension is no longer the preferred move

The number of position vectors grows rapidly:

- `D_72=8`: 13,733,231 exact prefixes;
- `D_72=9`: 51,650,827;
- `D_72=10`: 179,812,491.

The exact `D_72<=10` scan remains conveniently reproducible, but continuing by one displacement at a time will soon spend substantial computation for only a constant improvement in the defect lower bound.

The appropriate next target is structural:

\[
\boxed{
\text{bounded 72-bit formation floor}
+\text{very long coefficient survival}
\Longrightarrow
\text{many early/renewed displacement channels}.
}
\]

In particular, seek a transfer theorem that forces new displacement when a fixed bounded natural address survives through successive Beatty return scales.

## 5. DSD audit role

This certificate is an example of how the DSD logical chain is being used without becoming an additional mathematical axiom:

\[
\text{global candidate domain}
\to
\text{first-resonance band}
\to
\text{complete 72-bit address exposure}
\to
\text{ordinal-displacement state}
\to
\text{actual first-crossing test}.
\]

Each arrow has a standard arithmetic interpretation and can be verified without accepting DSD terminology. DSD's role is to keep the domains and information channels aligned and to identify where a finite certificate can be promoted to a reusable lemma.

Certificate:

`collatz/src/global_first_resonance_prefix72_displacement10_certificate.cpp`.
