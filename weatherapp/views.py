from django.shortcuts import render
import requests

def home(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'e194982fdd3da2b6368c9d45f50c02a7'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] = 'City not found'

    return render(request, 'weatherapp/home.html', {'weather_data': weather_data})
