from django import forms


class ApplyForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    InputEmail = forms.CharField()
    Phone = forms.IntegerField()

class MenuForm(forms.Form):
    CPizza = forms.FloatField()
    PPizza = forms.FloatField()
    SPizza = forms.FloatField()
    MPizza = forms.FloatField()
    CSandwich = forms.FloatField()
    GSandwich = forms.FloatField()
    FSandwich = forms.FloatField()
    TSandwich = forms.FloatField()
    PSoup = forms.FloatField()
    TSoup = forms.FloatField()
    VSoup = forms.FloatField()
    MSoup = forms.FloatField()
    GGSalad = forms.FloatField()
    CSalad = forms.FloatField()
    GSalad = forms.FloatField()
    GASalad = forms.FloatField()