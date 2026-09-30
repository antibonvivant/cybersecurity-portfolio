# Phishing Investigation

Status: **Pending execution**
No results or candidate-completed work are claimed.

## Goal
Triage a reported message from a .eml sample and justify malicious / benign / inconclusive disposition.

## Steps
1. Use an exported lab email or public educational sample; record source, permission, UTC retrieval and SHA-256. Preserve original privately. Do not open attachments or navigate links.
2. Run scripts/triage_email.py sample.eml > triage.json. The script parses locally without requests, renders no HTML and never executes attachments. URLs are defanged. Review output for personal data before publishing.
3. Compare From, Reply-To, Return-Path, Message-ID and trusted Received chain. Trace Received from the trusted receiving boundary; sender-supplied lines may be forged.
4. Authentication-Results matters only if inserted by a trusted receiving system. SPF authenticates envelope sender/IP; DKIM validates a signature; DMARC tests alignment with visible From. A pass is not proof of harmlessness, a fail alone is not proof of maliciousness. An offline .eml does not allow trustworthy revalidation of historic DNS/authentication.
5. Compare visible link text and destination; inspect subdomains and lookalikes offline; categorize attachment names/types and hashes. Hash reputation lookup of public samples is optional. Do not upload private emails or attachments to public services.
6. State the social-engineering pretext and supported indicators. Map T1566.002 only if link-based phishing behavior is evidenced; T1566.001 for supported attachment phishing, not just any attachment.
7. Recommend preserving message, checking recipients/clicks/login telemetry, scoped blocking under runbook, reset/revoke sessions if credential exposure is confirmed and escalate to N2. Record what you did versus recommendation.

## Evidence and acceptance
Provenance/hash, sanitized headers, defanged IOC table, 3 screenshots of offline analysis, actual findings, report with confidence and unknowns. No evidence of clicks means do not claim endpoint compromise.
After execution: “Analisei [amostra/origem] examinando cabeçalhos, URLs e indicadores; documentei [conclusão real] e recomendações de triagem.”
