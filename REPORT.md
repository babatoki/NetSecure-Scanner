# Security Assessment Report

## 1. Executive Summary

A controlled security assessment was performed against a deliberately vulnerable Metasploitable 2 virtual machine using Kali Linux.

The assessment identified four exposed TCP services: SSH, HTTP, MySQL, and Apache Tomcat. Two services were classified as high risk and two as medium risk based on their network exposure and potential security impact.

The assessment demonstrates how exposed services can increase the attack surface of a system and why unnecessary network services should be restricted and properly secured.

## 2. Scope

### Target

- Target system: Metasploitable 2
- IP address: `192.168.56.101`
- Testing system: Kali Linux
- Network: Isolated virtual laboratory
- Authorization: Controlled educational laboratory environment

### Testing Objective

The objective was to:

1. Identify exposed TCP services.
2. Determine basic service and version information.
3. Classify identified services according to security risk.
4. Document findings.
5. Generate machine-readable and human-readable reports.

## 3. Methodology

The assessment followed a basic reconnaissance and enumeration workflow:

1. Identify the target IP address.
2. Perform TCP port scanning.
3. Identify services running on open ports.
4. Collect basic service banners.
5. Compare results with Nmap service detection.
6. Classify security findings.
7. Generate assessment reports.

The custom NetSecure Scanner was used as the primary assessment tool, while Nmap was used to validate the results.

## 4. Findings

### Finding 1 — SSH Exposed

**Port:** 22/tcp  
**Service:** SSH  
**Risk:** Medium

The SSH service was accessible from the testing system.

Service information identified:

`OpenSSH 4.7p1 Debian-8ubuntu1`

### Security Impact

An exposed remote administration service increases the attack surface. If authentication controls are weak or vulnerabilities exist in the SSH implementation, an attacker could potentially attempt unauthorized access.

### Recommendation

- Restrict SSH access to trusted systems.
- Use strong authentication.
- Disable unnecessary accounts.
- Keep the SSH service updated.
- Monitor authentication attempts.

---

### Finding 2 — HTTP Service Without HTTPS

**Port:** 80/tcp  
**Service:** HTTP  
**Risk:** Medium

The target exposed a web service over HTTP.

Service information identified:

`Apache/2.2.8 (Ubuntu) DAV/2`

### Security Impact

HTTP does not provide transport encryption. Sensitive information transmitted through an unencrypted connection may be exposed to network interception.

### Recommendation

- Use HTTPS for sensitive web traffic.
- Disable unnecessary HTTP access where possible.
- Keep the web server updated.
- Review web server configuration.

---

### Finding 3 — MySQL Database Exposed

**Port:** 3306/tcp  
**Service:** MySQL  
**Risk:** High

The MySQL database service was directly accessible over the network.

### Security Impact

Exposing a database service increases the possibility of unauthorized database access, credential attacks, information disclosure, or exploitation of vulnerable database software.

### Recommendation

- Restrict MySQL access to authorized hosts.
- Do not expose database services unnecessarily.
- Use strong database authentication.
- Keep the database software patched.
- Monitor database authentication attempts.

---

### Finding 4 — Apache Tomcat Exposed

**Port:** 8180/tcp  
**Service:** Apache Tomcat  
**Risk:** High

An Apache Tomcat web application service was accessible over the network.

Service information identified:

`Apache-Coyote/1.1`

### Security Impact

An exposed application server increases the attack surface and may provide access to vulnerable web applications or administrative interfaces.

### Recommendation

- Restrict access to trusted hosts.
- Remove unnecessary applications.
- Secure administrative interfaces.
- Update the application server.
- Review authentication and authorization controls.
- Monitor application-server activity.

## 5. Risk Summary

| Risk Level | Findings |
|---|---:|
| High | 2 |
| Medium | 2 |
| Low | 0 |
| **Total** | **4** |

## 6. Validation

The custom scanner results were compared with Nmap service detection.

Nmap identified the following services:

| Port | Service | Version |
|---:|---|---|
| 22 | SSH | OpenSSH 4.7p1 |
| 80 | HTTP | Apache 2.2.8 |
| 3306 | MySQL | MySQL 5.0.51a |
| 8180 | HTTP/Tomcat | Apache Tomcat/Coyote |

The comparison demonstrated that the custom scanner successfully identified the same primary exposed services.

## 7. Evidence

Screenshots documenting the assessment are included in the project repository.

Evidence includes:

- Web enumeration
- PHP information
- Directory listing
- SQL injection testing
- Reflected XSS testing
- Session/logout testing
- Custom scanner results
- Nmap service detection

## 8. Remediation Priority

The recommended remediation order is:

1. **Restrict MySQL (3306/tcp).**
2. **Secure and restrict Tomcat (8180/tcp).**
3. **Review and secure the HTTP service (80/tcp).**
4. **Restrict and harden SSH (22/tcp).**

The highest priority should be given to services that expose sensitive functionality or provide access to databases and application servers.

## 9. Limitations

This assessment was conducted in an intentionally vulnerable educational environment.

The assessment did not attempt to:

- Exploit vulnerabilities.
- Obtain unauthorized credentials.
- Modify or destroy data.
- Perform denial-of-service testing.
- Conduct persistence activities.

The custom scanner also provides basic service identification and risk classification rather than comprehensive vulnerability assessment.

## 10. Conclusion

The assessment demonstrated the importance of identifying and reducing unnecessary network exposure.

The NetSecure Scanner successfully identified four open services and generated structured security reports. Validation against Nmap demonstrated that the custom scanner could identify the primary services exposed by the laboratory target.

Future improvements could include enhanced service fingerprinting, CVE correlation, UDP scanning, JSON/HTML reporting, and integration with vulnerability intelligence sources.
