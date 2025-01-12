import requests
def get_weather(city):
    api_key="cee7f6a6503f55fe06e84d45eb44a08a"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response=requests.get(url)
        if response.status_code==200:
            data = response.json()
            city_name=data['name']
            country=data['sys']['country']
            weather=data['weather'][0]['description']
            temperature=data['main']['temp']
            feels_like=data['main']['feels_like']
            humidity=data['main']['humidity']
            wind_speed=data['wind']['speed']
            print(f"Weather in {city_name}, {country}:")
            print(f"- Description: {temperature}C")
            print(f"- Feels Like:{feels_like}%")
            print(f"- Wind Speed:{wind_speed} m/s")
        else:
            print("City not found or API error. Please try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occured:{e}")

if __name__=="__main__":
    print("Welcome to the Weather App!")
    city=input("Enter the name of the city:")
    get_weather(city)
            
