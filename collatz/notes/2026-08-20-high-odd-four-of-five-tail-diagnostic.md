# High-odd four-of-five tail diagnostic

Date: 2026-08-20

Status: **finite exact diagnostic for the remaining high-odd-density obstruction.** This is not an asymptotic theorem and not a proof of the Collatz conjecture.

## 1. Why isolate this sublanguage

The five-block self-prepend theorem proves that every admissible block with

\[
q_w\ge4
\]

has nonnegative exact normalized syndrome penalty minus correction rebate. It therefore cannot create the local loss that occurs in some \(q_w\le3\) blocks.

The unresolved extreme case is consequently a tail dominated by blocks having at least four odd steps out of every aligned five steps. Such a tail has aligned block odd density at least

\[
\frac45=0.8,
\]

which is much larger than the coefficient threshold

\[
\alpha=\log_3 2\approx0.63093.
\]

This is a useful structural split, but high odd density by itself is not a known pointwise contradiction for a hypothetical divergent Collatz orbit. Classical parity-density results give the lower-density condition required by divergence; they do not exclude an individual orbit whose odd density is substantially larger.

## 2. Exact finite profile

Let \(H(K)\) be the least positive canonical start whose first \(K\) parity steps, grouped into aligned five-step blocks, have at least four odd steps in every complete block.

An exact best-first parity-cylinder search gives

\[
\begin{array}{c|r}
K&H(K)\\\hline
5&7\\
10&27\\
15&111\\
20&111\\
25&4591\\
30&4591\\
35&4591\\
40&1509545\\
45&6574831\\
50&8555497\\
55&60533863\\
60&180121343\\
65&3994690279\\
70&34406735401\\
75&129821427871
\end{array}
\]

The growth is very strong in this finite window. In particular,

\[
\boxed{H(75)=129821427871.}
\]

However, the plateaus at \(K=15\to20\) and \(K=25\to35\) are a warning against inferring a uniform exponential lower bound from the table alone.

## 3. Interpretation

For any fixed integer \(N<H(K)\), the first \(K\) accelerated parity steps of \(N\) cannot belong to this four-of-five sublanguage.

Thus the finite profile gives a strong exact exclusion of long high-odd tails below the recorded thresholds. It does **not** prove

\[
H(K)\to\infty.
\]

That asymptotic statement would already exclude a positive integer whose aligned five-block tail has at least four odd steps forever, and therefore must not be assumed from finite data.

## 4. Relation to the current sparse-tail split

The deterministic Stage-4 sparse-tail obstruction now separates into two regimes:

1. **low-q boundary events** \((q_w\le3)\), where negative normalized penalty-minus-rebate can occur but where the new floor-16 and terminal-layer lemmas control the small-value pathology;
2. **high-q tail events** \((q_w\ge4)\), where self-prepend contraction forces
   \[
   P_w-E_w\ge0,
   \]
   while the remaining pointwise question is whether a positive integer can sustain that high-odd sublanguage indefinitely.

The second regime is therefore the next exact target. A successful theorem must upgrade the finite growth of \(H(K)\) to a genuine divergence statement or derive an equivalent renewal obstruction. No such upgrade is claimed here.

Certificate:

`collatz/src/high_odd_four_of_five_minimal_residue.cpp`.
