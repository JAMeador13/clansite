from django import forms

class NameForm(forms.Form):
    clan_name = forms.CharField(label='Clan name', max_length=25)
