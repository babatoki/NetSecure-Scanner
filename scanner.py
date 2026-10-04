#!/usr/bin/env python3

import socket
import argparse
from datetime import datetime
from pathlib import Path
import csv

PORT_INFO = {
    22: ("SSH", "MEDIUM", "Remote administration service exposed."),
    80: ("HTTP", "MEDIUM", "Web service exposed without HTTPS."),
    3306: ("MySQL", "HIGH", "Database service exposed to the network."),
    8180: ("TOMCAT", "HIGH", "Web application server exposed."),
}


def scan_port(target, port, timeout=2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        if sock.connect_ex((target, port)) == 0:
            return sock
    except OSError:
        pass

    sock.close()
    return None


def get_banner(sock, port):
    try:
        if port in (80, 8180):
            request = (
                b"HEAD / HTTP/1.0\r\n"
                b"Host: target\r\n"
                b"Connection: close\r\n\r\n"
            )
            sock.sendall(request)

        elif port == 22:
            return sock.recv(1024).decode(
                "utf-8", errors="ignore"
            ).strip()

        else:
            sock.settimeout(2)

        data = sock.recv(2048).decode(
            "utf-8", errors="ignore"
        )

        for line in data.splitlines():
            if line.lower().startswith(("server:", "version:")):
                return line.strip()

        return data.splitlines()[0].strip() if data else "No banner"

    except (socket.timeout, ConnectionError, OSError):
        return "Banner unavailable"

    finally:
        sock.close()


def main():

    parser = argparse.ArgumentParser(
        description="NetSecure Scanner v5 - Security Assessment Scanner"
    )

    parser.add_argument(
        "target",
        help="IP address or hostname to scan"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="22,80,3306,8180",
        help="Comma-separated list of ports to scan"
    )

    args = parser.parse_args()

    target = args.target

    try:
        ports = [int(p.strip()) for p in args.ports.split(",")]
    except ValueError:
        print("Error: Ports must be numbers separated by commas.")
        return

    start_time = datetime.now()
    timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")

    print("=" * 75)
    print("                         NetSecure Scanner v5")
    print("=" * 75)
    print(f"Target:  {target}")
    print(f"Started: {timestamp}")
    print("-" * 75)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Could not resolve target.")
        return

    print(f"Resolved IP: {target_ip}")
    print("-" * 75)

    findings = []

    for port in ports:

        sock = scan_port(target_ip, port)

        if sock:

            service, risk, reason = PORT_INFO.get(
                port,
                ("UNKNOWN", "UNKNOWN", "Unclassified service.")
            )

            banner = get_banner(sock, port)

            findings.append(
                (port, service, risk, reason, banner)
            )

    print(
        f"{'PORT':<8}"
        f"{'STATE':<10}"
        f"{'SERVICE':<12}"
        f"{'RISK':<10}"
        f"VERSION/BANNER"
    )

    print("-" * 75)

    for port, service, risk, reason, banner in findings:

        print(
            f"{port:<8}"
            f"{'OPEN':<10}"
            f"{service:<12}"
            f"{risk:<10}"
            f"{banner[:40]}"
        )

    high = sum(1 for _, _, r, _, _ in findings if r == "HIGH")
    medium = sum(1 for _, _, r, _, _ in findings if r == "MEDIUM")
    low = sum(1 for _, _, r, _, _ in findings if r == "LOW")

    print("-" * 75)
    print(f"Open ports found: {len(findings)}")

    print("\nSecurity Summary:")
    print(f"  HIGH:   {high}")
    print(f"  MEDIUM: {medium}")
    print(f"  LOW:    {low}")

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    report_path = report_dir / (
        f"scan_{target_ip}_"
        f"{start_time.strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(report_path, "w") as report:

        report.write("NetSecure Scanner v5\n")
        report.write("Security Assessment Report\n")
        report.write("=" * 75 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Resolved IP: {target_ip}\n")
        report.write(f"Scan Time: {timestamp}\n")
        report.write("=" * 75 + "\n\n")

        report.write("OPEN PORTS AND SERVICE INFORMATION\n")
        report.write("-" * 75 + "\n")

        for port, service, risk, reason, banner in findings:

            report.write(f"Port: {port}\n")
            report.write(f"Service: {service}\n")
            report.write(f"Risk: {risk}\n")
            report.write(f"Banner/Version: {banner}\n")
            report.write(f"Finding: {reason}\n\n")

        report.write("SECURITY SUMMARY\n")
        report.write("-" * 75 + "\n")
        report.write(f"HIGH: {high}\n")
        report.write(f"MEDIUM: {medium}\n")
        report.write(f"LOW: {low}\n")
        report.write(f"Total Open Ports: {len(findings)}\n")

    print(f"\nReport saved to: {report_path}")

    csv_path = report_dir / (
        f"scan_{target_ip}_"
        f"{start_time.strftime('%Y%m%d_%H%M%S')}.csv"
    )

    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow([
            "Port",
            "State",
            "Service",
            "Risk",
            "Banner/Version",
            "Finding"
        ])

        for port, service, risk, reason, banner in findings:
            writer.writerow([
                port,
                "OPEN",
                service,
                risk,
                banner,
                reason
            ])

    print(f"CSV report saved to: {csv_path}")
if __name__ == "__main__":
    main()
