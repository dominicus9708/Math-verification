# q<=8 phase-adaptive repeated-backtrace refinement at positive skew height

Date: 2026-08-25

Status: **exact finite local-minimality refinement** at the current m=44 R1 resonance.  It uses only root-globalized backtrace/headroom inequalities; no later-block L7 maximality assumption is used.  This does not prove the Collatz conjecture.

## 1. Why this refinement is valid after the L7 scope correction

The exact two-place minimality inequality is

\[
\mathcal B_Q(x_i)+h_i+\theta_i+
\log_2\!\left(1+\frac{c_i}{N}\right)>0.
\]

The previous phase-adaptive q<=8 window calculation applied its backtrace exclusion only when

\[
h_i=0.
\]

But the same root-headroom argument is valid at positive skew height.  For a q-odd-step inverse code of total binary exponent K, a sufficient condition for its positive ancestor to be strictly below the original root N is

\[
\boxed{
2^{K+h_i}
\left(\sup 2^{\theta_i}\right)
(3V_0+H)
<3^{q+1}V_0,
}
\]

where

\[
V_0=4\cdot3^{44}+2,
\qquad
H=137,528,045,312.
\]

The phase supremum is taken over the entire exact length-47 Sturmian factor cylinder, so every rejected state is uniformly impossible for every occurrence in that cylinder.

## 2. Exact implementation

The certificate

`collatz/src/q8_phase_adaptive_positive_height_window_certificate.cpp`

constructs from scratch:

- all 48 length-47 critical Sturmian factor cylinders;
- exact rational phase suprema on each cylinder;
- the minimum total inverse exponent K for every endpoint residue modulo 3^q, q<=8;
- the affine residue transition modulo 3^8=6561;
- skew-height transitions;
- the overlapping-window defect capacities.

As a regression test, restricting the filter to h=0 exactly reproduces the previous threshold

\[
26,909,266,900
\]

and its published capacity table.

## 3. Positive-height progression

Applying the same exact inequality at successively higher skew heights gives

\[
\boxed{
\begin{array}{c|r|c}
\text{backtrace filter heights}&r_*&r_*/H\\\hline
h=0&26,909,266,900&0.19566385051829158\\
h\le1&26,964,171,399&0.19606307453747576\\
h\le2&26,984,844,191&0.19621339145613116\\
h\le3&26,990,139,680&0.19625189624973880
\end{array}
}
\]

Extending the q<=8 phase-adaptive filter to h=4 leaves all capacities through j=18 and the global threshold unchanged.  Thus this particular q<=8 scalar-defect calculation saturates at h<=3.

The new universal defect floor is therefore

\[
\boxed{
\frac{r_*}{H}>0.19625189624973879,
}
\]

or more than

\[
\boxed{19.6251\%}
\]

of the odd-event coordinates.

## 4. Exact low-cost capacities at h<=3

The authoritative capacities are

\[
\begin{array}{c|r}
j&C_j\\\hline
0&48\\
1&917\\
2&8,670\\
3&54,571\\
4&261,464\\
5&1,039,208\\
6&3,648,409\\
7&11,816,396\\
8&36,190,638\\
9&106,028,242\\
10&298,905,312\\
11&814,856,327\\
12&2,157,844,802\\
13&5,569,902,294\\
14&14,050,583,911\\
15&34,717,893,182\\
16&84,199,143,072\\
17&200,713,077,167\\
18&470,710,868,104.
\end{array}
\]

At the preceding integer

\[
r=26,990,139,679,
\qquad
E=83,547,765,907,
\]

we have

\[
\Phi(E)=1,241,546,425,277
>
1,241,546,425,234=46r.
\]

At the threshold

\[
r=26,990,139,680,
\qquad
E=83,547,765,905,
\]

we have

\[
\Phi(E)=1,241,546,425,245
<
1,241,546,425,280=46r.
\]

Hence the threshold is exact.

## 5. Interpretation

The progression of unconditional repeated-minimality filters at the current resonance is now

\[
16.3833\%
\to18.5090\%
\to18.8429\%
\to19.1825\%
\to19.5663\%
\to\boxed{19.6251\%}.
\]

The last step is important conceptually even though it is numerically modest: the defect coordinate h is not merely a binary zero/nonzero label.  The 3-adic predecessor potential continues to delete states at positive height, exactly as predicted by the two-place inequality.

## 6. Why not continue scalar defect counting indefinitely

The h<=4 saturation shows that q<=8 has nearly exhausted what it can contribute after collapsing all surviving paths to the single statistic

\[
r_*=\#\{i:h_i>0\}.
\]

The next proof step should preserve more of the coupled quantity

\[
\boxed{
\mathcal B_Q(x_i)+h_i+\theta_i+
\log_2\left(1+\frac{c_i}{N}\right)
}
\]

rather than immediately replacing the full height/potential profile by one defect count.

Possible exact routes are:

1. a weighted incidence functional that assigns larger cost to low-height states with strongly negative backtrace potential;
2. a finite min-plus automaton whose edge cost is the surviving two-place margin;
3. a two-sided local-minimum automaton that combines root-globalized backtrace exclusion with forward no-descent information.

The current certificate establishes the numerical baseline against which any of these stronger aggregations must improve.
