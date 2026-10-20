
# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
# Partea 3: Scrierea propriilor functii
# Exercitiile 21-34

import requests
import time

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def fetch(url, timeout=10):
    """Returneaza obiectul raspuns."""
    return requests.get(url, timeout=timeout)


response = fetch(BASE_URL)
print("Exercitiul 21:", response.status_code)

time.sleep(1)


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria

def get_status(url: str) -> int:
    """Returneaza codul de stare HTTP pentru URL."""
    response = fetch(url)
    return response.status_code


print("Exercitiul 22:")
for path in ["/", "/robots.txt", "/sitemap.xml"]:
    time.sleep(1)
    print(path, get_status(BASE_URL + path))

# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
print("Exercitiul 23:")

time.sleep(1)
response1 = fetch(BASE_URL)
print(response1.status_code)

time.sleep(1)
response2 = fetch(BASE_URL, timeout=3)
print(response2.status_code)


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def get_title(html):
    """Returneaza titlul paginii din codul HTML."""
    start = html.find("<title>")
    end = html.find("</title>")

    if start == -1 or end == -1:
        return "Fara titlu"

    start += len("<title>")
    return html[start:end].strip()


print("Exercitiul 24:", get_title(response1.text))

# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
print("Exercitiul 25:")
help(get_title)


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
print("Exercitiul 26:")

try:
    print(get_status(123))
except requests.RequestException:
    print("Eroare: 123 nu este un URL valid.")
    print("Adnotarile de tip nu opresc automat erorile.")


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def page_exists(url):
    """Verifica daca o pagina exista."""
    try:
        response = fetch(url)
        return response.ok
    except requests.RequestException:
        return False


print("Exercitiul 27:")
print(page_exists("https://this-domain-does-not-exist.invalid"))


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def check_paths(base, paths):
    """Returneaza codurile HTTP pentru mai multe cai."""
    result = {}

    for path in paths:
        time.sleep(1)
        try:
            result[path] = get_status(base + path)
        except requests.RequestException:
            result[path] = None

    return result


paths = ["/", "/robots.txt", "/sitemap.xml"]

print("Exercitiul 28:")
print(check_paths(BASE_URL, paths))

# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def get_header(url, name, default="lipseste"):
    """Returneaza valoarea unui antet HTTP."""
    response = fetch(url)
    return response.headers.get(name, default)


time.sleep(1)
print("Exercitiul 29:")
print(get_header(BASE_URL, name="Server"))

# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def security_headers(url):
    """Verifica prezenta antetelor de securitate."""
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


time.sleep(1)
security = security_headers(BASE_URL)

print("Exercitiul 30:")
print(security)

# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def score_headers(results):
    """Calculeaza scorul antetelor de securitate."""
    total = len(results)
    present = sum(results.values())
    return f"{present}/{total}"


print("Exercitiul 31:")
print(score_headers(security))


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def fetch_robots(base):
    """Returneaza continutul robots.txt sau None."""
    try:
        response = fetch(base + "/robots.txt")

        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        pass

    return None


def disallowed_paths(robots_text):
    """Returneaza lista cailor interzise."""
    if robots_text is None:
        return []

    result = []

    for line in robots_text.splitlines():
        line = line.strip()

        if line.startswith("Disallow:"):
            path = line[len("Disallow:"):].strip()
            if path:
                result.append(path)

    return result


time.sleep(1)
robots = fetch_robots(BASE_URL)

print("Exercitiul 32:")
print(disallowed_paths(robots))


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def response_times(*urls):
    """Returneaza timpul de raspuns pentru URL-uri."""
    result = {}

    for url in urls:
        time.sleep(1)
        try:
            response = fetch(url)
            result[url] = response.elapsed.total_seconds()
        except requests.RequestException:
            result[url] = None

    return result


print("Exercitiul 33:")
print(response_times(BASE_URL, ECHO_URL))


# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria
def log(message, **details):
    """Afiseaza mesajul si detaliile primite."""
    print(message, end="")

    for name, value in details.items():
        print(" | " + name + "=" + str(value), end="")

    print()


print("Exercitiul 34:")
log("verificat", url=BASE_URL, status=200)

