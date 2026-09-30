"""Offline SHA-256 manifest. AI-assisted scaffold; not candidate execution evidence."""
import argparse, hashlib, json
from pathlib import Path

def manifest(root):
    rows=[]
    for p in sorted(root.rglob('*')):
        if p.is_symlink() or not p.is_file(): continue
        h=hashlib.sha256()
        with p.open('rb') as f:
            for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
        rows.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':h.hexdigest()})
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('directory',type=Path)
    args=parser.parse_args()
    if not args.directory.is_dir(): parser.error('directory must exist')
    print(json.dumps(manifest(args.directory),indent=2))
# Redirect the output outside the directory being hashed to avoid hashing a partial manifest.
