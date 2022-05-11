import requests

def weather(location):
    city=location
    api_address=f'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['weather'][0]["description"]
    temp=json_data['main']['temp']         
    return city,format_add,temp

def location():
    ip=requests.get("http://myip.dnsomatic.com").text
    location="http://ipwhois.app/json/"
    url=location+ip
    try:
        json_data = requests.get(url).json()
        return json_data
    except:
        print("API is not working")    

def ip():
    ip=requests.get("http://myip.dnsomatic.com").text
    return ip