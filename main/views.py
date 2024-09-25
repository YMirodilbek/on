from django.shortcuts import render
from .models import *
# Create your views here.

def Index(request,id):
    a = A.objects.get(id=id)
    context={
        'i':a
    }
    return render(request,"index.html",context)
