# R1 E=20--21 formation subtraction ladder

Date: 2026-08-18

Status: **exact finite certificate inside the current isolated R1 core**.
This is not a global proof of the Collatz conjecture.

## 1. E=20

The exact necessary even-position vector is

\[
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,83,180,331,569,945].
\]

Because the event of rank 16 cannot occur before position 180, the window
73..179 has length 107 and a first-73 layer with \(k=e_{73}\) contains at most
\(16-k\) further even events in that window.  The earlier first-73 certificates
already remove \(k\le8\), while the position vector gives \(k\le15\).  Hence
\(k=9,\ldots,15\) are the only E=20 layers to check.

Using

\[
U_{73}\equiv-\sum_{i=0}^{z-1}2^{p_i}3^{-(p_i-i)}\pmod{2^{107}},
\]

with MITM enumeration for the large sparse layers gives:

| \(e_{73}\) | max window evens | raw classes | numerical intersection | zero by |
|---:|---:|---:|---:|---:|
| 15 | 1 | 108 | 0 | immediate |
| 14 | 2 | 5,779 | 0 | immediate |
| 13 | 3 | 204,264 | 11 | \(K=18\) |
| 12 | 4 | 5,364,874 | 845 | \(K=27\) |
| 11 | 5 | 111,673,440 | 54,844 | \(K=33\) |
| 10 | 6 | 1,918,919,062 | 2,820,474 | \(K=33\) |
| 9 | 7 | 27,994,891,608 | 123,546,096 | \(K=36\) |

For \(k=10\), the checkpoint ladder is

\[
265,666\ (K=15)
\to50,309\to7,337\to848\to93\to11\to0\ (K=33).
\]

For \(k=9\), the exact ladder is

\[
123,546,096
\to5,560,638\ (K=15)
\to871,631\ (K=18)
\to109,482\ (K=21)
\to11,660\ (K=24)
\to1,120\ (K=27)
\to92\ (K=30)
\to5\ (K=33)
\to0\ (K=36).
\]

Therefore

\[
\boxed{E=20\text{ is empty}}.
\]

## 2. E=21

The exact necessary vector is

\[
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,86,182,333,571,946].
\]

Using the rank-17 event bound at position 182 gives the 109-step window
73..181 and at most \(17-k\) further even events.  The relevant first-73
layers are \(k=9,\ldots,16\).

| \(e_{73}\) | max window evens | raw classes | numerical intersection | zero by |
|---:|---:|---:|---:|---:|
| 16 | 1 | 110 | 0 | immediate |
| 15 | 2 | 5,996 | 0 | immediate |
| 14 | 3 | 215,930 | 0 | immediate |
| 13 | 4 | 5,779,181 | 72 | \(K=24\) |
| 12 | 5 | 122,607,452 | 5,047 | \(K=30\) |
| 11 | 6 | 2,147,630,816 | 263,702 | \(K=33\) |
| 10 | 7 | 31,944,403,172 | 11,748,678 | \(K=36\) |
| 9 | 8 | 411,853,250,711 | 454,352,631 | \(K=39\) |

For \(k=10\):

\[
1,104,581\ (K=15)
\to208,347\to30,017\to3,628\to392\to32\to2\to0\ (K=36).
\]

For \(k=9\), the zero-through-seven-event portion gives

\[
35,245,014
\to1,585,534\to248,162\to31,116\to3,391\to326\to17\to1\to0.
\]

The exact eight-event layer was split by the first right-half event position
and evaluated in four disjoint batches.  Their combined ladder is

\[
419,107,617
\to18,865,160\ (K=15)
\to2,956,993\ (K=18)
\to369,580\ (K=21)
\to39,409\ (K=24)
\to3,782\ (K=27)
\to328\ (K=30)
\to23\ (K=33)
\to2\ (K=36)
\to0\ (K=39).
\]

Adding the lower sublayers gives the full \(k=9\) ladder

\[
454,352,631
\to20,450,694
\to3,205,155
\to400,696
\to42,800
\to4,108
\to345
\to24
\to2
\to0.
\]

Hence

\[
\boxed{E=21\text{ is empty}}
\qquad\Longrightarrow\qquad
\boxed{e_{1539}\ge22}.
\]

## 3. G13 consequence

For E=22..34 the exact relaxed endpoint optimizer has its largest value at
E=22 with

\[
\lfloor\log_2 U_{1539}^{\max}\rfloor=937.
\]

At E=35 the coarse product bound is already below \(2^{938}\) and is halved by
each additional even event.  Therefore

\[
\boxed{x_{1539}<2^{938}}.
\]

Since

\[
938=49\cdot19+7,
\]

the natural G13 cut becomes

\[
\boxed{t_{49}<2^7=128,\qquad t_b=0\ (b\ge50)}.
\]

The number of forced high zero G13 address bits is

\[
\boxed{20026-938=19088}.
\]

## 4. E=22 frontier

The next exact necessary event-position vector is

\[
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,26,88,184,335,572,947].
\]

Using the position-184 event gives a 111-step window and the next finite layers
\(e_{73}=9,\ldots,17\), with at most \(18-k\) window-even events.
The largest raw layer is \(k=9\):

\[
\sum_{j=0}^{9}\binom{111}{j}=5,530,925,666,576.
\]

This is now the main frontier for the window-formation transfer implementation.
