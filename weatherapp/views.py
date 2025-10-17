from django.shortcuts import render
import requests
# Create your views here.
def home(request):

    weather_data = {}
    if request.method == 'POST':

        city = request.POST.get('city')
        api_key = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {

                'city' : city ,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data['error'] = 'city not found'

    return render(request,'weatherapp/home.html',{'weather_data':weather_data})        