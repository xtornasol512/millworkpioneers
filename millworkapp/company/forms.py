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
            raise e

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
        ]


INSTALLATION_CHOICES = (
    ('0', 'Union'),
    ('1', 'Seeking Sponsorship'),
)

OFFICE_CHOICES = (
    ('0', 'Estimating Department'),
    ('1', 'Project Management'),
    ('2', 'HR Department'),
    ('3', 'IT Department'),
    ('4', 'Basic Application'),
)


class CareerForm(forms.Form):
    ''' Career Form '''

    installation = forms.ChoiceField(choices=INSTALLATION_CHOICES)
    office = forms.ChoiceField(choices=OFFICE_CHOICES)




