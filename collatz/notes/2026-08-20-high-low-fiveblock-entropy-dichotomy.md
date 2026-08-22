# High/low five-block entropy dichotomy

Date: 2026-08-20

Status: **exact combinatorial entropy split for the current sparse-tail classification.** This is not a same-integer cross-base theorem and not a proof of the Collatz conjecture.

## 1. Five-block alphabet

Classify each aligned five-bit parity word by its odd count:

- high block: \(q\ge4\);
- low block: \(q\le3\).

Among all \(2^5=32\) words,

\[
\#\mathcal H
=\binom54+\binom55
=6,
\]

and

\[
\#\mathcal L
=32-6
=26.
\]

The self-prepend theorem gives the high class a deterministic role: its exact syndrome penalty dominates its affine correction rebate. The low class is where local normalized losses may still occur.

## 2. Language count with a low-block frequency cap

For \(n\) aligned five-blocks, suppose at most \(m\) blocks are low. Ignoring the additional coefficient-prefix restrictions gives the safe upper bound

\[
\boxed{
N(n,m)
\le
\sum_{j=0}^{m}
\binom nj
26^j6^{n-j}.
}
\]

Put

\[
\rho=\frac mn.
\]

For \(0\le\rho\le26/32\), the asymptotic binary entropy per parity bit is

\[
\boxed{
e(\rho)
=
\frac{
H_2(\rho)
+\rho\log_2 26
+(1-\rho)\log_2 6
}{5}.
}
\]

Hence the corresponding dyadic exclusion rate is

\[
\boxed{
\eta_{HL}(\rho)=1-e(\rho).
}
\]

At \(\rho=0\), every block is high and

\[
\eta_{HL}(0)
=1-\frac{\log_2 6}{5}
\approx0.4830074999.
\]

This is a much stronger entropy deficit than coefficient survival alone.

## 3. Match to the coefficient-only exclusion rate

The coefficient-only asymptotic rate used by the corrected Stage-4 front is

\[
\eta_{\rm coeff}
=1-H_2(\log_3 2)
\approx0.05004447281.
\]

Solving

\[
\eta_{HL}(\rho_*)
=
\eta_{\rm coeff}
\]

gives

\[
\boxed{
\rho_*
\approx0.5547058790629843.
}
\]

Therefore any aligned five-block language in which the low-block frequency satisfies

\[
\rho<\rho_*
\]

already has a dyadic entropy deficit **strictly stronger** than the coefficient-only deficit, even before adding the coefficient-prefix restrictions.

Selected values are

\[
\begin{array}{c|c}
\rho&\eta_{HL}(\rho)\\\hline
0&0.4830075\\
0.1&0.3468988\\
0.2&0.2540028\\
0.3&0.1798207\\
0.4&0.1195792\\
0.5&0.0714598\\
0.5547058791&0.05004447\\
0.6&0.0349601
\end{array}
\]

## 4. Revised deterministic/entropy split

This suggests a quantitatively explicit two-regime front.

### Regime A: sparse low-q events

If the low-block frequency is eventually below about \(55.47\%\), the binary language is already strongly entropy-sparse:

\[
\eta_{HL}\ge\eta_{\rm coeff}.
\]

This regime should be sent to the Haar/selector cross-base side, now with a substantially reduced dyadic language whenever \(\rho\) is well below the threshold.

### Regime B: dense low-q events

If the low-block frequency stays above the threshold, then more than about \(55.47\%\) of aligned blocks are in the only class where a negative local normalized penalty-minus-rebate is possible. This is the regime where deterministic min-plus transport and low-q expansion should be concentrated.

The split does not yet prove either branch globally. Its value is that the proof front no longer has to treat all coefficient-surviving tails with a single mechanism.

## 5. Remaining theorem pair

A complete closure along this route would require one of the following compatible pairs:

1. a cross-base overlap bound strong enough for Regime A together with a deterministic accumulated low-q transport bound for Regime B; or
2. a stronger renewal theorem that lowers the frequency threshold until the two estimates overlap automatically.

The current note supplies only the exact alphabet count and entropy budget.

Certificate:

`collatz/src/high_low_fiveblock_entropy_split_certificate.py`.
