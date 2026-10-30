# Verification

- 13 Python integration and merge tests pass: server APIs, accepted/wrong/error/timeout results, shared saving, backup and restore, deduplication, compressed catalog refresh and offline runtime files.
- 6 JavaScript tests pass: unified index matching, solution deduplication, saved progress preservation, graded exercise links, shared revision routing, and the browser function runner.
- Library audit: 4,097 imported questions, 14,652 resource records and 33,160 solution variants; no broken local records were found.
- Interactive browser checks cover the unified home, Coding Lab, courses, exams, practice search, question reader and solutions, progress, and deep-link reload. Python, JavaScript and SQLite run using bundled/local engines.
- The portable archive is CRC-checked. A clean extraction is checked with `install.py --check`, then served on a temporary loopback port to verify its home, catalog, question data, worker and offline runtime assets.

Python 3.10+ must already be installed. Node.js is only used to run development tests; it is not required by the app. C/C++ and Java require an optional local compiler/JDK. Automatic reference judging is available for the included 22 local function suites, with additional input/output exercises in Practice. Other reference entries support reading, custom runs and self-assessed progress.
