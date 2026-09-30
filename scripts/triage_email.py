"""Offline .eml parsing only. No network, rendering, attachment execution or verdict."""
import argparse, hashlib, json, re
from pathlib import Path
from email import policy
from email.parser import BytesParser

def defang(s):
    return re.sub(r'^https?', lambda m: 'hxxps' if m.group(0).lower() == 'https' else 'hxxp', s, flags=re.I).replace('.', '[.]')

def triage(path):
    if path.stat().st_size > 25*1024*1024: raise ValueError('Sample exceeds 25 MiB')
    raw=path.read_bytes(); msg=BytesParser(policy=policy.default).parsebytes(raw)
    headers={k:msg.get_all(k,[]) for k in ['From','To','Subject','Reply-To','Return-Path','Message-ID','Date','Received','Authentication-Results']}
    urls=set(); attachments=[]
    for part in msg.walk():
        if part.is_multipart(): continue
        data=part.get_payload(decode=True) or b''
        filename=part.get_filename()
        if filename is not None or part.get_content_disposition()=='attachment':
            attachments.append({'name':filename,'type':part.get_content_type(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
            continue
        if part.get_content_type() in ['text/plain','text/html']:
            text=data.decode(part.get_content_charset() or 'utf-8',errors='replace')
            urls.update(re.findall(r'https?://[^\s<>"\x27]+',text,flags=re.I))
    return {'source_sha256':hashlib.sha256(raw).hexdigest(),'headers':headers,'urls_defanged':sorted(defang(u) for u in urls),'attachments':attachments,'limits':['Headers are untrusted unless provenance establishes receiving boundary','No historical SPF/DKIM/DMARC validation','Regex URL extraction can miss obfuscated or encoded links','No malicious/benign verdict assigned','Review personal data before publishing']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('sample',type=Path);a=p.parse_args()
    print(json.dumps(triage(a.sample),ensure_ascii=False,indent=2))
