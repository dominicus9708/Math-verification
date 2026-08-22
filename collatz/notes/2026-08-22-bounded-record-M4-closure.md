# Exact closure of the eventual M=4 bounded-record branch

Date: 2026-08-22

Status: **exact exclusion of every hypothetical divergent positive-integer tail whose record gaps are eventually at most four.** This closes the first previously unresolved bounded-record case. It does not close M>=5 and is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil,
\qquad
d_k=b_k-b_{k-1}\in\{0,1\}.
\]

Let `tau_r` be sufficiently late first record times of the height

\[
h_k=m_k-b_k.
\]

Every record climb ends with a plateau-odd step, hence

\[
\boxed{d_{\tau_{r+1}}=0.}
\]

Thus late record times lie at zero positions of the mechanical word `d`.

## 1. Consecutive mechanical zeros are separated by two or three steps

The mechanical word contains no `00` because

\[
2\alpha>1.
\]

Indeed every length-two factor has either `floor(2alpha)=1` or `ceil(2alpha)=2` ones.

It also contains no `111` because

\[
3\alpha<2.
\]

Every length-three factor has either one or two ones, never three.

Therefore the distance between consecutive zero positions is exactly

\[
\boxed{2\text{ or }3.}
\]

## 2. Two consecutive zero-gaps of length two are impossible

If zero positions occurred at

\[
s,\quad s+2,\quad s+4,
\]

then the length-five mechanical factor beginning at `s` would be

\[
01010.
\]

But a Sturmian/Beatty factor of length five has either

\[
\lfloor5\alpha\rfloor=3
\]

or

\[
\lceil5\alpha\rceil=4
\]

ones. The word `01010` has only two ones.

Hence

\[
\boxed{\text{the zero-gap pattern }2,2\text{ never occurs}.}
\]

Equivalently, every pair of consecutive zero-gaps has total length at least five.

## 3. An M=4 record tail cannot skip a mechanical zero

Assume now that for all sufficiently large record levels

\[
L_r=\tau_{r+1}-\tau_r\le4.
\]

Starting from a late record time `tau_r`, the next mechanical zero occurs after two or three steps.

If the next record did not occur at that zero, it would have to skip it and end at a later zero. Such a skip has length equal to the sum of two consecutive mechanical zero-gaps.

The only way that sum could be at most four is

\[
2+2=4,
\]

which was just proved impossible.

Therefore every sufficiently late record time is followed by the **immediately next** mechanical zero:

\[
\boxed{L_r\in\{2,3\}.}
\]

## 4. The corresponding record macros are uniquely all-odd

Between consecutive mechanical zeros the only possible factors are

\[
10
\]

and

\[
110.
\]

A record first-passage word begins at relative height zero, stays at or below that record until its final step, and ends at relative height `+1`.

For mechanical factor `10`, total mechanical rise count is one, so the actual parity word must have two odd bits. The unique possibility is

\[
\boxed{11}.
\]

For mechanical factor `110`, total mechanical rise count is two, so the actual parity word must have three odd bits. The unique possibility is

\[
\boxed{111}.
\]

Thus every sufficiently late record block in an eventual M=4 tail is all odd.

Concatenating the record blocks gives an eventually all-odd accelerated parity tail.

## 5. A positive integer cannot have an eventually all-odd accelerated tail

Use

\[
z=x+1.
\]

On an odd accelerated Collatz step,

\[
\boxed{z\mapsto\frac{3z}{2}.}
\]

If `ell` consecutive future steps are all odd, then the starting `z` must be divisible by `2^ell`.

An infinite all-odd tail would therefore require

\[
2^\ell\mid z
\]

for every `ell`, hence `z=0` in the ordinary integers. This would mean `x=-1`, not a positive integer.

Therefore

\[
\boxed{
L_r\le4\text{ eventually is impossible for a divergent positive integer.}
}
\]

Combined with the earlier M<=3 pruning, the bounded-record remainder now starts at

\[
\boxed{M\ge5.}
\]

## 6. Why length-four non-singleton factors do not contradict this theorem

The mechanical word does contain length-four factor `1010`, and the earlier local terminal theorem correctly assigns it two record first-passage words.

However a **late record macro starts immediately after a mechanical zero**, because the previous record ended on a plateau. For `1010` to be the entire interval between two record zeros of length four, the preceding zero together with this factor would create

\[
01010,
\]

which is forbidden.

Thus `1010` exists as a local mechanical factor but is not reachable as a complete late record-to-record interval under an M=4 tail. This distinction is essential.

Companion certificate:

`collatz/src/bounded_record_M4_closure_certificate.py`.
