''' Forms for Millworkpioneer project '''
from django import forms
from django.conf import settings
from django.core.mail import send_mail

from core.utils import logger
from .models import Quote


class ContactForm(forms.Form):
    '''  Contact form '''
    name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        ''' Send emails '''
        try:
            subject = "Contact Form Request"
            name = self.cleaned_data["name"]
            email = self.cleaned_data["email"]
            message = self.cleaned_data["message"]
            from_email = settings.WORKING_EMAIL
            to_email = settings.ADMIN_EMAIL

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success send email from :{}, email:{}".format(name, email))


class AskMailForm(forms.Form):
    '''  Contact form '''
    ask_email = forms.EmailField(required=True)

    def send_mail(self):
        ''' Send email '''
        try:
            email = self.cleaned_data["ask_email"]
            subject = "Ask Email"
            message = "Somebody ask for suscription: {}".format(email)
            from_email = settings.WORKING_EMAIL
            to_email = settings.ADMIN_EMAIL

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))
            raise e

        else:
            logger.info("Success receive email:{}".format(email))


class QuoteForm(forms.ModelForm):
    ''' Quote Form '''

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    bid_due = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

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


INSTALLATION_CHOICES = (
    ('UNION', 'Union'),
    ('SEEKING SPONSORSHIP', 'Seeking Sponsorship'),
)

OFFICE_CHOICES = (
    ('ESTIMATING DEPARTMENT', 'Estimating Department'),
    ('PROJECT MANAGEMENT', 'Project Management'),
    ('HR DEPARTMENT', 'HR Department'),
    ('IT DEPARTMENT', 'IT Department'),
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
    message = forms.CharField(max_length=300,widget=forms.Textarea)
    installation = forms.ChoiceField(choices=INSTALLATION_CHOICES)
    union_ubc_number = forms.CharField(max_length=100, required=False)
    office = forms.ChoiceField(choices=OFFICE_CHOICES)
    finish_carpenter = forms.ChoiceField(choices=FINISH_CARPENTER_CHOICES)
    years_of_experience = forms.CharField(max_length=20, required=False)

    def send_mail(self):
        ''' Custom send mail for career form  '''
        try:
            email = self.cleaned_data["email"]
            name = self.cleaned_data["name"]
            subject = "Career application form, email:{}, name: {}".format(email, name)
            message = "Somebody send an application from website: {}".format(email)
            from_email = settings.WORKING_EMAIL
            to_email = settings.ADMIN_EMAIL

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success receive email:{}".format(email))




