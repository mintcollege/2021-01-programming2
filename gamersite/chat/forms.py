from django import forms


class CreateMessage(forms.Form):
    message = forms.CharField(label='Your message', max_length=255, required=True)
    username = forms.CharField(label='Username', max_length=20, required=True)
    userage = forms.IntegerField(label='Age')