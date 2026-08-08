# Resonance-core logarithmic bound

## Setup

For a first coefficient crossing with q odd terms, let

- sigma(q) = ceil(q log_2 3),
- M = 2^sigma,
- P = 3^q,
- D = M - P > 0.

Define the dangerous-coordinate count

h(q) = #{1 <= i <= q : 3^(q-i) >= D}.

Equivalently,

h(q) = q - ceil(log_3 D).

## Exact resonance formula

Let

theta_q = sigma(q) - q log_2 3,  with 0 < theta_q < 1.

Then

D = 2^sigma - 3^q
  = 3^q (2^theta_q - 1).

Hence

h(q)
= q - ceil(q + log_3(2^theta_q - 1))
= floor(-log_3(2^theta_q - 1)).

Thus h(q) depends only on the one-sided Diophantine approximation error theta_q. Large dangerous dimension occurs exactly at near-resonances where q log_2 3 lies unusually close below an integer.

## Rhin-derived global logarithmic bound

Rozier and Terracol (arXiv:2502.00948v5, Proposition 6.3) quote Rhin's effective irrationality estimate

|j ln 2 - q ln 3| >= j^(-13.3),

for j >= 2 in the specialization u0=0, u1=j, u2=-q.

At first coefficient crossing j=sigma,

Lambda = sigma ln 2 - q ln 3 = theta_q ln 2 > 0.

Also

2^theta_q - 1 = exp(Lambda) - 1 >= Lambda >= sigma^(-13.3).

Therefore

h(q)
= floor(-log_3(2^theta_q - 1))
<= floor(13.3 log_3 sigma).

So the dangerous coordinate dimension is globally O(log sigma), not merely O(q).

This is a derived consequence of the previously established dangerous-coordinate criterion plus Rhin's published lower bound; it is not claimed as an existing Collatz theorem in the literature.

## Exact computational records

Wolfram exact-arithmetic scan through q <= 100000 gave record increases

(q,h) =
(1,1),
(5,2),
(29,3),
(41,4),
(253,5),
(306,6),
(8951,7),
(13606,8),
(15601,9),
(47468,10),
(79335,11).

These record locations are associated with unusually good upper approximations of log_2 3, consistent with the exact theta_q formula.

## Matrix / tensor implication

If the proposed Dangerous-Core Extremal Reduction (DCER) is proved, all safe coordinates can be analytically contracted and only h(q) coordinates need remain in the explicit transfer object.

Since h(q)=O(log sigma), any exponential-in-h core representation becomes polynomial in sigma. For example, the crude universal bound 4^h gives

4^h <= sigma^(13.3 log_3 4),

with exponent approximately 16.78.

The actual admissibility transfer matrix is much smaller than this crude worst-case bound at observed h.

## Status

Proved/derived:
- exact h(q) resonance formula;
- Rhin-based logarithmic upper bound, conditional only on the cited published inequality;
- exact record scan through q=100000.

Still unproved:
- DCER: safe-tail contraction preserves the extremal representative needed for the CST/FCS decision;
- any global Collatz conclusion from the logarithmic core bound alone.
