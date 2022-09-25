from socket import fromshare
from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(label='Your Name',label_suffix=" ",initial="")
    email=forms.EmailField(help_text="limit 20 characters")
    mobile=forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput,required=False)