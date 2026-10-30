"""Build the self-contained Windows x64 installer using Microsoft's local C# compiler.

Only --download-runtime uses the internet. Installation and app execution do not.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, zipfile
from pathlib import Path
from urllib.request import urlopen
from package_offline import package

ROOT=Path(__file__).resolve().parent
VERSION='1.1.0'
RUNTIME_URL='https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-amd64.zip'
RUNTIME_SHA256='90905e64a840557d8c1bc4f5b74db3d7ee85e3ffb217611cac1c7813acea4159'

def build(runtime_zip,download=False):
    if os.name!='nt':raise RuntimeError('Build this Windows installer on Windows.')
    build_root=ROOT/'build/windows';build_root.mkdir(parents=True,exist_ok=True)
    runtime_zip=Path(runtime_zip) if runtime_zip else ROOT/'build/cache/python-3.14.10-embed-amd64.zip'
    if not runtime_zip.exists():
        if not download:raise RuntimeError('Supply --runtime-zip or use --download-runtime once.')
        runtime_zip.parent.mkdir(parents=True,exist_ok=True)
        with urlopen(RUNTIME_URL,timeout=60) as response:runtime_zip.write_bytes(response.read())
    actual=hashlib.sha256(runtime_zip.read_bytes()).hexdigest()
    if actual!=RUNTIME_SHA256:raise RuntimeError('Official Python runtime SHA-256 verification failed.')
    runtime=build_root/'runtime';runtime.mkdir(exist_ok=True)
    with zipfile.ZipFile(runtime_zip) as archive:archive.extractall(runtime)
    (runtime/'python314._pth').write_text('python314.zip\n.\n..\n',encoding='utf-8')
    csc=Path(os.environ.get('WINDIR','C:/Windows'))/'Microsoft.NET/Framework64/v4.0.30319/csc.exe'
    if not csc.is_file():raise RuntimeError('Microsoft .NET Framework C# compiler is required to build the installer.')
    launcher=build_root/'Pratice Code.exe'
    common=[str(csc),'/nologo','/target:winexe','/platform:x64','/optimize+','/reference:System.Windows.Forms.dll','/reference:System.Drawing.dll']
    subprocess.run(common+['/out:'+str(launcher),str(ROOT/'windows/Launcher.cs')],check=True)
    extras={'Pratice Code.exe':launcher}
    for f in runtime.rglob('*'):
        if f.is_file():extras['runtime/'+f.relative_to(runtime).as_posix()]=f
    output=ROOT/'downloads';output.mkdir(exist_ok=True)
    payload=output/'Pratice-Code-Windows-Portable.zip'
    report=package(payload,extras)
    installer=output/'Pratice-Code-Setup.exe'
    subprocess.run(common+['/reference:System.IO.Compression.dll','/reference:System.IO.Compression.FileSystem.dll','/resource:'+str(payload)+',PraticeCode.Payload','/out:'+str(installer),str(ROOT/'windows/Installer.cs')],check=True)
    digest=hashlib.sha256(installer.read_bytes()).hexdigest()
    (output/'Pratice-Code-Setup.sha256').write_text(digest+'  Pratice-Code-Setup.exe\n',encoding='ascii')
    report.update(installer=str(installer),installerMiB=round(installer.stat().st_size/1048576,2),sha256=digest,runtime='Python 3.14.10 x64',version=VERSION)
    (output/'windows-build.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report),flush=True)
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--runtime-zip');parser.add_argument('--download-runtime',action='store_true');args=parser.parse_args()
    build(args.runtime_zip,args.download_runtime)
