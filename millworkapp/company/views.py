from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages


from .forms import ContactForm

class ContactFormView(View):
    ''' Contact View '''

    def post(self, request):
        ''' Get post form '''

        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_mail()
            messages.success(request, "Succesful send email!")
            return redirect('home')

        else:
            messages.success(request, "We found an error on the form, please fill up again and resend it")
            return redirect('contact')


