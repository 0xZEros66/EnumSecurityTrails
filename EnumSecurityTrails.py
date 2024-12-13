import requests

def fetch_domains(apex_domain, api_key):
    url = f"https://api.securitytrails.com/v1/domain/{apex_domain}/subdomains"
    headers = {
        "Accept": "application/json",
        "APIKEY": api_key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "subdomains" in data:
            subdomains = data["subdomains"]
            full_domains = [f"{sub}.{apex_domain}" for sub in subdomains]
            return full_domains
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    api_key = "PUT your API TOKEN HERE" # PUT your api here
    apex_domain = input("Enter the apex domain (e.g., google.com): ").strip()
    
    if apex_domain:
        print(f"Fetching subdomains for {apex_domain}...")
        domains = fetch_domains(apex_domain, api_key)
        if domains:
            with open("trailsdomains.txt", "w") as file:
                for domain in domains:
                    file.write(domain + "\n")
            print(f"Subdomains successfully saved to 'trailsdomains.txt'.")
        else:
            print("No domains were found or an error occurred.")
    else:
        print("No domain entered. Exiting...")
