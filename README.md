# Protoporphyrin Effects Boosting

A source-grounded research wiki beginning with Danielius Vargonas's Vilnius University biophysics master's thesis on ascorbic acid, protoporphyrin IX (PpIX), albumin and pH.

Start at the [wiki index](wiki/index.md). The [research overview](wiki/thesis/research-overview.md) explains the original question and the [experimental design](wiki/thesis/experimental-design.md) records the conditions needed to interpret the findings.

## Evidence and maintenance

- `raw/` contains immutable original documents and faithful text extracts. Original thesis files were relocated here without changing their bytes; presentation variants remain separate sources.
- `wiki/` contains English synthesis, relative source links, explicitly qualified interpretations and an append-only [operation log](wiki/log.md).
- `raw/manifest.json` pins source bytes with SHA-256 hashes. Add newly collected sources to the manifest; do not replace old snapshots when a website changes.
- Run `python scripts/check_wiki.py` to check source hashes, local links, article metadata and index coverage. This checks structure and integrity, not scientific truth.

Text extraction preserves the Lithuanian source wording. Word field instructions were removed while retaining displayed field results; table cells are separated by ` | `, and embedded figures are marked rather than reconstructed. Original binaries remain authoritative for figures, equations and layout. PDF extraction and presentation XML extraction have their own reading-order limitations.

The original work is exploratory solution photochemistry. Its spectral assignments and biological motivation should not be read as evidence of clinical benefit or as treatment instructions.
