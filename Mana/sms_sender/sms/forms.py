from dataclasses import fields
from email import message
import imp
from pyexpat import model
from django import forms
from sms.models import Contact
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'content', 'number']
        
    def clean_number(self):
        number = self.cleaned_data['number']            
        pattern = '^(\+989|00989|09)\d{9}$'
        if re.match(pattern, number):
            return number
        message = 'number is not valid'
        raise forms.ValidationError(message)
