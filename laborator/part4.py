# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

from urllib.parse import urlparse

def parse_url(url):
    result = urlparse(url)

    print("scheme:", result.scheme)
    print("netloc:", result.netloc)
    print("path:", result.path)
    print("query:", result.query)
    print("fragment:", result.fragment)


parse_url("https://cybercor.org/path?x=1#top")

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

from urllib.parse import urljoin

def make_urls(base, paths):
    for path in paths:
        print(urljoin(base, path))


paths = ["/about", "contact.html", "../index.html"]

make_urls(BASE_URL, paths)

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

import re

def extract_links(html):
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


response = requests.get(BASE_URL)
print(extract_links(response.text))

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

from urllib.parse import urljoin, urlparse

def split_links(links, domain):
    internal = []
    external = []

    for link in links:
        full_url = urljoin(BASE_URL, link)

        if urlparse(full_url).netloc == domain:
            internal.append(full_url)
        else:
            external.append(full_url)

    return internal, external


links = ["/about", "contact.html", "https://google.com"]

internal, external = split_links(links, "cybercor.org")

print("Interne:", internal)
print("Externe:", external)

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

from html.parser import HTMLParser

class ImageFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "img":
            src = dict(attrs).get("src")

            if src:
                self.images.append(src)


test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fără src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)

print(finder.images)

assert finder.images == [
    "/logo.png",
    "poza.jpg",
    "https://cdn.example.com/banner.webp",
], "Parserul nu a găsit exact imaginile așteptate"

print("Testul a trecut!")

response = requests.get(BASE_URL, timeout=TIMEOUT)

finder = ImageFinder()
finder.feed(response.text)

print(len(finder.images), "imagini găsite")

for src in finder.images:
    print(src)

    # Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

import hashlib

def page_fingerprint(url):
    response = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()


fingerprint1 = page_fingerprint(BASE_URL)
fingerprint2 = page_fingerprint(BASE_URL)

print("Prima amprentă:", fingerprint1)
print("A doua amprentă:", fingerprint2)

print("Sunt identice:", fingerprint1 == fingerprint2)

#Amprentele ar fi diferite dacă și conținutul primit de la server este diferit, de exemplu dacă pagina a fost modificată sau serverul generează conținut dinamic.

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

import json

def save_headers(url):
    response = requests.get(url, timeout=TIMEOUT)

    with open("headers.json", "w") as file:
        json.dump(dict(response.headers), file, indent=2)


def load_headers():
    with open("headers.json", "r") as file:
        return json.load(file)


save_headers(BASE_URL)

headers = load_headers()

print(headers["Server"])

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

import socket

def resolve(hostname):
    return socket.gethostbyname(hostname)


print(resolve("cybercor.org"))

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

import ssl
import socket
from datetime import datetime

def cert_days_left(hostname):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

    expiry = ssl.cert_time_to_seconds(cert["notAfter"])
    expiry_date = datetime.fromtimestamp(expiry)
    days_left = (expiry_date - datetime.now()).days

    return days_left


print(cert_days_left("cybercor.org"))

# Laborator: functii, metode si importuri pe web
# Student: Şchiopu Valeria

TIMEOUT = 10 # secunde

DEFAULT_HEADERS = {"User-Agent": "WebLab-SchiopuValeria"}

import requests
import re
import socket
import ssl
import json
from urllib.parse import urlparse, urljoin
from datetime import datetime

def fetch(url):
    """Returnează obiectul răspuns."""
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    return response


def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


def get_title(html):
    """Returnează titlul paginii din codul HTML."""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()


def security_headers(url):
    """Verifică prezența antetelor de securitate."""
    response = requests.get(url, timeout=TIMEOUT)

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


def check_paths(base, paths):
    """Verifică codul de stare pentru mai multe căi."""
    result = {}

    for path in paths:
        response = requests.get(base + path, timeout=TIMEOUT)
        result[path] = response.status_code

    return result

def site_report(url):
    response = fetch(url)

    # 1. Codul de stare și URL-ul final
    status = response.status_code
    final_url = response.url

    # 2. Titlul paginii
    title = get_title(response.text)

    # 3. Adresa IP
    hostname = urlparse(final_url).hostname
    ip = socket.gethostbyname(hostname)

    # 4. Lanțul de redirecționări pornind de la http://
    redirect_response = requests.get(
        "http://" + hostname,
        headers=DEFAULT_HEADERS,
        timeout=TIMEOUT
    )

    redirects = [r.status_code for r in redirect_response.history]
    redirects.append(redirect_response.status_code)

    redirect_urls = [r.url for r in redirect_response.history]
    redirect_urls.append(redirect_response.url)

    # 5. Scorul antetelor de securitate
    security = security_headers(final_url)
    total = len(security)
    present = sum(security.values())
    security_score = f"{present}/{total}"

    # 6. Zilele rămase până la expirarea certificatului
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()

    expiry = ssl.cert_time_to_seconds(certificate["notAfter"])
    expiry_date = datetime.fromtimestamp(expiry)
    certificate_days = (expiry_date - datetime.now()).days

    # 7. Numărul de legături interne și externe
    links = re.findall(r'href="([^"]+)"', response.text)

    internal = 0
    external = 0
    domain = urlparse(final_url).netloc

    for link in links:
        full_url = urljoin(final_url, link)

        if urlparse(full_url).netloc == domain:
            internal += 1
        else:
            external += 1

    # 8. Căile interzise din robots.txt
    robots_response = requests.get(
        final_url + "/robots.txt",
        headers=DEFAULT_HEADERS,
        timeout=TIMEOUT
    )

    forbidden = []

    if robots_response.status_code == 200:
        for line in robots_response.text.splitlines():
            line = line.strip()

            if line.startswith("Disallow:"):
                path = line[len("Disallow:"):].strip()

                if path:
                    forbidden.append(path)

    # Afișarea raportului
    print("=== Raport site:", url, "===")
    print()
    print("Cod de stare:", status)
    print("URL final:", final_url)
    print("Titlu:", title)
    print("Adresă IP:", ip)
    print("Redirecționări:", " -> ".join(
        str(code) for code in redirects
    ), "->", " -> ".join(redirect_urls))
    print("Scor securitate:", security_score)
    print("Certificat:", certificate_days, "de zile rămase")
    print("Legături:", internal, "interne,", external, "externe")
    print("Căi interzise:", ", ".join(forbidden))

    # Salvarea în report.json
    report = {
        "status": status,
        "final_url": final_url,
        "title": title,
        "ip": ip,
        "redirects": redirect_urls,
        "security_score": security_score,
        "certificate_days": certificate_days,
        "internal_links": internal,
        "external_links": external,
        "disallowed_paths": forbidden
    }

    with open("report.json", "w") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

    print()
    print("Salvat în report.json")


if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
