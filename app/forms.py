from django import forms


class ApplyForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    InputEmail = forms.CharField()
    Phone = forms.IntegerField()

class MenuForm(forms.Form):
    CPizza = forms.IntegerField(required=False)
    PPizza = forms.IntegerField(required=False)
    SPizza = forms.IntegerField(required=False)
    MPizza = forms.IntegerField(required=False)
    CSandwich = forms.IntegerField(required=False)
    GSandwich = forms.IntegerField(required=False)
    FSandwich = forms.IntegerField(required=False)
    TSandwich = forms.IntegerField(required=False)
    PSoup = forms.IntegerField(required=False)
    TSoup = forms.IntegerField(required=False)
    VSoup = forms.IntegerField(required=False)
    MSoup = forms.IntegerField(required=False)
    GGSalad = forms.IntegerField(required=False)
    CSalad = forms.IntegerField(required=False)
    GSalad = forms.IntegerField(required=False)
    GASalad = forms.IntegerField(required=False)