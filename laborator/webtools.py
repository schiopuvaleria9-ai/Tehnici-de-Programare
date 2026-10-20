# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

import requests
import re
import socket
import ssl
import json
from urllib.parse import urlparse, urljoin
from datetime import datetime, timezone

TIMEOUT = 10
# Exercitiul 47: Constante de modul
DEFAULT_HEADERS = {"User-Agent": "WebLab-SchiopuValeria"}

# Exercitiul 44: Crearea unui modul
def fetch(url):
    return requests.get(
        url, headers=DEFAULT_HEADERS, timeout=TIMEOUT
    )


def get_status(url):
    return fetch(url).status_code


def get_title(html):
    match = re.search(
        r"<title[^>]*>(.*?)</title>",
        html, re.IGNORECASE | re.DOTALL
    )
    return match.group(1).strip() if match else "Fara titlu"


def security_headers(url):
    response = fetch(url)

    headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    result = {}
    for header in headers:
        result[header] = header in response.headers

    return result

# Exercitiul 49: Verificarea cailor site-ului
def check_paths(base, paths):
    result = {}

    for path in paths:
        url = urljoin(base.rstrip("/") + "/", path.lstrip("/"))
        result[path] = get_status(url)

    return result

# Exercitiul 50: Proiect final - raportul site-uluiz
def site_report(url):
    response = fetch(url)

    status = response.status_code
    final_url = response.url
    title = get_title(response.text)

    hostname = urlparse(final_url).hostname
    ip = socket.gethostbyname(hostname)

    # Redirectionari
    redirect_response = fetch("http://" + hostname)
    redirects = [
        {"status": r.status_code, "url": r.url}
        for r in redirect_response.history
    ]
    redirects.append({
        "status": redirect_response.status_code,
        "url": redirect_response.url
    })

    # Antete de securitate
    security = security_headers(final_url)
    present = sum(security.values())
    security_score = f"{present}/{len(security)}"

    # Certificat SSL
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()

    expiry = ssl.cert_time_to_seconds(certificate["notAfter"])
    expiry_date = datetime.fromtimestamp(expiry, timezone.utc)
    certificate_days = (expiry_date - datetime.now(timezone.utc)).days

    # Legaturi interne si externe
    links = re.findall(
        r'href\s*=\s*["\']([^"\']+)["\']',
        response.text, re.IGNORECASE
    )

    internal = 0
    external = 0
    domain = urlparse(final_url).hostname

    for link in links:
        full_url = urljoin(final_url, link)
        parsed = urlparse(full_url)

        if parsed.scheme not in ("http", "https"):
            continue

        if parsed.hostname == domain:
            internal += 1
        else:
            external += 1

    # Robots.txt
    robots_url = urljoin(final_url, "/robots.txt")
    robots_response = fetch(robots_url)
    forbidden = []

    if robots_response.status_code == 200:
        for line in robots_response.text.splitlines():
            line = line.strip()

            if line.lower().startswith("disallow:"):
                path = line.split(":", 1)[1].split("#", 1)[0].strip()
                if path:
                    forbidden.append(path)

    # Afisarea raportului
    print("\n=== Raport site:", url, "===")
    print("Cod de stare:", status)
    print("URL final:", final_url)
    print("Titlu:", title)
    print("Adresa IP:", ip)
    print("Redirectionari:", redirects)
    print("Scor securitate:", security_score)
    print("Certificat:", certificate_days, "de zile ramase")
    print("Legaturi:", internal, "interne,", external, "externe")
    print("Cai interzise:", forbidden)

    # Salvarea raportului JSON
    report = {
        "status": status,
        "final_url": final_url,
        "title": title,
        "ip": ip,
        "redirects": redirects,
        "security_score": security_score,
        "certificate_days": certificate_days,
        "internal_links": internal,
        "external_links": external,
        "disallowed_paths": forbidden
    }

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("Salvat in report.json")


# Exercitiul 46
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
