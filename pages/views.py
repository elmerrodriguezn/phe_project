from django.shortcuts import render, redirect
from pages.api_queries import *

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def send_lead(request):
    fullName = request.GET.get('fullName', False)
    email = request.GET.get('email', False)
    phone = request.GET.get('phone', False)
    msg = request.GET.get('msg', False)
    create_lead(fullName, email, phone, msg)
    return redirect('/gracias-por-contactarnos/')
    
def thanks(request):
    return render(request, 'pages/thanks.html')