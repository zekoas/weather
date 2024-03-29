from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        source = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&units=metric&appid=f197832259d5317a878327c99b655350"
        )
        json_data = source.read().decode("utf-8")  # Read the content and decode it
        list_of_data = json.loads(json_data)
        icon_id = str(list_of_data["weather"][0]["icon"])
        data = {
            "icon_id": str(list_of_data["weather"][0]["icon"]),
            "icon_url": f"https://openweathermap.org/img/wn/{icon_id}@2x.png",
            "weather": str(list_of_data["weather"][0]["main"]),
            "city": str(list_of_data["name"]),
            "country": str(list_of_data["sys"]["country"]),
            "wind_speed": str(list_of_data["wind"]["speed"]),
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "temperature": str(list_of_data["main"]["temp"]),
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
