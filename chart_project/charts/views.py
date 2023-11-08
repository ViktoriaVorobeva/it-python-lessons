from django.shortcuts import render

def temperature_chart(request):
    # Мокап данных (замените этот код на получение данных из вашей базы данных или других источников)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    temperatures = [36.6, 36.7, 36.8, 36.5, 37.0, 37.2, 37.1]

    return render(request, 'temperature_chart.html', {'days': days, 'temperatures': temperatures})

# from django.shortcuts import render

# def chart_view(request):
#     return render(request, 'chart.html')