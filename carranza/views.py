from django.shortcuts import render

def inicio (request):
    return render (request, "carranza/inicio.html")
def registro(request):
    return render(request,'carranza/formregistro.html')
def registrocoffee(request):
    return render(request,'carranza/registrocoffee.html')


# Create your views here.
