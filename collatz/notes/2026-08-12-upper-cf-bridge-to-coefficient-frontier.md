# Bridge from upper-CF renewal ceilings to the coefficient-survivor frontier

Date: 2026-08-12

Status: **exact bridge theorem + finite eliminations using previously established coefficient-survivor frontier data**. This does not supply an asymptotic exclusion of all upper convergents.

## 1. First-crossing identity

For a primitive upper-CF renewal word of accelerated length `A` and odd count `H`, every proper prefix is coefficient-surviving while the full word is coefficient-contracting:

\[
3^{H_p}>2^{A_p}
\quad\text{for every proper prefix},
\]

and

\[
3^H<2^A.
\]

Hence for any integer realizing such a renewal,

\[
\boxed{\tau_c(N)=A.}
\]

Therefore

\[
\boxed{N\ge\mu(A-1),}
\]

where

\[
\mu(K):=\min\{n\ge1:\tau_c(n)>K\}.
\]

## 2. Exact renewal ceiling

The upper-CF first-crossing correction theorem gives

\[
N<\frac{H}{3(P-1)},
\qquad
P=\frac{2^A}{3^H}.
\]

Equivalently,

\[
\boxed{
N<\frac{H3^{H-1}}{2^A-3^H}.
}
\]

Thus an upper-CF renewal can exist only if

\[
\boxed{
\mu(A-1)
<
\frac{H3^{H-1}}{2^A-3^H}.
}
\]

This is an exact compatibility test between the global coefficient-survivor frontier and the local renewal ceiling.

## 3. Previously established coefficient-frontier data

The current repository checkpoint contains

\[
\mu(447)=12{,}235{,}060{,}455,
\]

\[
\mu(k)=12{,}235{,}060{,}455
\qquad(447\le k\le546),
\]

and

\[
\mu(547)\ge400{,}000{,}000{,}000.
\]

Since `mu` is nondecreasing,

\[
\boxed{
\mu(K)\ge400{,}000{,}000{,}000
\quad\text{for every }K\ge547.
}
\]

## 4. Exact upper-convergent eliminations

For the upper convergent

\[
(A,H)=(485,306),
\]

the renewal ceiling is

\[
\boxed{N\le99{,}729.}
\]

But

\[
N\ge\mu(484)=12{,}235{,}060{,}455.
\]

Contradiction.

For

\[
(A,H)=(24727,15601),
\]

the exact ceiling is

\[
\boxed{N\le285{,}814{,}986.}
\]

But

\[
N\ge\mu(24726)\ge\mu(547)\ge400{,}000{,}000{,}000.
\]

Contradiction.

For

\[
(A,H)=(125743,79335),
\]

the exact ceiling is

\[
\boxed{N\le7{,}216{,}089{,}270.}
\]

Again

\[
N\ge\mu(125742)\ge400{,}000{,}000{,}000.
\]

Contradiction.

Thus

\[
\boxed{
\text{the primitive upper-CF renewal branch is excluded through }A=125743.
}
\]

## 5. Current frontier

The next upper convergent is

\[
(A,H)=(301994,190537).
\]

Its exact renewal ceiling is

\[
\boxed{N\le984{,}572{,}779{,}224.}
\]

This exceeds the present general frontier lower bound

\[
\mu(K)\ge400{,}000{,}000{,}000
\qquad(K\ge547),
\]

so the existing finite coefficient-frontier data no longer decides this convergent.

This identifies a clean boundary between the existing finite audit and the remaining asymptotic arithmetic problem.

## 6. Structural role

The useful point is not merely the finite exclusion. The two independently derived quantities now meet in one inequality:

\[
\boxed{
\mu(A-1)
\le N
<
\frac{H3^{H-1}}{2^A-3^H}.
}
\]

Therefore a complete asymptotic upper-CF exclusion could be obtained from any universal lower bound on `mu(A-1)` that eventually exceeds the convergent renewal ceiling.

Conversely, failure to obtain such a bound shows precisely why coefficient-survivor growth remains part of the hard core rather than something already solved by the renewal reduction.
