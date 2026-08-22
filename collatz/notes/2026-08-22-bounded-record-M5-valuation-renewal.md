# M=5 bounded-record branch as an exact valuation renewal

Date: 2026-08-22

Status: **exact structural reduction of the first unresolved bounded-record case.** The eventual M<=4 branch is already closed. This note reduces M=5 to a finite macro alphabet synchronized with a 2-adic/3-adic valuation renewal. It does not exclude every infinite renewal and is not a proof of the Collatz conjecture.

Let

\[
z=x+1.
\]

For the accelerated Collatz map,

- if `x` is odd (`z` even),
  \[
  \boxed{z\mapsto 3z/2};
  \]
- if `x` is even (`z` odd),
  \[
  \boxed{z\mapsto (z+1)/2}.
  \]

Let the mechanical Beatty bits be

\[
d_k=b_k-b_{k-1},
\qquad b_k=\lceil k\log_3 2\rceil.
\]

Late record times lie at mechanical zero positions.

## 1. Mechanical zero-gap alphabet

As proved in the M=4 closure note, consecutive mechanical zeros are separated by

\[
\boxed{2\text{ or }3}
\]

steps, and the gap pair `2,2` never occurs.

Let

\[
g_i\in\{2,3\}
\]

be the consecutive zero-gap sequence.

Under an eventual record bound `M=5`, a record interval can therefore do only one of two things.

1. Use the immediately next mechanical zero, giving length `2` or `3`.
2. Skip exactly one mechanical zero. This is possible only when
   \[
   g_i+g_{i+1}=5,
   \]
   i.e. gap pair `2,3` or `3,2`.

Skipping two mechanical zeros is impossible because the sum of three positive zero-gaps is at least `2+3+2=7>5` (and `2,2` is already forbidden).

Thus the record selection itself has a finite local alphabet.

## 2. Exact M=5 record macro alphabet

### No skipped zero

Gap `2` gives mechanical factor

\[
10
\]

and the unique record first-passage parity word

\[
\boxed{11}.
\]

Gap `3` gives mechanical factor

\[
110
\]

and the unique record word

\[
\boxed{111}.
\]

### Skip across gap pair `2,3`

The mechanical factor is

\[
10110.
\]

Its exact record first-passage words are

\[
\boxed{01111,\qquad10111}.
\]

### Skip across gap pair `3,2`

The mechanical factor is

\[
11010.
\]

Its exact record words are

\[
\boxed{01111,\qquad10111,\qquad11011}.
\]

Therefore every M=5 non-singleton record contains **exactly one even parity step**.

## 3. Exact z-maps

The five possible record-map formulas are:

\[
\boxed{
11:\quad z'={9z\over4},
}
\]

\[
\boxed{
111:\quad z'={27z\over8},
}
\]

and

\[
\boxed{
01111:\quad z'={81(z+1)\over32},
}
\]

\[
\boxed{
10111:\quad z'={81z+54\over32}
={27(3z+2)\over32},
}
\]

\[
\boxed{
11011:\quad z'={81z+36\over32}
={9(9z+4)\over32}.
}
\]

The corresponding exact input congruences modulo `32` for the three non-singleton maps are

\[
\boxed{
01111:\ z\equiv31\pmod{32},
}
\]

\[
\boxed{
10111:\ z\equiv10\pmod{32},
}
\]

\[
\boxed{
11011:\ z\equiv28\pmod{32}.
}
\]

In particular their input 2-adic valuations are respectively

\[
\boxed{0,1,2.}
\]

## 4. Deterministic rule from lambda=v2(z)

At a record time let

\[
\lambda=v_2(z)
\]

and let `g in {2,3}` be the distance to the immediately next mechanical zero.

If

\[
\boxed{\lambda\ge g,}
\]

then the next `g` actual parity bits are all odd. The trajectory reaches the immediately next mechanical zero and creates the next record there. Thus the record macro is the singleton `11` or `111`, and

\[
\boxed{\lambda'=\lambda-g.}
\]

If

\[
\boxed{\lambda<g,}
\]

then an actual even step occurs before the next mechanical zero, so that zero cannot be the next record time. To preserve the M=5 bound, the trajectory must skip it and reach the following zero in at most five steps. Hence necessarily

\[
\boxed{g+g_{next}=5.}
\]

The value `lambda=0,1,2` selects which of the available non-singleton words can occur.

This makes the record selection deterministic once the current integer `z` and the mechanical phase are known.

## 5. Exact 3-adic valuation update

Let

\[
a=v_3(z)
\]

at a sufficiently late record time. Every record macro ends with at least two odd steps, so `a>=2` after the first such record.

For a singleton macro, no even reset occurs. Hence

\[
\boxed{
11:\ a'=a+2,
\qquad
111:\ a'=a+3.
}
\]

For a non-singleton macro, the unique even step acts on a value divisible by `3`, so `(z+1)/2` or its shifted analogue is not divisible by `3`. All accumulated 3-adic valuation is reset to zero at that even event. The remaining odd steps then rebuild the valuation exactly.

Therefore

\[
\boxed{
01111:\ a'=4,
}
\]

\[
\boxed{
10111:\ a'=3,
}
\]

\[
\boxed{
11011:\ a'=2.
}
\]

Thus singleton records transfer available 2-adic divisibility into increasing 3-adic divisibility, whereas every non-singleton reset destroys the accumulated 3-adic valuation and creates a new 2-adic divisibility requirement through an affine `+1` event.

## 6. 2-adic reset formulas at a non-singleton record

The outgoing 2-adic valuation is

\[
\boxed{
01111:\quad
\lambda'=v_2(z+1)-5,
}
\]

\[
\boxed{
10111:\quad
\lambda'=v_2(3z+2)-5,
}
\]

\[
\boxed{
11011:\quad
\lambda'=v_2(9z+4)-5.
}
\]

The input congruences above guarantee that these quantities are nonnegative.

Consequently the first unresolved bounded-record branch is an exact valuation renewal driven by

- the Sturmian zero-gap word `g_i in {2,3}`;
- deterministic subtraction of `2` or `3` from `v_2(z)` on singleton records;
- one of three affine 2-adic reset valuations on a non-singleton record;
- deterministic growth/reset of `v_3(z)` as above.

## 7. Remaining M=5 theorem

A complete closure of M=5 would follow from:

> **M=5 valuation-renewal theorem.** No positive integer `z` can iterate the above synchronized renewal forever while satisfying the Sturmian zero-gap admissibility condition.

This is a substantially smaller arithmetic problem than the unrestricted Collatz divergent-orbit problem, but it is not yet proved here.
