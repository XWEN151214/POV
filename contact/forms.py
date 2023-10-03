from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        subject = 'Contact Form Submission'
        message = f'Name: {self.cleaned_data["name"]}\nEmail: {self.cleaned_data["email"]}\nMessage: {self.cleaned_data["message"]}'
        sender = self.cleaned_data['email']
        recipient = [settings.DEFAULT_FROM_EMAIL]  
        send_mail(subject, message, sender, recipient)