from django.shortcuts import render
from django.views import View
from .forms import send_form
from .modules.sms_kave import make_sms
from django.http import HttpResponse, HttpResponseRedirect
from email import message

class sendsmsview(View):
    
    def post(self, request,*args,**kwargs):
        form = send_form(request.post)
        
        context={
            "form": form,
        }
        if form.is_valid():
            phonenumber = request.POST.get('phonenumber')
            message = request.POST.get('message')
            
            sms = make_sms(phonenumber, message)
            
            sms.send()
            
            context={
                "form":send_form(),
                "status":"sent",
            }
            return render(request,"sms.html",context)
        
        def get(self, request, *args, **kwargs):
            form = send_form()
            context ={
                "form":form,
            }
            return render(request,"sms.html",context)
            
            