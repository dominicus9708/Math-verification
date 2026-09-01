# A0 s=1 Route-B — terminal residue to critical right-H transfer

Date: 2026-09-01

Status: **EXACT transfer theorem CLOSED; inverse projective-path compression and root closure OPEN.**

Certificate:

`collatz/src/A0_s1_routeB_terminal_residue_rightH_transfer_certificate.py`

## 1. Purpose

The previous G2 work identified the correct remaining object as the inverse image of the **actual terminal checkpoint residue**, not the set of all possible ternary carries.

This note closes the exact dependency chain

\[
Z \bmod 3^\ell
\longrightarrow
N_J \bmod 3^\ell
\longrightarrow
\Delta_L \bmod 3^\ell
\longrightarrow
\Delta_H \bmod 3^\ell
\longrightarrow
z_{\rm req}\bmod 3^\ell.
\]

It also audits the sign convention against the backward exponential carry chart.

No marginal-density independence assumption is used.

---

## 2. Correction composition

For words \(A,B\), with \(A\) occurring before \(B\),

\[
C(AB)=3^{q(B)}C(A)+2^{|A|}C(B).
\]

For target/candidate pairs of equal block length and equal block one-count,

\[
\Delta(AB)
=
3^{q(B)}\Delta(A)+2^{|A|}\Delta(B),
\]

where throughout this note

\[
\Delta=C(\text{target})-C(\text{candidate}).
\]

This sign is the forward H-defect convention already used by the H/L min-plus certificate.

---

## 3. Full checkpoint to full correction defect

The checkpoint identity is

\[
2^{t_0}Z=3^{j_0}X+C(W).
\]

For every \(\ell\le j_0\),

\[
C(W)\equiv 2^{t_0}Z\pmod{3^\ell}.
\]

Define

\[
N_J=C(W_{\rm th})-C(W).
\]

Then exactly

\[
\boxed{
N_J\equiv C(W_{\rm th})-2^{t_0}Z
\pmod{3^\ell}.
}
\]

---

## 4. Shielding to the final \(L\)-block

The threshold word is

\[
W_{\rm th}=UL^9.
\]

Split the full word immediately before its final \(L\)-block:

\[
W=P\,L_{\rm cand}.
\]

The prefix has length \(9J_0\), and the final \(L\)-block has \(R_0\) ones.

Write

\[
\Delta_P=C(P^*)-C(P),
\qquad
\Delta_L=C(L^*)-C(L_{\rm cand}).
\]

Then

\[
N_J
=
3^{R_0}\Delta_P
+
2^{9J_0}\Delta_L.
\]

Hence, for every \(\ell\le R_0\), the prefix term vanishes modulo \(3^\ell\), giving

\[
\boxed{
\Delta_L
\equiv
2^{-9J_0}N_J
\pmod{3^\ell}.
}
\]

This is exact suffix shielding, not a statistical approximation.

---

## 5. Critical cut to the right-H factor

Inside the final \(L\)-block use the certified critical cut

\[
c=9,809,721,694,
\qquad
s=630,138,897,
\qquad
c+s=J_0.
\]

The target right factor is \(H_s^*\), with

\[
q_H=\lfloor\alpha s\rfloor+1
=397,573,380.
\]

Write

\[
L_{\rm cand}=A\,H,
\]

and define

\[
\Delta_A=C(A^*)-C(A),
\qquad
\Delta_H=C(H_s^*)-C(H).
\]

Then

\[
\Delta_L
=
3^{q_H}\Delta_A
+
2^c\Delta_H.
\]

Therefore, for every \(\ell\le q_H\),

\[
\boxed{
\Delta_H
\equiv
2^{-c}\Delta_L
\pmod{3^\ell}.
}
\]

Combining the two shielding steps,

\[
\boxed{
\Delta_H
\equiv
2^{-(9J_0+c)}N_J
\pmod{3^\ell}.
}
\]

---

## 6. Cancellation to the clean terminal join

Because

\[
t_0-(9J_0+c)
=
J_0-c
=
s,
\]

and because the target correction compositions themselves satisfy the same two shielding identities,

\[
2^{-9J_0}C(W_{\rm th})
\equiv C(L^*)
\pmod{3^\ell},
\]

\[
2^{-c}C(L^*)
\equiv C(H_s^*)
\pmod{3^\ell},
\]

we obtain

\[
\boxed{
\Delta_H
\equiv
C(H_s^*)-2^sZ
\pmod{3^\ell}.
}
\]

Equivalently,

\[
\boxed{
C(H)\equiv2^sZ\pmod{3^\ell}.
}
\]

This holds for every

\[
\ell\le\min(R_0,q_H).
\]

Thus it includes all currently relevant precisions

\[
\ell=18,24,28,47.
\]

---

## 7. Backward-chart sign audit

The backward exponential carry chart was defined by

\[
\Gamma_{m,z_+,A}(B)
=
3z_+-2^A+2^B
\pmod{3^m}.
\]

Its atomic term is therefore candidate-minus-target:

\[
2^B-2^A.
\]

But

\[
\Delta_H=C(H_s^*)-C(H)
\]

uses target-minus-candidate.

Therefore the backward chart must be initialized with

\[
\boxed{
z_{\rm req}
\equiv
-\Delta_H
\pmod{3^\ell}.
}
\]

Using the terminal join,

\[
\boxed{
z_{\rm req}
\equiv
2^sZ-C(H_s^*)
\pmod{3^\ell}.
}
\]

This sign is now fixed and should not be silently reversed in later G2 code.

---

## 8. Exact practical join constants

Only the final \(\ell\) ranked-one positions of \(H_s^*\) contribute to

\[
C(H_s^*)\bmod3^\ell.
\]

The certificate extracts these positions using the same exact rational enclosure for

\[
\alpha=\frac{\log2}{\log3}
\]

as the H/L certificates.

| \(\ell\) | \(3^\ell\) | \(2^s\bmod3^\ell\) | \(C(H_s^*)\bmod3^\ell\) | \((2^s)^{-1}\bmod3^\ell\) |
|---:|---:|---:|---:|---:|
| 18 | 387,420,489 | 139,937,030 | 20,406,043 | 38,405,528 |
| 24 | 282,429,536,481 | 169,442,690,723 | 135,230,156,704 | 117,039,393,206 |
| 28 | 22,876,792,454,961 | 12,596,342,295,887 | 2,677,095,985,033 | 17,062,811,582,066 |
| 47 | 26,588,814,358,957,503,287,787 | 16,163,172,281,939,751,936,170 | 5,836,864,555,257,551,064,118 | 5,262,100,326,525,769,175,294 |

Hence, at \(\ell=47\),

\[
\boxed{
z_{\rm req}
\equiv
16,163,172,281,939,751,936,170\,Z
-
5,836,864,555,257,551,064,118
\pmod{3^{47}}.
}
\]

Since \(2^s\) is invertible modulo every \(3^\ell\),

\[
Z
\equiv
2^{-s}
\left(z_{\rm req}+C(H_s^*)\right)
\pmod{3^\ell}.
\]

Thus the \(Z\)-residue and the right-H root carry are in exact affine bijection at fixed precision.

---

## 9. DSD audit

### EXACT / CLOSED

- full checkpoint residue \(\to N_J\bmod3^\ell\);
- final-\(L\) suffix shielding;
- critical-cut right-H shielding;
- clean cancellation to
  \[
  C(H)\equiv2^sZ\pmod{3^\ell};
  \]
- backward-chart sign:
  \[
  z_{\rm req}\equiv-\Delta_H;
  \]
- affine \(Z\leftrightarrow z_{\rm req}\) bijection for every fixed \(\ell\le\min(R_0,q_H)\).

### REGRESSION ONLY

The certificate also performs finite exact implementation checks:

- 450 correction-composition checks;
- 2,800 suffix-projection checks;
- 2,800 critical-projection checks;
- 2,800 backward-sign checks;
- exact root arithmetic and join constants for \(\ell=18,24,28,47\).

These finite checks validate the implementation; they are not the proof of the symbolic transfer theorem.

### REJECTED

Do **not** infer that terminal ternary exposure contributes an independent multiplicative density factor.

The correct object is the synchronized relation

\[
Z\bmod3^\ell
\longleftrightarrow
z_{\rm req}\bmod3^\ell.
\]

Therefore a later CRT or checkpoint count must preserve the common \(Z\) coordinate.

### OPEN

- Invert the right-H multi-gate projective/carry family only over the synchronized values \(z_{\rm req}(Z)\), rather than over all \(3^\ell\) carries.
- Combine this with the existing 27-bit dyadic checkpoint-tail exposure without independence multiplication.
- Determine the smallest projective state required for the actual 14 root families.
- Close any of the 14 roots only after the full synchronized predicate chain is active.
- No Collatz proof is claimed.
