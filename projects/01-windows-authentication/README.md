# Windows Authentication Investigation

Status: **Pending execution**
No results or candidate-completed work are claimed.

## Goal
Investigate controlled failed logons and a later success. A successful logon is not proof of compromise; source, account, logon type and subsequent activity matter.

## Minimal path - execute first
1. Use an isolated Windows VM and a dedicated standard local test account. Snapshot; note Windows build, clock/time zone and current audit settings. Do not use a corporate or personal privileged account.
2. Verify Audit Logon success/failure is enabled using Local Security Policy (secpol.msc where available) > Advanced Audit Policy > Logon/Logoff. Windows editions differ; if unavailable, document that and use the supported audit-policy method for your edition.
3. Record start time UTC. Manually attempt 3-5 incorrect sign-ins to the lab account, remaining below its lockout threshold, then one correct sign-in. This is a small controlled authentication pattern, not a production brute-force incident.
4. Event Viewer > Windows Logs > Security: filter 4625 and 4624 within the experiment window. Save original event XML and screenshots. Missing events: confirm host, policy, collection window and record policy state; do not clear logs.
5. Run scripts/export-auth-events.ps1 in the VM using a specific Start/End window. Security log reading normally requires elevation; script is read-only and does not modify auditing.
6. Record target user/domain, logon type, IP/workstation if present, status/substatus, UTC and record ID. Source may be absent or local; do not fabricate a remote source. Compare background logons to the test account.
7. Build a timeline with the actual number of failures, interval, success and evidence references. Consider mistyped password and stale credentials. Distinguish local interactive (type 2), network (3) and remote interactive (10) if observed.

## SIEM extension - separate capability gate
Use the current official Wazuh quickstart on a supported Linux VM after checking hardware. Do not expose the dashboard publicly. Install an official Windows agent, enroll it, verify active status and receipt of the Security channel. Inspect an actual event JSON to confirm field names.
Draft search (only if schema matches): data.win.system.eventID:4625 OR data.win.system.eventID:4624. Filter by agent, account and time; record the exact working query and version. Events that do not generate alerts may not appear in the default alert index; confirm collection/rules or appropriately configured archives instead of assuming absence means no activity.
Sysmon is optional: its Operational channel provides process/network telemetry according to configuration; Security supplies authentication. Sysmon process-create event 1 can add post-logon context; network event 3 depends on configuration. Do not claim Sysmon collected authentication.

## Detection reasoning
The draft Sigma only selects 4625. To detect a pattern: aggregate failures by host/account/source (when present) in a defined interval; choose and validate a threshold against your baseline. To investigate subsequent success: correlate same relevant entities and logon type within a justified window. A basic 4625 rule is not a brute-force correlation rule.
ATT&CK T1110.001 only if the controlled behavior actually models password guessing; otherwise keep the case as authentication analysis. Do not call every failed login an attack.

## Deliverables / acceptance
3-5 screenshots; sanitized event excerpts; CSV timeline; actual query; case study and report; alternate explanations; original/redacted hash references. State local analysis complete and SIEM pending if only minimal path ran.
After execution only: “Investiguei [N] eventos de autenticação em laboratório Windows, correlacionando [campos reais] e documentando timeline, evidências e critérios de escalonamento.” Add Wazuh only if it was deployed and used.

## Sources
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624
- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- https://documentation.wazuh.com/current/quickstart.html
- https://attack.mitre.org/techniques/T1110/001/
