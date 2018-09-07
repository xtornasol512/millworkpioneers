import logging
from django import forms
from django.core.mail import send_mail

from .models import Quote

logger = logging.getLogger('django')

class SuscriptionForm(forms.Form):
    ''' Suscription Form '''
    email = forms.EmailField(label='Your email here', max_length=100, required=True)


    def clean_email(self, cleaned_data):
        ''' Clean email '''
        email = cleaned_data['email']


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
            from_email = "hello@millworkpioneers.com"
            to_email = "xtornasol512@gmail.com"

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

        except Exception as e:
            logger.error("[Send email ERROR]:  {}, type:{}".format(e, type(e)))

        else:
            logger.info("Success send email from :{}, email:{}".format(name, email))





class QuoteForm(forms.ModelForm):
    ''' Quote Form '''

    class Meta:
        model = Quote
        fields = [
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




