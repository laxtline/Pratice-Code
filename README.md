# Pratice Code

Complete Windows desktop application and local website for coding practice, courses, exams, interviews and study materials.

## Downloads

- [Windows installer — Pratice-Code-Setup.exe](https://github.com/laxtline/Pratice-Code/releases/latest/download/Pratice-Code-Setup.exe)
- [Offline website ZIP](https://github.com/laxtline/Pratice-Code/releases/latest/download/Pratice-Code-Offline.zip)
- [Release notes and checksums](https://github.com/laxtline/Pratice-Code/releases/latest)
- [Live website](https://laxtline.github.io/Pratice-Code/)
- [Windows installer package](https://github.com/laxtline/Pratice-Code/packages)

## Complete project layout

| Folder | Contents |
| --- | --- |
| `App/` | Portable desktop app, bundled Python, fixed WebView2 runtime, source and study collection |
| `Installer/` | Windows setup executable, checksum and build record |
| `Website/` | Complete local website, source, study collection and bundled Python |
| `Publish/` | Offline website archive, checksums and release notes |

Run `OPEN_APP.cmd` to open the portable app, or `OPEN_WEBSITE.cmd` to start the local website. Read `Start.pdf` for instructions. The installer includes the required runtimes.

## Clone the complete project

Large installer/runtime files use Git LFS. Install Git LFS before cloning, then run:

```sh
git lfs install
git clone https://github.com/laxtline/Pratice-Code.git
cd Pratice-Code
git lfs pull
```

GitHub source ZIP downloads can contain LFS pointer files. Use the Release installer for a ready-to-run Windows download.

The repository mirrors the collected local project. Personal progress, private browser data, logs and caches are excluded. `PROJECT-FILES.json` records the included file hashes and excluded paths. Original application notices are in `App/THIRD_PARTY.md`, `Website/THIRD_PARTY.md` and their `third_party_notices/` folders.

## GitHub Packages

`Pratice.Code.Windows` packages the same verified Windows installer under `tools/Pratice-Code-Setup.exe` in the NuGet format supported by GitHub Packages. The direct EXE download is available in Releases. The publishing workflow verifies its SHA-256 before packaging.
