from django import forms
from django.forms import ModelForm, fields
from notebook.models import Notebook

class NotebookForm(ModelForm):
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Enter Title"}))
    
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Enter Notes", "rows":"8"}))
    
    class Meta:
        model = Notebook
        fields = ['heading', 'text']