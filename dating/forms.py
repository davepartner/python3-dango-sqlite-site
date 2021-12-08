from django import forms

# from .models import Facilitator

class RegistrationForm(forms.Form):
    # class Meta:
    #     model = Facilitator
    #     fields = ['email']
    email = forms.EmailField(label='Your email')