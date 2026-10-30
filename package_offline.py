"""Package the working combined folder with its offline engines and public content."""
import json, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
output=ROOT/'downloads'/'Pratice-Code-Offline.zip'
output.parent.mkdir(exist_ok=True)
SKIP={'downloads','backups','__pycache__','.git','studio-private','node_modules'}
EXCLUDE={'user-state.json','user-state.json.tmp','imported-files.json','import_sources.json','.github-publish-state.json','server.log'}
files=[]
def public_metadata(value):
    if isinstance(value,dict):
        return {key:({Path(folder.replace('\\','/')).name:public_metadata(report) for folder,report in item.items()} if key=='additionalImports' and isinstance(item,dict) else public_metadata(item)) for key,item in value.items()}
    if isinstance(value,list):return [public_metadata(item) for item in value]
    return value
for file in ROOT.rglob('*'):
    rel=file.relative_to(ROOT)
    if not file.is_file() or any(part in SKIP for part in rel.parts) or file.name in EXCLUDE or file.name.endswith(('.log','.merge-tmp')):continue
    files.append(file)
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=5) as archive:
    for file in sorted(files):
        relative=file.relative_to(ROOT).as_posix();name='Pratice-Code-Offline/'+relative
        if relative in ('data/catalog.json','data/import-report.json'):
            archive.writestr(name,json.dumps(public_metadata(json.loads(file.read_text(encoding='utf-8'))),ensure_ascii=False,separators=(',',':')))
        else:archive.write(file,name)
with zipfile.ZipFile(output) as archive:
    invalid=archive.testzip()
    if invalid:raise SystemExit('Archive verification failed: '+invalid)
print(json.dumps({'archive':str(output),'files':len(files),'sizeMiB':round(output.stat().st_size/1048576,2),'verified':True}))
