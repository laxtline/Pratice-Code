"""Task-local GitHub API helper. Credentials remain in memory via Git Credential Manager."""
import argparse, json, os, subprocess, sys, urllib.request, urllib.error
from pathlib import Path

REPO = 'laxtline/Pratice-Code'

def credential():
    result = subprocess.run(['git', 'credential', 'fill'], input='protocol=https\nhost=github.com\n\n', text=True, capture_output=True,
                            env={**os.environ, 'GIT_TERMINAL_PROMPT':'0', 'GCM_INTERACTIVE':'never'})
    fields = dict(line.split('=',1) for line in result.stdout.splitlines() if '=' in line)
    token = fields.get('password')
    if not token:
        raise RuntimeError('No saved GitHub credential is available. Sign in to GitHub first.')
    return token

def request(token, path, method='GET', data=None, binary=None):
    url = path if path.startswith('https://') else 'https://api.github.com' + path
    headers = {'Authorization':'Bearer '+token, 'Accept':'application/vnd.github+json', 'X-GitHub-Api-Version':'2022-11-28', 'User-Agent':'Pratice-Code-Publisher'}
    if binary is not None:
        body = Path(binary).read_bytes(); headers['Content-Type'] = 'application/octet-stream'
    elif data is not None:
        body = json.dumps(data).encode(); headers['Content-Type'] = 'application/json'
    else:
        body = None
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=headers, method=method), timeout=600) as response:
            raw = response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        detail = error.read().decode(errors='replace')[:1200]
        raise RuntimeError(f'GitHub HTTP {error.code}: {detail}') from None

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('action', choices=['inspect','metadata','pages','status','release','upload']); parser.add_argument('--sha'); parser.add_argument('--file'); args=parser.parse_args()
    token=credential(); root='/repos/'+REPO
    if args.action=='inspect':
        user=request(token,'/user'); repo=request(token,root)
        print(json.dumps({'login':user['login'],'permissions':repo.get('permissions'),'default_branch':repo['default_branch'],'homepage':repo.get('homepage')}))
        releases=request(token,root+'/releases'); print(json.dumps({'releases':[{k:r.get(k) for k in ('id','tag_name','name','draft','html_url')}|{'assets':[{k:a.get(k) for k in ('id','name','size')} for a in r['assets']]} for r in releases]}))
        try: print(json.dumps({'pages':request(token,root+'/pages')}))
        except RuntimeError as e: print(str(e))
    elif args.action=='metadata':
        repo=request(token,root,'PATCH',{'description':'Coding practice, courses, exams and a complete study library. Use the live website or download the offline Windows app.','homepage':'https://laxtline.github.io/Pratice-Code/'})
        request(token,root+'/topics','PUT',{'names':['coding-practice','python','javascript','placement-preparation','offline-first','windows-app','study-material','github-pages']})
        print(json.dumps({k:repo.get(k) for k in ('html_url','homepage','description')}))
    elif args.action=='pages':
        try: current=request(token,root+'/pages')
        except RuntimeError as e:
            if 'HTTP 404' not in str(e): raise
            current=None
        result=request(token,root+'/pages','PUT' if current else 'POST',{'build_type':'workflow'})
        print(json.dumps(result))
    elif args.action=='status':
        runs=request(token,root+'/actions/runs?per_page=5')
        print(json.dumps({'runs':[{k:r.get(k) for k in ('id','name','head_sha','status','conclusion','html_url')} for r in runs['workflow_runs']]}))
        try: print(json.dumps({'pages':request(token,root+'/pages')}))
        except RuntimeError as e: print(str(e))
    elif args.action=='release':
        data={'tag_name':'v1.2.0','target_commitish':args.sha or 'main','name':'Pratice Code 1.2.0 — Windows app and live website','body':Path(args.file).read_text(encoding='utf-8'),'draft':False,'prerelease':False,'make_latest':'true'}
        try: release=request(token,root+'/releases/tags/v1.2.0')
        except RuntimeError as e:
            if 'HTTP 404' not in str(e): raise
            release=None
        result=request(token,root+'/releases'+('/'+str(release['id']) if release else ''),'PATCH' if release else 'POST',data)
        print(json.dumps({k:result.get(k) for k in ('id','html_url','tag_name','upload_url')}))
    elif args.action=='upload':
        import hashlib, urllib.parse
        release=request(token,root+'/releases/tags/v1.2.0'); file=Path(args.file)
        for asset in release['assets']:
            if asset['name']==file.name:
                digest='sha256:'+hashlib.file_digest(file.open('rb'),'sha256').hexdigest()
                if asset.get('digest')==digest:
                    print(json.dumps({'already_uploaded':True,'name':file.name,'browser_download_url':asset['browser_download_url']})); return
                raise RuntimeError('A different asset with this name already exists; refusing to replace it automatically.')
        url=release['upload_url'].split('{')[0]+'?name='+urllib.parse.quote(file.name)
        result=request(token,url,'POST',binary=file)
        print(json.dumps({k:result.get(k) for k in ('id','name','size','digest','browser_download_url','state')}))

if __name__=='__main__':
    try: main()
    except Exception as error: print(str(error),file=sys.stderr); sys.exit(1)
