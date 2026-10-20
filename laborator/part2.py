# Laborator: Primul import
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 #secunde

import requests

response = requests.get(BASE_URL)

print(response.status_code) #atribut
print(response.ok)  #atribut
print(response.url)  #atribut
print(response.encoding)  #atribut

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 #secunde

import requests

response = requests.get(BASE_URL)
response.raise_for_status()

try:
    response = requests.get(BASE_URL + "/this-page-does-not-exist")
    print(response.status_code)
    response.raise_for_status()
except requests.HTTPError:
    print("Pagina nu exista sau nu poate fi accesata. Mai incearca :)")

    
# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)
for nume, valoare in response.headers.items():
	print(nume+": "+ valoare)

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

print(response.headers.get("Server", "lipsește"))
print(response.headers.get("Content-Type", "lipsește"))
print(response.headers.get("content-type", "lipsește"))

#cloudflare
#text/html; charset=utf-8
#text/html; charset=utf-8

#Antetele HTTP nu sunt case-sensitive, deci nu conteaza ca sunt scrie cu majuscula sau minuscula

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

print(response.text.lower().count("cyber"))

#lower() - pentru citirea textului in minuscula, pentru a nu fi mai multe forme de scriere precum:CYBER/Cyber/cyber
#count() - pentru numararea de cate ori apare "cyber"

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

html = response.text

start = html.find("<title>") + len("<title>")
end = html.find("</title>")

print(html[start:end].strip())

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

lines = response.text.splitlines()

print("Numar de linii:", len(lines))
print("Lungimea celei mai lungi linii:", len(max(lines, key=len)))


# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

if response.url.startswith("https://"):
    print("Conexiune securizată")
else:
    print("Conexiune nesecurizată")

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get("http://cybercor.org")

for redirect in response.history:
    print(redirect.status_code, redirect.url)

print("URL final:", response.url)

# Laborator: functii, metode si importuri pe web
# Student: Șcchiopu Valeria
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

head_response = requests.head(BASE_URL)
get_response = requests.get(BASE_URL)

print("HEAD:", len(head_response.content))
print("GET:", len(get_response.content))

# HEAD primește doar antetele, fără conținutul paginii,, avand un numar mic, sau chiar 0 iar GET primește și conținutul paginii,un numar cu mult mai mare.

# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

response = requests.get(BASE_URL)

if response.cookies:
    for cookie in response.cookies:
        print("Nume:", cookie.name, "Secure:", cookie.secure)
else:
    print("Niciun cookie setat")
# Laborator: functii, metode si importuri pe web
# Student: Șchiopu Valeria

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "WebLab-Schiopu Valeria"
})

response = session.get(ECHO_URL + "/headers")

print(response.json())
print("User-Agent:", response.json()["headers"]["User-Agent"])