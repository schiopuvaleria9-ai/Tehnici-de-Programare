
import requests

SITES = [
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500"
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

# Partea 1
def build_url(host, path):
    return "https://" + host + "/" + path.lstrip("/")

def is_https(url):
    return url.startswith("https://")


# Partea 2
def show_response(url):
    try:
        r = requests.get(url, timeout=5)
        print("Status:", r.status_code)
        print("Content-Type:", r.headers.get("Content-Type"))
    except requests.RequestException:
        print("Eroare la conectare")


# Partea 3
def check_site(url):
    try:
        r = requests.get(url, timeout=5)
        return {
            "status": r.status_code,
            "content_type": r.headers.get("Content-Type"),
            "length": len(r.content),
            "server": r.headers.get("Server", "unknown")
        }
    except requests.RequestException:
        return {"status": None, "error": "Conexiune esuata"}


# Partea 4
def scan_sites():
    rezultate = []

    for site in SITES:
        rezultat = check_site(site)
        rezultate.append((site, rezultat))

    bune = []

    for site, rezultat in rezultate:
        if rezultat["status"] == 200:
            bune.append((site, rezultat))

    bune.sort(key=lambda x: x[1]["length"], reverse=True)

    for site, rezultat in bune:
        print(site, "->", rezultat["length"], "octeti")

    print("Reusite:", len(bune))
    print("Esuate:", len(rezultate) - len(bune))


# Partea 5
def check_headers(url):
    try:
        r = requests.get(url, timeout=5)

        present = []
        missing = []

        for h in SECURITY_HEADERS:
            if h in r.headers:
                present.append(h)
            else:
                missing.append(h)

        score = len(present) * 100 // len(SECURITY_HEADERS)

        return {
            "present": present,
            "missing": missing,
            "score": score
        }

    except requests.RequestException:
        return {"status": None, "error": "Conexiune esuata"}


# Partea 6
def retry_check(url, attempts=3):
    status = None
    error = None

    for i in range(attempts):
        try:
            r = requests.get(url, timeout=5)
            status = r.status_code
            error = None

            if status < 500:
                return {"status": status, "attempts": i + 1}

        except requests.RequestException:
            error = "Conexiune esuata"

    rezultat = {"status": status, "attempts": max(0, attempts)}

    if error is not None:
        rezultat["error"] = error

    return rezultat
