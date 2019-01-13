''' Forms for Millworkpioneer project '''
from django import forms
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives

from core.utils import logger
from .models import Quote


class ContactForm(forms.Form):
    '''  Contact form '''
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)

    def send_mail(self):
        ''' Send emails '''
        data = self.cleaned_data
        try:
            subject = F"[MillworkPioneers Website] Contact Form Request, by {data['name']}"
            message = F"""Somebody send an contact form request from website and below is the info:
                        Name: {data['name']}
                        Email: {data['email']}
                        Phone: {data.get('phone', 'N/A')}
                        Message:
                        {data.get('message', 'No message')}
                        """
            from_email = settings.WORKING_EMAIL
            to_email = settings.WORKING_EMAIL

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success send email from :{}, email:{}".format(data['name'], data['email']))


class AskMailForm(forms.Form):
    '''  Contact form '''
    ask_email = forms.EmailField(required=True)

    def send_mail(self):
        ''' Send email '''
        try:
            email = self.cleaned_data["ask_email"]
            subject = "[MillworkPioneers Website] ASK EMAIL: {}".format(email)
            message = "Somebody ask for suscription with his/her email: {}".format(email)
            from_email = settings.WORKING_EMAIL
            to_email = settings.WORKING_EMAIL

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success receive email:{}".format(email))


class QuoteForm(forms.ModelForm):
    ''' Quote Form '''

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    bid_due = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    file = forms.FileField(required=False)

    class Meta:
        model = Quote
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "project",
            "bid_due",
            "start_date",
            "prevailing_wage",
            "description",
        ]

    def send_mail(self, attach_file):
        ''' Send mail '''
        data = self.cleaned_data
        try:
            email = self.cleaned_data["email"]
            subject = "[MillworkPioneers Website] ASK QUOTE FORM: {}".format(email)
            message = F"""Somebody send a quote form from website and below is the info:
                        Name: {data['name']}
                        Email: {data['email']}
                        Phone: {data.get('phone', 'N/A')}
                        Company: {data['company']}
                        Project: {data.get('project', 'N/A')}
                        Bid Due: {data['bid_due'].strftime("%A, %d. %B %Y")}
                        Start Date: {data['start_date'].strftime("%A, %d. %B %Y")}
                        Prevailing Wage: {data.get('prevailing_wage', 'N/A')}
                        Description:
                        {data.get('description', 'No message')}
                        """
            from_email = settings.WORKING_EMAIL
            to_email = settings.WORKING_EMAIL

            sent_email = EmailMultiAlternatives(subject, message, from_email, [to_email])

            if attach_file:
                sent_email.attach(attach_file.name, attach_file.read(), attach_file.content_type)

            sent_email.send()

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success receive email:{}".format(email))


INSTALLATION_CHOICES = (
    ('UNION', 'Union'),
    ('SEEKING SPONSORSHIP', 'Seeking Sponsorship'),
)

OFFICE_CHOICES = (
    ('ESTIMATING DEPARTMENT', 'Estimating Department'),
    ('PROJECT MANAGEMENT', 'Project Management'),
    ('HR DEPARTMENT', 'HR Department'),
    ('IT DEPARTMENT', 'IT Department'),
    ('FINISH CARPENTER', 'Finish Carpenter'),
    ('FOREMAN', 'Foreman'),
    ('SAFETY MANAGEMENT', 'Safety Management'),
    ('BASIC APPLICATION', 'Basic Application'),
)

FINISH_CARPENTER_CHOICES =(
    ('YES', 'YES'),
    ('NO', 'NO'),

)


class CareerForm(forms.Form):
    ''' Career Form '''
    name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(max_length=300,widget=forms.Textarea, required=False)
    installation = forms.ChoiceField(choices=INSTALLATION_CHOICES)
    union_ubc_number = forms.CharField(max_length=100, required=False)
    office = forms.ChoiceField(choices=OFFICE_CHOICES)
    finish_carpenter = forms.ChoiceField(choices=FINISH_CARPENTER_CHOICES)
    years_of_experience = forms.CharField(max_length=20, required=False)

    def send_mail(self):
        ''' Custom send mail for career form  '''
        data = self.cleaned_data
        try:
            email = data["email"]
            name = data["name"]
            subject = F"[MillworkPioneers Website] Career application form, email:{data['email']}, name: {data['name']}"
            message = F"""Somebody send an application from website and below is the info:
                        Name: {data['name']}
                        Email: {data['email']}
                        Phone: {data.get('phone', 'N/A')}
                        Installation: {data['installation']}
                        Union or UBC number: {data.get('union_ubc_number', 'N/A')}
                        Office: {data['office']}
                        Finish carpenter: {data['finish_carpenter']}
                        Years of experience: {data.get('years_of_experience', 'N/A')}
                        Message:
                        {data.get('message', 'No message')}
                        """

            from_email = settings.WORKING_EMAIL
            to_email = settings.WORKING_EMAIL

            if settings.DEBUG:
                logger.info(F"EMAIL MSG: {message}")

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success receive email:{}".format(email))




