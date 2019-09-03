from django.shortcuts import render, redirect
from api.query import Query


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')


def send_lead(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']

    query = Query()

    data = query.create(
        'crm.lead', 'create',
        {
            'name': 'plate-heat-exchanger.com.mx',
            'contact_name': full_name,
            'email_from': email,
            'phone': phone,
            'description': msg
        })

    return redirect('/gracias-por-contactarnos/')


def thanks(request):
    return render(request, 'pages/thanks.html')
