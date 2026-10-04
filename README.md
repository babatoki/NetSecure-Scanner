# NetSecure Scanner

A Python-based TCP port scanning and security assessment tool developed in an isolated cybersecurity laboratory environment.

## Overview

NetSecure Scanner is a lightweight security assessment tool designed to identify exposed TCP services, classify potential risk, collect basic service banners, and generate structured security reports.

The project was developed and tested against a deliberately vulnerable **Metasploitable 2** virtual machine from a Kali Linux environment.

> **Important:** This project is intended for authorized security testing and controlled laboratory environments only.

## Features

- TCP port scanning
- Target IP/hostname resolution
- Service identification
- Basic service banner/version detection
- Security risk classification
- Security findings and recommendations
- Timestamped TXT security reports
- CSV report generation
- Command-line interface
- Configurable port selection

## Technologies

- Python 3
- Kali Linux
- Nmap
- cURL
- Metasploitable 2
- VirtualBox

## Lab Environment

| Component | Role |
|---|---|
| Kali Linux | Security testing workstation |
| Metasploitable 2 | Deliberately vulnerable target |
| VirtualBox | Virtualization platform |
| Network | Isolated host-only laboratory network |

### Target

`192.168.56.101`

## Usage

Run the scanner with:

```bash
python3 scanner.py 192.168.56.101
```

Specify custom ports:

```bash
python3 scanner.py 192.168.56.101 -p 22,80,3306,8180
```

View available options:

```bash
python3 scanner.py --help
```

## Example Assessment

The scanner identified four open services on the laboratory target:

| Port | Service | Risk |
|---:|---|---|
| 22 | SSH | Medium |
| 80 | HTTP | Medium |
| 3306 | MySQL | High |
| 8180 | Tomcat | High |

### Service Information

- **22/tcp:** OpenSSH 4.7p1
- **80/tcp:** Apache 2.2.8
- **3306/tcp:** MySQL
- **8180/tcp:** Apache Tomcat/Coyote

## Risk Assessment

### High Risk

**MySQL — Port 3306**

A database service is directly exposed to the network.

**Recommendation:** Restrict database access to authorized systems and hosts and review authentication and network-access controls.

**Tomcat — Port 8180**

A web application server is exposed to the network.

**Recommendation:** Restrict access where possible and review the Tomcat configuration, authentication, and exposed applications.

### Medium Risk

**SSH — Port 22**

Remote administration is available.

**Recommendation:** Restrict SSH access to trusted hosts and use strong authentication.

**HTTP — Port 80**

A web service is available without HTTPS encryption.

**Recommendation:** Use HTTPS where appropriate and restrict unnecessary access to the web service.

## Reporting

Each scan automatically generates:

- A human-readable TXT report
- A CSV report suitable for spreadsheet analysis

Reports are stored in the `reports/` directory.

Example:

```text
reports/
├── scan_192.168.56.101_YYYYMMDD_HHMMSS.txt
└── scan_192.168.56.101_YYYYMMDD_HHMMSS.csv
```

## Validation

The results were validated against Nmap service detection.

Example:

```bash
nmap -sV -p 22,80,3306,8180 192.168.56.101
```

The purpose of the comparison was to evaluate whether the custom scanner identified the same exposed services as an established security scanning tool.

## Project Structure

```text
NetSecure-Scanner/
├── scanner.py
├── README.md
├── REPORT.md
├── reports/
│   ├── TXT reports
│   └── CSV reports
└── screenshots/
    ├── reconnaissance
    ├── enumeration
    └── findings
```

## Limitations

NetSecure Scanner is an educational security assessment tool and is not intended to replace professional vulnerability scanners.

Current limitations include:

- Limited service fingerprinting
- Basic banner detection
- TCP scanning only
- No UDP scanning
- No automated vulnerability exploitation
- Risk classifications are based on predefined rules

## Future Improvements

Potential future development includes:

- UDP scanning
- Improved service fingerprinting
- CVE correlation
- JSON reporting
- HTML reporting
- Configurable risk profiles
- Improved banner detection
- Multi-target scanning
- Logging and scan history
- Integration with vulnerability databases

## Ethical Use

This tool should only be used against systems for which the tester has explicit authorization.

The laboratory testing in this project was conducted against an intentionally vulnerable Metasploitable 2 virtual machine in an isolated environment.
