# Legacy executable certificate/source layer

This directory remains the physical location of the current Collatz Python certificates during reorganization phase 1.

Canonical classification is now maintained in:

- `../certificates/README.md` — certificate roles and execution policy;
- `../theorems/README.md` — mathematical theorem roles;
- `../audits/README.md` — DSD audit roles;
- `../frontier/A0_S1_ROUTEB.md` — active computation.

## Why files are not moved yet

Many certificates import neighboring modules directly.  Moving a file for cosmetic organization can therefore break another certificate or make a historical note irreproducible.

Until the import/reference migration audit is complete:

- keep existing Python filenames and paths stable;
- new certificates may still be placed here when they depend on the current flat import layout;
- immediately classify any new canonical certificate in `../certificates/README.md` or the active frontier;
- do not infer theorem status from the presence of a `PASS` print statement.

## Execution-status distinction

A source file can be:

1. committed but not executed in the current environment;
2. executed;
3. independently cross-checked;
4. associated with an algebraically closed theorem.

These are distinct states.

## Future migration

Physical migration to `../certificates/` will occur by dependency groups after:

- import inventory;
- Markdown path-reference inventory;
- package/import repair;
- rerun of affected certificates.

See `../archive/README.md` and `../certificates/README.md` for the migration policy.
