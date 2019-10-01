from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'portfolio/home.html')

def portfolio(request):
    return render(request,'portfolio/portfolio_page.html')

def about(request):
    return render(request,'portfolio/about.html')


    
