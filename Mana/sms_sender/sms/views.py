import os
from django.shortcuts import render
from sms.models import Contact
from sms.forms import ContactForm
from kavenegar import *
import dotenv
dotenv.read_dotenv()

API_KEY = os.environ.get('API_KEY')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'forms.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.content = form.cleaned_data['content']
            contact.number = form.cleaned_data['number']
            contact.save()
            context['result'] = 'Sms sent. Thank you for choosing us <3'

            api = KavenegarAPI(API_KEY)
            params = { 'sender' : '10008663', 'receptor': str(contact.number), 'message' : str(contact.content)}
            api.sms_send( params)

            return render(request, 'forms.html', context)
        return render(request, 'forms.html', context)

        


