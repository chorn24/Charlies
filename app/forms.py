from django import forms


class ApplyForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    InputEmail = forms.CharField()
    Phone = forms.IntegerField()
