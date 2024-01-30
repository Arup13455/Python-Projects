class CityTemperature:
    def __init__(self, city, temperature):
        self.city = city
        self.temperature = temperature

# Get user input for the number of cities
num_cities = int(input("Enter the number of cities: "))

# Create a list to store CityTemperature instances
cities_data = []

# Get user input for each city and its temperature
for i in range(num_cities):
    city_name = input(f"Enter the name of city {i+1}: ")
    city_temp = float(input(f"Enter the temperature in {city_name} (in Celsius): "))
    city_instance = CityTemperature(city_name, city_temp)
    cities_data.append(city_instance)

# Displaying city temperatures
print("\nCity Temperatures:")
for city_data in cities_data:
    print(f"{city_data.city}: {city_data.temperature}°C")

# Find and display the city with the highest temperature
highest_temp_city = max(cities_data, key=lambda x: x.temperature)
print(f"\nCity with the highest temperature: {highest_temp_city.city} ({highest_temp_city.temperature}°C)")

# Find and display the city with the lowest temperature
lowest_temp_city = min(cities_data, key=lambda x: x.temperature)
print(f"City with the lowest temperature: {lowest_temp_city.city} ({lowest_temp_city.temperature}°C)")
# Calculate and display the average temperature
average_temp = sum(city_data.temperature for city_data in cities_data) / num_cities
print(f"Average temperature across cities: {average_temp}°C")
