# Install Pratice Code

1. Install Python **3.10 or newer** once. No Node.js, npm, account or paid service is required.
2. Download the repository ZIP or the full offline ZIP and **extract the complete folder**.
3. On Windows, double-click **Install and Start.cmd**. On macOS/Linux, run `python3 install.py` from that folder, or `sh start.sh`.
4. Your browser opens **http://127.0.0.1:8787/**. The internet can be disconnected. Keep the folder and local server available while using the site.

The installer checks the folder and opens the site; it does not download software or change system settings. `python install.py --check` runs the check without opening a browser. `python launch.py --stop` stops the app.

Included offline: courses, notes, quizzes, interviews, mock sessions, the question/reference library, PDF books, Monaco editing, Python, JavaScript, SQLite and HTML/CSS/JavaScript previews. Optional C/C++ and Java execution needs an installed local compiler/JDK; those languages never fall back to a cloud compiler in this edition. Their reference code remains readable without a compiler. External source links open online only when you choose them.

Progress is private to your browser and local folder. Use **Progress → Back up all progress** before moving to another computer, and restore the JSON there. Downloaded application ZIPs intentionally omit personal notes, answers and progress.

To import your own files, copy `import_sources.example.json` to `import_sources.json`, enter your local folder paths, then run `python merge_packs.py`. Bundled study content works without the original source folders.
