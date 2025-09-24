import requests
import threading

# Read subdomains from file
with open("sub_domain.txt", "r") as f:
    subdomains = f.read().splitlines()

domain = "youtube.com"
discovered_subdomains = []  
lock = threading.Lock()     

def check_subdomains(subdomain):
    url = f"https://{subdomain}.{domain}"
    try:
        # Use HEAD request for faster response
        response = requests.head(url, timeout=5)
    except requests.Timeout:
        # Timeout occurred
        pass
    except requests.RequestException:
        # Other request exceptions (ConnectionError, SSLError etc.)
        pass
    else:
        # Successfully got response
        print(f"[+] Discovered: {url} (Status: {response.status_code})")
        with lock:
            discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomains, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Save discovered subdomains to file
with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

print("\nScanning complete!")
