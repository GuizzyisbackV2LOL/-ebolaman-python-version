import requests

def get_ip_geolocation(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def print_geolocation_info(data):
    print("IP Address:", data["ip"])
    print("Country:", data["country"])
    print("City:", data["city"])
    print("Coordinates:", data["loc"])
    print("Postal Code:", data["postal"])
    print("Region:", data["region"])
    print("ASN:", data["org"])
    print("Google Maps:")
    loc = data["loc"].split(',')
    print(f"https://www.google.com/maps/?q={loc[0]},{loc[1]}")

# Get user input for IP address
ip_address = input("Enter IP Address: ")

# Get geolocation data
result = get_ip_geolocation(ip_address)

# Print geolocation information
print_geolocation_info(result)

# Credits
print("\n---- Credits ----")
print("This IP Geolocation script uses data from ipinfo.io.")
print("Please use this script responsibly and do not engage in any harmful activities.")
print("Enjoy exploring the world around you!")
print("This recode from ebola man IP Address GeoLocator C# Version converted into pyhton")

# Pause to prevent immediate exit
input("Press Enter to exit...")
