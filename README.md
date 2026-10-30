# Pratice Code

One offline website for learning, coding, practice, assessments and your complete study collection.

## Open it

**Windows app:** download **Pratice-Code-Setup.exe** from [Releases](https://github.com/laxtline/Pratice-Code/releases). Run it, choose an install folder, then open the **Pratice Code** shortcut. The installer includes its own Python runtime and the complete study collection; no separate Python or Node installation is needed. A Windows portable ZIP with the same runtime is also available. Both work without internet after download.

Double-click **Install and Start.cmd** (or **Start Pratice Code.cmd** after the first check). Open **http://127.0.0.1:8787/**. Keep the complete project folder together. Python 3.10+ is required; Node.js, npm and an internet connection are not required. **Stop Pratice Code.cmd** stops the local website.

## One application

The home page and the single top menu cover:

- **Coding Lab:** Monaco editing, Python, JavaScript, real SQLite, HTML/CSS/JS preview, saved snippets, file import/export and run history.
- **Practice:** local function-test suites and the retained judged input/output exercises. Equivalent question titles link their graded exercises and reference versions together.
- **Learn:** 30 courses, 145 lessons, worked examples, quizzes, notes and 446 interview answers from the retained curriculum.
- **Exams:** coding rounds, aptitude/written tests, coding challenges, SQL assessments, cognitive drills, interview prompts and company preparation.
- **Library:** 4,097 imported question records merged with the older reference collection; additional older topics remain available. All 14,652 preparation files and books are included. Search by title/topic, company, difficulty, file type and progress. Source versions and reference implementations open in the same reader.
- **Library → Level wise:** three preparation tracks based on the included Service-Based, Product/Fintech/Finance and Top-Tier Product PDF guides. Filter matching questions by topic, difficulty and progress; open the source PDF offline. Questions reuse their existing IDs, notes, solutions and progress across tracks. The guides contain topic priorities and typical examples, not exhaustive or guaranteed company question lists.
- **Progress:** coding, learning and reference practice in one place, including shared spaced revision and **Back up all progress / Restore progress**.

The main website uses one document and the same editor/learning engines. It does not embed the old websites in a second app frame. Browser history, deep links and a single navigation work across sections.

## Reading and running code

Open a reference question to read it, inspect solutions, edit your draft, keep notes and run code in the same page. The 22 included local function suites support Python and JavaScript. Other reference entries support custom function arguments and self-assessed progress. A reference implementation alone does not establish an automatically judged exercise. Local suites do not submit to an external platform or test every possible input.

Questions with a matching original input/output exercise show **Open input/output exercise** in the reader. The retained native exercise engine, exam sessions, scores and reference answers work as before. C/C++ and Java use an installed local compiler/JDK; missing compilers are labeled. This edition never sends code to a cloud compiler. External reference links are optional online sources.

## Saved work

The unified application uses the retained browser autosave and private folder backup at `studio-private/.codelab-data/progress.json`. Imported reference drafts, language choices, notes, bookmarks, attempts and revision join this same backup format. Existing personal records from the earlier question website migrate once without overwriting matching notes or drafts already present.

Choose **Progress → Back up all progress** to export one JSON backup containing the whole workspace. Restore through the same screen. Backups exclude compiler API credentials. Browser-only work from another origin/browser still needs its previous export/import controls.

The earlier `data/user-state.json` remains available for migration and compatibility. The importer does not erase it. Personal progress, private folder backups, import caches and logs are excluded from Git and from portable ZIP files.

## Add more material

Configure local folders in `import_sources.json`, then double-click **Merge New Files.cmd**. Refresh the website after the import. Matching links, numbers and titles are merged; identical files and implementations are skipped. Source paths and language variants stay with their records. Imported programs are not executed by the importer.

All usable content is copied into this project. The original Downloads folders are unnecessary for ordinary offline use. Company-sheet statistics remain historical snapshots dated 12 July 2025. Some older pre-existing renamed question IDs remain compatible with saved links.

## Portable package

Run `python package_offline.py` to build and verify `downloads/Pratice-Code-Offline.zip`. Extract the entire ZIP and use its launcher. The folder includes local Python/Pyodide, SQLite and Monaco browser engines and the complete study collection. Internet can be disconnected; the local launcher must stay running for library and code-runner APIs.

## Checks

- `python -m unittest test_server test_merge -v`: server, judging, wrong-answer/error/timeout behavior, shared saving, backup/restore, duplicate handling, compressed catalog reload, runtime files and inline script parsing.
- `node --test test_unified.cjs`: combined collection matching, implementation deduplication, preservation of saved status and bookmarks, graded-exercise linking, and reference practice in the shared revision system.
- The Windows installer is tested in a separate folder using only its bundled runtime, including launching/stopping its executable and submitting a Python practice solution.
- The home page, editor execution, courses, assessments, library, reference question workspace and deep-link reload are checked through the browser.

## Sources and notices

The original editor/study modules and their license notices remain under `web/studio/`, including its `vendor/` and `offline/licenses/` folders. Source and solution origins remain attached to imported records. Original project folders are retained separately. The app is a personal offline learning workspace; it does not install account-unlocking extensions or use an external platform login.

Additional collection notices and source information are listed in [THIRD_PARTY.md](THIRD_PARTY.md).

Local code runs with your computer account permissions and execution limits. The server listens only on 127.0.0.1. It is intended for personal use, not public multi-user hosting.

For installation on another computer, follow [INSTALL.md](INSTALL.md). On macOS/Linux run `python3 install.py` or `sh start.sh`. No original Downloads folders or saved browser data are required.

## Build the Windows installer

On Windows, run `python build_windows.py --download-runtime` once, or pass `--runtime-zip` with the official Python 3.14.10 x64 embeddable ZIP. The pinned SHA-256 is verified before packaging. The build uses Microsoft's local .NET Framework C# compiler and writes `downloads/Pratice-Code-Setup.exe`, `Pratice-Code-Windows-Portable.zip` and a checksum. No build tools or downloads are needed by the person installing the finished app. Python's original license is included with its bundled runtime.
