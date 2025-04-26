import requests
import folium
import webbrowser

def get_geolocation():
    try:
        # Using a public API to get IP-based geolocation
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        
        if data['status'] == 'success':
            location_data = {
                'IP': data.get('query'),
                'City': data.get('city'),
                'Region': data.get('regionName'),
                'Country': data.get('country'),
                'Latitude': data.get('lat'),
                'Longitude': data.get('lon'),
                'ISP': data.get('isp')
            }
            return location_data
        else:
            print("Could not fetch location. Reason:", data.get('message'))
            return None
    except Exception as e:
        print("Error occurred:", e)
        return None

def show_location_on_map(latitude, longitude):
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup="You are here!").add_to(map_obj)
    # Save map to HTML
    map_obj.save("geolocation_map.html")
    # Open the map in a web browser
    webbrowser.open("geolocation_map.html")

def main():
    print("Fetching your location...\n")
    location = get_geolocation()
    if location:
        print("Your Geolocation Details:")
        for key, value in location.items():
            print(f"{key}: {value}")
        
        # Display location on map
        show_location_on_map(location['Latitude'], location['Longitude'])

if __name__ == "__main__":
    main()