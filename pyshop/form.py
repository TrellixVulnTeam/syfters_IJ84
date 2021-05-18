from django import forms


class contactForEmail(forms.Form):
    forEmail = forms.EmailField(required=True)
    name = forms.EmailField(required=True)
    message = forms.CharField(required=True)