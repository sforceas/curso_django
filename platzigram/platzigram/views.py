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