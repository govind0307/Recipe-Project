
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello")

def home1(request):
    return HttpResponse("Welcome to Recipe page.")


