# Supporting tools
Python 3 standard library only. These are AI-assisted preparation, not evidence that Kaique ran a lab.

```powershell
.\scripts\export-auth-events.ps1 -Start "2026-09-30T09:00:00-03:00" -End "2026-09-30T09:15:00-03:00" -OutDir ".\evidence-privateun-01"
```
Replace the time window with the actual run. Windows/PowerShell live execution is pending; Python tools were verified with a synthetic harmless email in the assistant environment.

```text
python scripts/triage_email.py evidence-private/sample.eml > evidence-private/triage.json
python scripts/hash_evidence.py projects/01-windows-authentication/evidence > manifest.json
```
Never write a manifest into the directory being hashed. Preserve original and sanitized hashes separately.
