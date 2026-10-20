
# Laborator: functii, metode si importuri pe web
# Student: Schiopu Valeria

# Exercitiul 44: Importarea modulului webtools
import webtools

# Exercitiul 45: Importarea anumitor nume
from webtools import get_title, security_headers

# Daca main.py ar avea o functie proprie get_title,
# aceasta ar inlocui numele importat din webtools.

# Exercitiul 47: Importarea constantei
from webtools import DEFAULT_HEADERS

# Exercitiul 48: Argumente din linia de comanda
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Adresa site-ului")
args = parser.parse_args()

url = args.url

# Exercitiul 44: Apelarea functiilor din modul
print("Titlu:", webtools.get_title(webtools.fetch(url).text))

# Exercitiul 45: Utilizarea functiilor importate
print("Antete securitate:", security_headers(url))

# Exercitiul 47: Afisarea constantei
print("DEFAULT_HEADERS:", DEFAULT_HEADERS)

# Exercitiul 49: Generarea raportului CSV
paths = ["/", "/robots.txt", "/admin", "/login"]
results = webtools.check_paths(url, paths)

with open("report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["path", "status", "checked_at"])

    for path, status in results.items():
        writer.writerow([
            path,
            status,
            datetime.now().isoformat()
        ])

print("Salvat in report.csv")

# Exercitiul 50: Generarea raportului final JSON
webtools.site_report(url)
