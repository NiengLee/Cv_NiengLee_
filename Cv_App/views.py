from django.shortcuts import render, redirect
from .models import msg_user

# Create your views here.
def index(request):
    if request.method=="GET":
        
        return render(request, 'index.html')

    else:
        msg_user.objects.create(nombre=request.POST['nombre'], mail=request.POST['email'], asunto=request.POST['asunto'], mensaje=request.POST['mensaje'])

        return redirect('gracias')

def gracias(request):

    return render(request,'gracias.html')