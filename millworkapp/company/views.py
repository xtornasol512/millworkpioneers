from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages


from .forms import ContactForm, QuoteForm, AskMailForm, CareerForm
from core.utils import logger
from website.models import CareersPage


class ContactFormView(View):
    ''' Contact View '''

    def post(self, request):
        ''' Get post form '''

        form = ContactForm(request.POST)

        if form.is_valid():
            form.send_mail()
            messages.success(request, "Successful send email!")
            return redirect('home')

        else:
            messages.success(
                request,
                "We found an error on the form, please fill up again and resend it")
            return redirect('contact')


class AskQuoteFormView(View):
    ''' Ask qoute form hadler '''

    def post(self, request):
        ''' Handle post  '''

        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save()
            attach_file = request.FILES.get("file", False)
            form.send_mail(attach_file)
            logger.info(F"[AskQuote Form Success]: {quote}")
            messages.success(request, "Successful ask quote!")
            return redirect('home')
        else:
            logger.error(F"[AskQuote ERROR form]: {form.errors}")
            messages.error(
                request,
                "We found some errors on the form, please fill up again and resend it")
            return redirect('home')


class AskMailFormView(View):
    ''' Ask qoute form hadler '''

    def post(self, request):
        ''' Handle post  '''
        form = AskMailForm(request.POST)

        if form.is_valid():
            form.send_mail()
            messages.success(request, "Successful subscribed!")
            return redirect('home')
        else:
            logger.error(F"[AshQuote ERROR form]: {form.errors}")
            messages.error(request, "Sorry wrong email, please try again")
            return redirect('home')


class CareersView(View):
    ''' Simple view '''
    template = 'website/careers.html'

    def get_page_settings(self):
        if CareersPage.objects.first():
            return CareersPage.objects.first()
        else:
            return None

    def get(self, request):
        return render(request, self.template, {
                "careers_page": self.get_page_settings(),
                "form": CareerForm(),
            }
        )

    def post(self, request):
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            attach_file = request.FILES.get("file", False)
            form.send_mail(attach_file)
            messages.success(
                request,
                "Thank you for your application! We'll contact you soon!")
            return redirect('home')
        else:
            logger.error(F"FOUND ERRORS ON CAREER FORM: {form.errors}")
            messages.error(
                request,
                "We found errors on form, please check them and try again!")
            messages.warning(request, F"{form.errors}")
            return render(request, self.template, {
                    "careers_page": self.get_page_settings(),
                    "form": CareerForm()
                }
            )
