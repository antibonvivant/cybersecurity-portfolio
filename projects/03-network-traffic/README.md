# Network Traffic / PCAP Investigation

Status: **Pending execution**
No results or candidate-completed work are claimed.

## Goal
Explain a DNS → TCP → HTTP exchange and distinguish observations from unsupported claims of malicious traffic.

## Controlled fast path
1. Use two lab VMs on an isolated host-only network. One runs a local HTTP server: python -m http.server 8000 --bind [LAB_SERVER_IP] from a folder containing only a harmless index.html. Replace the placeholder with the actual lab IP.
2. Start Wireshark on the client lab interface. Generate a DNS lookup of example.com using the lab resolver if available; record it separately from local HTTP. Visit http://[LAB_SERVER_IP]:8000/ using curl or browser. Stop capture immediately. No public server exposure or real credentials.
3. Save PCAP privately, hash it and record interface, topology, IP pseudonyms, start/end UTC, versions and commands. If DNS is unavailable, mark it missing; do not manufacture DNS packets.
4. Filters: dns; tcp.flags.syn == 1; http.request; http.response; tcp.stream eq [actual stream number]; ip.addr == [lab address]; tcp.analysis.retransmission. Distinguish display filters from capture filters. Follow TCP Stream only for unencrypted lab HTTP.
5. Build frame-referenced timeline: DNS (separate example.com test), SYN/SYN-ACK/ACK, GET, status and close. The example.com DNS lookup did not resolve the IP-address-based local HTTP request: do not claim a single causal chain.
6. Add a public training PCAP with suspicious traffic if useful; link to source and record terms/hash. Analyze offline, do not replay malicious traffic. Label supplied capture versus your own experiment.

## Suspicious traffic reasoning
Check frequency, NXDOMAIN ratio, length/entropy of names, destination rarity, affected hosts and process context when available. High entropy or repeated DNS alone does not prove tunneling. TLS encrypts application contents; port 443 is not proof of benign traffic. Missing packets, NAT and capture location constrain interpretation.

## Deliverables
Topology description, source/hash, 3 screenshots, filters, frame IDs, UTC timeline, findings/limitations and escalation recommendation. For a baseline capture, conclusion may be expected benign traffic; do not relabel it an attack.
After execution: “Analisei PCAP [origem] no Wireshark, reconstruindo [fluxos reais] e documentando filtros, frames e limites da investigação.”
