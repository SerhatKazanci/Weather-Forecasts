import requests


API = "f6a34a43c83f31f774f959bdfd779c2a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

SEHIR_ISMI = input("Şehir İsmi Giriniz :")

URL = BASE_URL + "appid=" + API + "&q=" + SEHIR_ISMI

gelen_veri = requests.get(URL)

gelen_veri_JSON = gelen_veri.json()

if (gelen_veri_JSON["cod"] != "404"):

    temp = gelen_veri_JSON["main"]["temp"]
    description = gelen_veri_JSON["weather"][0]["description"]
    pressure = gelen_veri_JSON["main"]["pressure"]
    country = gelen_veri_JSON["sys"]["country"]
    windSpeed = gelen_veri_JSON['wind']['speed']

    print("temp :" + str(float(temp)-273.15))
    print("description :" + str(description))
    print("windSpeed :", windSpeed)
    print("pressure :", pressure)
    print("country :", country)


else:
    print("böyle bir şehir bulunamadı...")
