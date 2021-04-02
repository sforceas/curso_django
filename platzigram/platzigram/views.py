"""
Archivo de vistas de la aplicación
"""

#Django
from django.http import HttpResponse, JsonResponse

#Utilidades
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs') #Aplicamos formato al datetime 
    return HttpResponse('Hi! The current server time is {now}'.format(now=str(now))) # Al ejecutar la función se responde con mensaje http

def numbers(request):
    # http://localhost:8000/numbers?numbers=12,13
    numbers = (request.GET['numbers'])
    #print(numbers)
    numbers = (list(numbers.split(",")))
    numbers = [int(i) for i in numbers]
    numbers.sort()
    #print(numbers)

    #return HttpResponse(f'Hi there! Your ascending list is: {numbers}') 
    return JsonResponse({ "numbers" : numbers}) #Reto: ordenar los numeros y devolver en formato json

def check_age(request,name,age):

    if age < 18:
        message = 'Lo sentimos, tienes que ser mayor de edad para usar este servicio.'
    else:
        message = 'Bienvenido a nuestro servicio'
    return HttpResponse(f'Hola, {name}. Tu edad es de {age} años. {message}')