# Short-record ballot lower bound

Date: 2026-08-21

Status: **analytic lower bound for short Beatty record excursions.** This closes the short-record side of the record-measure information estimate. It does not prove the final selector/Hensel splice and does not prove the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_k=\lceil \alpha k\rceil,
\qquad
D_s(j)=b_{s+j}-b_s.
\]

A record first-passage word of length \(L\) at record height \(r\) has strip coordinate

\[
y_j=D_s(j)-q_j
\]

satisfying

\[
0\le y_j\le r\quad(j<L),
\qquad y_L=-1.
\]

Under Bernoulli\((\alpha)\) parity bits, write

\[
X_j=\varepsilon_1+\cdots+\varepsilon_j,
\qquad
W_j=\alpha j-X_j.
\]

Then \(W\) is a mean-zero finite-variance lattice random walk with increments \(\alpha\) and \(\alpha-1\).

## 1. Uniform bounded connectors

The mechanical word

\[
d_j=b_{s+j}-b_{s+j-1}\in\{0,1\}
\]

has no factor `00` and no factor `111`.

Indeed the one-slack identity gives

\[
D_s(2)\ge b_2-1=1
\]

and

\[
D_s(3)\le b_3=2.
\]

Hence, uniformly in phase:

- two mechanical rises occur within at most four steps;
- a mechanical plateau occurs at least once in every three steps.

Starting at \(y=0\), use parity equal to the mechanical bit except make parity even at the first two mechanical rises. This reaches the safe interior state \(y=2\) in at most four steps without leaving the strip.

At the other end, if a record exit is possible then the final mechanical bit is a plateau. Using the last three preceding plateaus, one can move monotonically from \(y=3\) to \(y=0\), then use the final plateau-odd step to exit through \(y=-1\). The total exit connector length is bounded by an absolute constant.

All connector bits therefore cost only a fixed positive Bernoulli factor depending on \(\alpha\).

## 2. Ballot event in the middle

Let the middle interval have length \(n=L-O(1)\), starting at strip state \(y=2\). Put

\[
D=D_a(n)=b_{a+n}-b_a
\]

for the corresponding mechanical phase \(a\). Choose the endpoint odd count

\[
\boxed{X_n=D-1.}
\]

Then the middle endpoint strip state is exactly

\[
y_{\rm out}=2+D-X_n=3.
\]

Also

\[
W_n=\alpha n-X_n
=1-(D-\alpha n).
\]

Since the mechanical one-slack estimate gives

\[
|D-\alpha n|<1,
\]

we have the uniform endpoint range

\[
\boxed{0<W_n<2.}
\]

If

\[
W_j>0\qquad(0<j<n),
\]

then

\[
y_j
=2+D_a(j)-X_j
=2+(D_a(j)-\alpha j)+W_j
>1,
\]

so the path never crosses the upper record boundary \(y=0\).

## 3. Finite-variance ballot lower bound

Addario-Berry and Reed, `Ballot theorems for random walks with finite variance` (arXiv:0802.2491), prove that for a mean-zero positive finite-variance random walk, uniformly for positive endpoints \(k=O(\sqrt n)\),

\[
\Pr(W_j>0\ \forall 0<j<n\mid W_n=k)
=\Theta(k/n).
\]

Here \(k=W_n\in(0,2)\) is uniformly bounded away from the diffusive scale. The lattice local central limit theorem gives

\[
\Pr(W_n=k)=\Theta(n^{-1/2})
\]

uniformly over the two possible lattice endpoints in that compact range. Therefore there is \(c_0(\alpha)>0\) such that

\[
\boxed{
\Pr_\alpha
\bigl(W_j>0\ (0<j<n),\ X_n=D-1\bigr)
\ge c_0 n^{-3/2}.
}
\]

## 4. The lower strip wall is negligible for short records

The remaining requirement is \(y_j\le r\). Since

\[
y_j<3+W_j,
\]

it is enough that

\[
\max_{j\le n}W_j<r-3.
\]

The increments of \(W\) have range length one, so the maximal Hoeffding inequality gives

\[
\Pr\left(\max_{j\le n}W_j\ge r-3\right)
\le
\exp\left(-c\frac{(r-3)^2}{n}\right).
\]

Fix any \(A<\infty\) and assume

\[
L\le Ar.
\]

Then \(n\le Ar+O(1)\), hence

\[
\Pr\left(\max W_j\ge r-3\right)
\le e^{-c_A r},
\]

which is eventually smaller than half of \(c_0n^{-3/2}\).

After restoring the bounded connectors, there are constants \(c_A>0\) and \(r_A,L_A\) such that every nonempty short record language with

\[
r\ge r_A,
\qquad
L_A\le L\le Ar
\]

satisfies

\[
\boxed{
P_\alpha(\mathcal R_{s,r}(L))
\ge
c_A L^{-3/2}.
}
\]

The constants are uniform in the mechanical phase \(s\).

## 5. Information consequence

With

\[
K_\alpha(\mathcal R)
=-\ln P_\alpha(\mathcal R),
\]

we obtain

\[
\boxed{
K_\alpha(\mathcal R)
\le
\frac32\ln L+O_A(1)
\qquad(L\le Ar).
}
\]

Hence any sequence of short record excursions with \(r\to\infty\) and \(L\to\infty\) has

\[
\boxed{
K_\alpha/L\to0.
}
\]

Combined with the long-record loop bound, this will imply the same conclusion for **every** record sequence whose lengths tend to infinity, with no restriction on the ratio \(L/r\).

Companion finite regression:

`collatz/src/short_record_ballot_certificate.py`.
