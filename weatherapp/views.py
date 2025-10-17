from django.shortcuts import render

# Create your views here.
def home(request):

    weather_data = {}
    if request.method == 'POST':

        city = request.POST.get('city')
        api_key = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'
        response = request.get(url)
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

    return render(request,'weather/home.html',{'weather_data':weather_data})        