from django.shortcuts import render, redirect
from api.query import Query
from modules.recaptcha import recaptcha


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')


def send_lead(request):
    if request.method == 'POST' and recaptcha(request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

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
        return redirect('index')


def thanks(request):
    return render(request, 'pages/thanks.html')
