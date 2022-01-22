from django import forms

class send_form(forms.Form):
    phonenumber = forms.CharField(min_length=11,max_length=11,label='phone number :',required=True)
    message = forms.CharField(widget=forms.Textarea,min_length=500,label="your message:",required=True)
    
