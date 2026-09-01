# Archive and migration policy

The archive preserves rejected, superseded, and historical proof routes.  It is not a trash directory.

## Planned subroles

Future physical migration may create:

- `archive/rejected/` — mathematically invalid or over-promoted implications;
- `archive/search-rejected/` — valid mathematics rejected only as a long-search engine;
- `archive/superseded/` — older statements replaced by stronger canonical ones;
- `archive/history/` — chronological milestones no longer needed in the active navigation layer.

Git does not preserve empty directories, so these subdirectories should be created only when the first audited migration occurs.

## Phase-1 rule

No existing historical file is physically moved merely for neatness.

Reasons:

- Markdown notes cross-reference old paths;
- Python certificates may import legacy module names;
- GitHub/Zenodo/external references may point to existing paths;
- a move can damage reproducibility while changing no mathematics.

Instead, phase 1 creates canonical indexes and leaves chronological evidence in place.

## Migration record required for every moved file

Record:

1. old path;
2. new path;
3. classification (`REJECTED`, `SUPERSEDED`, `HISTORY`, etc.);
4. reason;
5. import/reference fixes made;
6. certificates rerun after the move;
7. canonical replacement, if any.

## Current rejected concepts to preserve when migration begins

- interval inclusion treated as correction-language membership;
- endpoint exposure treated as same-orbit connectivity;
- target adic mismatch treated as automatic membership rejection;
- multiplication of marginal residue/cardinality ratios without independence;
- terminal ternary saturation contradiction against a defect not visible at that resolution;
- unproved preservation of a complete C4F state by a local quotient;
- local carry greedy used to choose the global carry/cylinder sequence;
- uncompressed exact completion-defect DP used as the root-scale search engine.

## Supersession rule

A stronger result does not erase the dependency history of the weaker result.

If theorem B supersedes theorem A:

- A remains historically valid in its original domain;
- canonical navigation points to B;
- any computation certified using A remains documented as using A unless rerun with B;
- B is not applied retroactively to change the interpretation of old finite outputs.

## Safe physical migration sequence

1. finish the current canonical indexing layer;
2. generate a reference/import inventory;
3. migrate Markdown-only files with redirects/index updates first;
4. convert `src/` into an explicit Python package if needed;
5. migrate Python certificates by coherent dependency groups, not one by one;
6. rerun all affected certificates;
7. update PR documentation and canonical indexes.

Until those steps occur, the legacy `notes/` and `src/` directories remain authoritative evidence locations while the new role directories provide authoritative navigation/classification.
