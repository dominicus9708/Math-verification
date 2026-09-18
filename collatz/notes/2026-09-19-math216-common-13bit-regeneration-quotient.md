# MATH-216 — one 13-bit regeneration quotient for all remaining paid counts r=2..10

Date: 2026-09-19

Status: EXACT COMMON QUOTIENT / ALL OPEN MULTI-PAID TAGS SHARE ONE REGISTER / r=10 OPEN

## 1. Purpose

MATH-215 proves that a dangerous nonzero-carry transition with emitted paid count \(r\) requires
\[
\gamma=\nu_2(3^Qu+a)\ge z_{\min}(r),
\]
after matching the carry and factor valuations.

For the currently unresolved range
\[
2\le r\le10,
\]
the largest threshold is
\[
\boxed{z_{\min}(10)=13}.
\]

Therefore the entire remaining paid-count range can be tested with one 13-bit odd-carry register. No separate \(r=10,r=9,\ldots,r=2\) address automata are required.

## 2. Common residue

On the nonzero-carry matched-valuation branch write
\[
d=2^su,\qquad c=2^sa
\]
with \(u,a\) odd.

Define
\[
\boxed{R_{13}:=3^Qu+a\pmod{8192}}.
\]

For emitted tag \(r\in\{2,\ldots,10\}\),
\[
\boxed{
\text{danger can survive only if }
R_{13}\equiv0\pmod{2^{z_{\min}(r)}}.
}
\]

Thus the emitted paid count selects only a low-bit mask on the same register.

## 3. Explicit masks

| emitted r | required low zero bits |
|---:|---:|
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 6 |
| 6 | 7 |
| 7 | 8 |
| 8 | 10 |
| 9 | 11 |
| 10 | 13 |

For \(r=10\),
\[
\boxed{R_{13}=0}.
\]

## 4. Zero incoming carry

If \(d=0\) and \(c\ne0\), MATH-215 requires
\[
\nu_2(c)\ge z_{\min}(r).
\]

The same 13-bit register may be used by taking
\[
R_{13}^{(0)}=c\bmod8192.
\]

The emitted \(r\) selects the same low-zero-bit mask.

The exact reset
\[
d=0,\qquad c=0
\]
remains a separate flag.

## 5. One common transition architecture

The theorem-facing executor may therefore use
\[
\boxed{
(\text{phase},
\text{Hensel/Pareto cell},
\text{valuation-match state},
R_{13},
\text{reset flag})
}
\]
and let the MATH-187/209 recurrence emit \(r\) only at first return.

Then:
1. no \(r\)-specific transition law is invoked;
2. no depth interval is scanned;
3. no unbounded carry magnitude is retained;
4. the emitted \(r\) only selects a bit mask.

## 6. r=10 closure target

The \(r=10\) layer is now reduced to:
\[
\boxed{
\text{Can a reachable Hensel/Pareto-extremal terminal state emit }r=10
\text{ with }R_{13}=0?
}
\]
together with the separate exact-reset possibility.

MATH-206 already answers this negatively for the frozen initial zero-carry full-factor catalogue.

The remaining structural task is nonreachability in the regenerated common quotient.

## 7. Higher paid counts

For \(r\ge11\), MATH-202 requires more than 13 regeneration bits, reaching 29 bits by \(r=21\).

Those layers are already closed in the older audited multi-paid framework. A future fully uniform structural proof may enlarge the common register to 29 bits, but this is not required to put all currently open \(r=2..10\) tags into one quotient.

## 8. Claim boundary

Established:
- one 13-bit residue is sufficient for every remaining paid count \(2\le r\le10\);
- emitted \(r\) acts only as a low-bit mask selector;
- r=10 danger requires the exact residue \(R_{13}=0\);
- raw carry magnitude, raw depth, and separate per-r address automata are unnecessary.

Not established:
- nonreachability of \(R_{13}=0\) at every emitted r=10 terminal;
- universal reset exclusion;
- closure of r=10;
- lower-r layer closure;
- first-cell emptiness;
- the Collatz conjecture.
