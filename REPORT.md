# Web Application Security Assessment Report

## Executive Summary

A controlled security assessment was conducted against a deliberately vulnerable DVWA application hosted on an isolated Metasploitable 2 virtual machine. The assessment identified several security weaknesses, including directory listing, PHP information disclosure, exposed phpMyAdmin, SQL injection, and reflected cross-site scripting.

The most significant validated application vulnerability was SQL injection, which allowed a crafted input to return multiple database records. Reflected XSS was also successfully demonstrated. Recommendations focus on secure coding, access control, information minimization, parameterized database queries, output encoding, and secure configuration.

## Scope and Rules of Engagement

The assessment was limited to the user's isolated VirtualBox laboratory target at 192.168.56.101. No external systems were tested.

## Findings Summary

| ID | Finding | Severity |
|---|---|---|
| F-01 | Directory listing enabled | Medium |
| F-02 | PHP information disclosure | Medium |
| F-03 | phpMyAdmin exposed | Medium |
| F-04 | SQL Injection | High |
| F-05 | Reflected XSS | Medium |

## Conclusion

The exercise demonstrates the value of combining reconnaissance with application-level validation. Scanner output was treated as leads rather than automatically reported vulnerabilities, and confirmed findings were supported with direct evidence. The assessment reinforces the importance of secure application development, least privilege, controlled administration interfaces, and continuous security testing.
