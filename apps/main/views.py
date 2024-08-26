from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request,'home.html', {})

def resultado(request):
    json = request.POST.get('data')
    print(json)
    resultado = {'resultado': [1,2,3,4,5]}
    return JsonResponse(resultado, safe=False)