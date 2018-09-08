from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages


from .forms import ContactForm, QuoteForm, AskMailForm
from core.utils import logger


class ContactFormView(View):
    ''' Contact View '''

    def post(self, request):
        ''' Get post form '''

        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_mail()
            messages.success(request, "Succesful send email!")
            return redirect('/?success=true')

        else:
            messages.success(request, "We found an error on the form, please fill up again and resend it")
            return redirect('contact')



class AskQuoteFormView(View):
    ''' Ask qoute form hadler '''

    def post(self, request):
        ''' Handle post  '''

        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = form.save()
            messages.success(request, "Succesful ask quote!")
            return redirect('/?success=true')
        else:
            logger.error("[AshQuote ERROR form]: {}".format(form.errors))
            messages.error(request, "We found some errors on the form, please fill up again and resend it")
            return redirect('home')


class AskMailFormView(View):
    ''' Ask qoute form hadler '''

    def post(self, request):
        ''' Handle post  '''
        form = AskMailForm(request.POST)

        if form.is_valid():
            form.send_mail()
            messages.success(request, "Succesful suscribed!")
            return redirect('/?success=true')
        else:
            logger.error("[AshQuote ERROR form]: {}".format(form.errors))
            messages.error(request, "Sorry wrong email, please try again")
            return redirect('home')




