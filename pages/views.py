from django.shortcuts import render, redirect
from api.query import Query
from modules.recaptcha import recaptcha
from django.contrib import messages


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')


def send_lead(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['msg']

    if request.method == 'POST' and recaptcha(request) and '' not in (full_name, email, phone, msg):
        query = Query()

        data = query.create(
            'crm.lead', 'create',
            {
                'name': 'plate-heat-exchanger.com.mx',
                'user_id': 110,
                'contact_name': full_name,
                'email_from': email,
                'phone': phone,
                'description': msg
            })

        return redirect('thanks')
    else:
        messages.add_message(request, messages.INFO, 'Favor de llenar los campos con la información correcta.')
        return redirect('contact')


def thanks(request):
    return render(request, 'pages/thanks.html')
