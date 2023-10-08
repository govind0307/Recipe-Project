from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def veges(request):
    # print("printing hello moto")
    if request.method == "POST":
        data = request.POST
        
        vege_name = data.get('vege_name')
        vege_description = data.get('vege_description')
        vege_image = request.FILES.get('vege_image')
        
        vege.objects.create(
            vege_name = vege_name,
            vege_description = vege_description,
            vege_image = vege_image,
        )
        
        return redirect('/recipes/')
        
    queryset = vege.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(vege_name__icontains = request.GET.get('search'))
        
    context = {'veges': queryset}
        
    return render(request, "form.html", context)

def del_rec(request, id):
    queryset = vege.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_rec(request, id):
    queryset = vege.objects.get(id=id)
        
    if request.method == "POST":
        data = request.POST
        
        vege_name = data.get('vege_name')
        vege_description = data.get('vege_description')
        vege_image = request.FILES.get('vege_image')
        
        queryset.vege_name = vege_name
        queryset.vege_description = vege_description
       
        if vege_image:
            queryset.vege_image = vege_image
        queryset.save()
        return redirect('/recipes/')

    context = {'vege': queryset}
    return render(request, "updaterec.html", context)
    