
from checker import SITES, build_url, is_https, show_response, check_site, scan_sites, check_headers, retry_check

print("PARTEA 1")
print(build_url("example.com", "login"))
print(build_url("example.com", "/login"))
print(is_https(SITES[0]))
print(is_https("http://example.com"))

print("\nPARTEA 2")
show_response(SITES[0])
show_response(SITES[1])

print("\nPARTEA 3")
for site in SITES:
    print(site, check_site(site))

print("\nPARTEA 4")
scan_sites()

print("\nPARTEA 5")
print(check_headers(SITES[0]))
print(check_headers("http://this-site-does-not-exist.invalid"))

print("\nPARTEA 6")
print(retry_check(SITES[0]))
print(retry_check(SITES[3]))
print(retry_check(SITES[4], attempts=2))
