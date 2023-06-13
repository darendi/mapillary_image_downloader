import requests

# Specify the address to geocode
address = '1600 Amphitheatre Parkway, Mountain View, CA'

# Make a request to the Nominatim API
url = f'https://nominatim.openstreetmap.org/search?q={address}&format=json'
response = requests.get(url)
data = response.json()

# Extract the coordinates from the response
if data:
    location = data[0]
    latitude = float(location['lat'])
    longitude = float(location['lon'])
    print(f'Latitude: {latitude}, Longitude: {longitude}')
else:
    print('Geocoding failed.')