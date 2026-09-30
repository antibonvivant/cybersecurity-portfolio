# Cybersecurity Portfolio - Kaique Brito
Computer Science student focused on SOC / Blue Team and Security Operations. Background in Python automation, REST APIs and web development.

This repository contains investigation plans and supporting tools. **No completed security investigation is claimed yet.** Cases move to completed only after I execute the investigation and provide verifiable evidence.

| Investigation | Status | Focus |
|---|---|---|
| [Windows Authentication](projects/01-windows-authentication/README.md) | Pending execution | Security events, authentication timeline, triage |
| [Phishing](projects/02-phishing/README.md) | Pending execution | Email headers, URLs, confidence and response |
| [Network Traffic](projects/03-network-traffic/README.md) | Pending execution | DNS, HTTP, TCP and packet evidence |

## Evidence standard
Every completed case includes provenance, environment/version details, UTC timeline, raw-data references, reproducible queries, alternative explanations, confidence, limitations and recommendations. Lab scenarios are identified as lab scenarios. MITRE mappings require supported behavior.

## Supporting material
- [Investigation and incident templates](templates/)
- [Windows event export](scripts/export-auth-events.ps1)
- [Email triage](scripts/triage_email.py)
- [SHA-256 evidence manifest](scripts/hash_evidence.py)
- [Draft detection](detections/windows_failed_logon.yml)
- [Publication checklist](docs/PUBLICATION.md)

Preparation was assisted by AI. Tools and drafts are scaffolding; execution, investigation conclusions and candidate understanding must be demonstrated separately. Do not interpret generated scaffolding as production SOC experience.
