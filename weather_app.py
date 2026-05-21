import requests

city = input("Enter city name: ")

api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")

else:
    print("City not found!")
