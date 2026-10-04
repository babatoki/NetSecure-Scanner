# Web Application Security Assessment — DVWA

## Overview

A controlled web application security assessment performed against Damn Vulnerable Web Application (DVWA) running on an isolated Metasploitable 2 virtual machine. The project demonstrates reconnaissance, web enumeration, vulnerability validation, evidence collection, risk assessment, and remediation recommendations.

> **Scope:** Isolated lab environment only. The target was a deliberately vulnerable application designed for security training.

## Environment

- **Testing platform:** Kali Linux
- **Target:** Metasploitable 2
- **Application:** DVWA
- **Target IP:** 192.168.56.101
- **Tools used:** Nmap, cURL, browser/DVWA

## Methodology

1. Verified connectivity between Kali Linux and the target.
2. Performed service/version discovery with Nmap.
3. Enumerated HTTP services and exposed directories.
4. Validated information-disclosure and web-application findings.
5. Tested SQL injection and reflected XSS within DVWA.
6. Captured screenshots as evidence.
7. Assessed impact and documented remediation recommendations.

## Findings

| ID | Finding | Severity | Status |
|---|---|---|---|
| F-01 | Directory listing enabled at `/doc/` | Medium | Confirmed |
| F-02 | PHP information disclosure at `/phpinfo.php` | Medium | Confirmed |
| F-03 | phpMyAdmin exposed | Medium | Confirmed exposure; vulnerability not claimed |
| F-04 | SQL Injection in DVWA | High | Confirmed |
| F-05 | Reflected Cross-Site Scripting (XSS) | Medium | Confirmed |

## F-01 — Directory Listing

The `/doc/` endpoint returned an `Index of /doc/` page and exposed directory contents.

**Impact:** Application structure and files may become available to an attacker, supporting further reconnaissance.

**Remediation:** Disable directory indexing and explicitly restrict publicly accessible files/directories.

## F-02 — PHP Information Disclosure

The publicly accessible `/phpinfo.php` endpoint disclosed PHP and operating-system details.

**Impact:** Technology and configuration information can help an attacker fingerprint the environment and research applicable vulnerabilities.

**Remediation:** Remove or restrict `phpinfo.php` in production and avoid exposing unnecessary platform/configuration details.

## F-03 — phpMyAdmin Exposure

The `/phpMyAdmin/` administrative interface was reachable over HTTP.

**Impact:** Exposed administration interfaces increase attack surface and should not normally be publicly reachable.

**Remediation:** Restrict access using network controls, VPN/private access, strong authentication, and appropriate administrative access policies.

## F-04 — SQL Injection

DVWA accepted the test input `1' OR '1'='1' #` and returned multiple database records, demonstrating SQL injection in the deliberately vulnerable application.

**OWASP:** A03:2021 — Injection

**Impact:** SQL injection can permit manipulation of database queries and potentially unauthorized access to data, depending on database privileges and application design.

**Remediation:** Use parameterized queries/prepared statements, validate input, apply least-privilege database permissions, suppress detailed database errors, and include injection testing in the SDLC.

## F-05 — Reflected XSS

The DVWA reflected-XSS function executed the test payload `<script>alert('XSS')</script>` in the browser and produced a JavaScript alert.

**OWASP:** A03:2021 — Injection

**Impact:** Reflected XSS can allow attacker-controlled JavaScript to execute in a victim's browser and may support phishing, unauthorized actions, or session-related attacks depending on application protections.

**Remediation:** Apply context-appropriate output encoding, validate input where appropriate, implement a strong Content Security Policy, and avoid inserting untrusted data directly into HTML/JavaScript contexts.

## Key Learning Outcomes

- Network and web-service reconnaissance
- HTTP response/header analysis
- Web application attack-surface enumeration
- SQL injection validation
- Reflected XSS validation
- Security evidence collection
- Risk and impact assessment
- Vulnerability remediation planning

## Evidence

Screenshots supporting the assessment are stored in the `evidence/` directory.
