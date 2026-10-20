# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10 #secunde

import requests

print(requests.__version__)

import urllib.request

# Explicație:
#requests e o bibliotecă externă, în timp ce urllib este în biblioteca standard.

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10 #secunde


import requests

response = requests.get(BASE_URL)
print(response.status_code)

# Avantaj: putem accesa ușor mai multe funcții din biblioteca requests.


from requests import get

response = get(BASE_URL)
print(response.status_code)

# Avantaj: codul este mai scurt, deoarece apelăm direct funcția get().

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10 #secunde

import requests as rq

# Aliasul face codul mai usor de citit cand numele este lung.
# Il face mai greu de citit cand numele nu este clar.

pagina = rq.get(BASE_URL)

print(pagina.status_code)

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10 #secunde

import urllib.request

request = urllib.request.Request(BASE_URL)
request.add_header("User-Agent", "Mozilla/5.0")

response = urllib.request.urlopen(request)

print(response.status)

data = response.read()

print(data[:200].decode("utf-8"))

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10 #secunde

import requests
print(dir(requests))

#'get'- functie
#'ConnectTimeout' - clasa
#'auth' - modul

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

import requests
#help(requests.get)

r = requests.get(BASE_URL, timeout=5)
print(r.status_code)

# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"
import time
import requests
start = time.perf_counter()

response = requests.get(BASE_URL)

end = time.perf_counter()
print(response.elapsed)


# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 #secunde
try:
  
    print("Modulul bs4 este instalat.")
except ImportError:
    print("Instalați modulul cu: pip install beautifulsoup4")

