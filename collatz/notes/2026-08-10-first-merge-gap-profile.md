# First-merge q-gap profile

Date: 2026-08-10

Status: exact finite diagnostic through depth 32. No global theorem is claimed.

For a new same-depth endpoint merge, order the two states so that

\[
q_h>q_l,
\qquad d=q_h-q_l.
\]

The exact coefficient-survivor enumeration through depth 32 contains

\[
2,760,811
\]

new merge pairs. Their cumulative q-gap distribution is

| d | new merge pairs |
|---:|---:|
| 1 | 2,734,148 |
| 2 | 25,503 |
| 3 | 1,158 |
| 4 | 2 |

No new equal-q merge pair was found through depth 32.

Thus almost all observed first mergers are adjacent-q interactions. The largest observed gap is 4.

The two d=4 mergers both occur at depth 32:

\[
y=3,962,615,339,
\]
\[
(r_l,q_l)=(1,627,029,503,21),
\qquad
(r_h,q_h)=(20,086,783,25),
\]

and

\[
y=5,943,923,009,
\]
\[
(r_l,q_l)=(2,440,544,255,21),
\qquad
(r_h,q_h)=(30,130,175,25).
\]

In both examples,

\[
r_l-3^4r_h=80=3^4-1.
\]

This visually strong identity is not a universal first-merge law. Testing all 2,760,811 new merges for divisibility

\[
3^d-1\mid r_l-3^d r_h
\]

gives 3,450 failures in total. Broken down by q-gap:

| d | total | divisibility failures |
|---:|---:|---:|
| 1 | 2,734,148 | 0 |
| 2 | 25,503 | 3,413 |
| 3 | 1,158 | 37 |
| 4 | 2 | 0 |

The d=1 divisibility is automatic because \(3^1-1=2\) and the relevant canonical starts are odd, so their scaled difference is even. It should not be interpreted as additional structure.

The useful structural observation remains the much weaker and still unproved global target recorded in the companion status note:

\[
R_h>R_l
\]

at every new coefficient-surviving endpoint merge. The q-gap profile indicates that a proof strategy specialized first to d=1, then treating rare d>=2 interactions separately, may be more economical than a single unrestricted pair theorem.
