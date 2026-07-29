# Cities Dictionary
cities = {'bikaner': (28.0176, 73.3149) , 'mumbai': (19.0760, 72.8777),'bangalore': (12.9716, 77.5946),'chennai': (13.0827, 80.2707),'pune': (18.5204, 73.8567),'hyderabad': (17.3850, 78.4867) }

# Function to check city name
def check_city(city_name):
    city = city_name.lower()  # Ignore case
    if city in cities:
        lat, lon = cities[city]
        return f"{city.title()}: Latitude = {lat}, Longitude = {lon}"
    else:
        return "City not found in the dictionary."

while True:
    user_input = input("Enter a city name (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting the program.")
        break

    print(check_city(user_input))