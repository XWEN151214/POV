from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Notifying admin that someone has contacted via contact form

            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']

            # subject = 'New Contact Form Submission'
            # message = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'

            # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


