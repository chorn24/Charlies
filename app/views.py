from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from app.forms import ApplyForm, MenuForm


# Create your views here.
def hub(request: HttpRequest):
    return render(request, "index.html")


def giga(request: HttpRequest):
    return render(request, "Giga.html")


def bltg(request: HttpRequest):
    return render(request, "brycelovesthisguy.html")


def about_us(request: HttpRequest):
    return render(request, "about_us.html")


def contacts(request: HttpRequest):
    form = ApplyForm(request.GET)
    if form.is_valid():
        FirstName = form.cleaned_data["FirstName"]
        LastName = form.cleaned_data["LastName"]
        InputEmail = form.cleaned_data["InputEmail"]
        Phone = form.cleaned_data["Phone"]
        return render(
            request,
            "contacts.html",
            {
                "form": form,
                "FirstName": FirstName,
                "LastName": LastName,
                "InputEmail": InputEmail,
                "Phone": Phone,
            },
        )
    else:
        return render(request, "contacts.html")


def location_hour(request: HttpRequest):
    return render(request, "location_hour.html")


def menu(request):
    form = MenuForm(request.GET)
    if form.is_valid():
        CPizza = form.cleaned_data["CPizza"]
        PPizza = form.cleaned_data["PPizza"]
        SPizza = form.cleaned_data["SPizza"]
        MPizza = form.cleaned_data["MPizza"]
        CSandwich = form.cleaned_data["CSandwich"]
        GSandwich = form.cleaned_data["GSandwich"]
        FSandwich = form.cleaned_data["FSandwich"]
        TSandwich = form.cleaned_data["TSandwich"]
        PSoup = form.cleaned_data["PSoup"]
        TSoup = form.cleaned_data["TSoup"]
        VSoup = form.cleaned_data["VSoup"]
        MSoup = form.cleaned_data["MSoup"]
        GGSalad = form.cleaned_data["GGSalad"]
        CSalad = form.cleaned_data["CSalad"]
        GSalad = form.cleaned_data["GSalad"]
        GASalad = form.cleaned_data["GASalad"]
        if CPizza == None or CPizza == "":
            CPizza = 0
        if PPizza == None or PPizza == "":
            PPizza = 0
        if SPizza == None or SPizza == "":
            SPizza = 0
        if MPizza == None or MPizza == "":
            MPizza = 0
        if CSandwich == None or CSandwich == "":
            CSandwich = 0
        if GSandwich == None or GSandwich == "":
            GSandwich = 0
        if FSandwich == None or FSandwich == "":
            FSandwich = 0
        if TSandwich == None or TSandwich == "":
            TSandwich = 0
        if PSoup == None or PSoup == "":
            PSoup = 0
        if TSoup == None or TSoup == "":
            TSoup = 0
        if VSoup == None or VSoup == "":
            VSoup = 0
        if MSoup == None or MSoup == "":
            MSoup = 0
        if GGSalad == None or GGSalad == "":
            GGSalad = 0
        if CSalad == None or CSalad == "":
            CSalad = 0
        if GSalad == None or GSalad == "":
            GSalad = 0
        if GASalad == None or GASalad == "":
            GASalad = 0
        CPizzaTOTAL = CPizza * 4.00
        PPizzaTOTAL = PPizza * 5.00
        SPizzaTOTAL = SPizza * 6.00
        MPizzaTOTAL = MPizza * 4.50
        CSandwichTOTAL = CSandwich * 6.00
        GSandwichTOTAL = GSandwich * 5.50
        FSandwichTOTAL = FSandwich * 5.00
        TSandwichTOTAL = TSandwich * 4.50
        PSoupTOTAL = PSoup * 6.00
        TSoupTOTAL = TSoup * 6.00
        VSoupTOTAL = VSoup * 6.50
        MSoupTOTAL = MSoup * 4.50
        GGSaladTOTAL = GGSalad * 5.00
        CSaladTOTAL = CSalad * 5.00
        GSaladTOTAL = GSalad * 5.00
        GASaladTOTAL = GASalad * 5.00
        Total = (
            CPizzaTOTAL
            + PPizzaTOTAL
            + SPizzaTOTAL
            + MPizzaTOTAL
            + CSandwichTOTAL
            + GSandwichTOTAL
            + FSandwichTOTAL
            + TSandwichTOTAL
            + PSoupTOTAL
            + TSoupTOTAL
            + VSoupTOTAL
            + MSoupTOTAL
            + GGSaladTOTAL
            + CSaladTOTAL
            + GSaladTOTAL
            + GASaladTOTAL
        )
        return render(
            request,
            "menu.html",
            {
                "form": form,
                "Total": Total,
                "CPizza": CPizza,
                "PPizza":PPizza,
                "SPizza": SPizza,
                "MPizza": MPizza,
                "CSandwich": CSandwich,
                "GSandwich": GSandwich,
                "FSandwich": FSandwich,
                "TSandwich": TSandwich,
                "PSoup": PSoup,
                "TSoup": TSoup,
                "VSoup": VSoup,
                "MSoup": MSoup,
                "GGSalad": GGSalad,
                "CSalad": CSalad,
                "GSalad": GSalad,
                "GASalad": GASalad,
                "CPizzaTOTAL": CPizzaTOTAL,
                "PPizzaTOTAL": PPizzaTOTAL,
                "SPizzaTOTAL": SPizzaTOTAL,
                "MPizzaTOTAL": MPizzaTOTAL,
                "CSandwichTOTAL": CSandwichTOTAL,
                "GSandwichTOTAL": GSandwichTOTAL,
                "FSandwichTOTAL": FSandwichTOTAL,
                "TSandwichTOTAL": TSandwichTOTAL,
                "PSoupTOTAL": PSoupTOTAL,
                "TSoupTOTAL": TSoupTOTAL,
                "VSoupTOTAL": VSoupTOTAL,
                "MSoupTOTAL": MSoupTOTAL,
                "GGSaladTOTAL": GGSaladTOTAL,
                "CSaladTOTAL": CSaladTOTAL,
                "GSaladTOTAL": GSaladTOTAL,
                "GASaladTOTAL": GASaladTOTAL,
            },
        )
    else:
        Total = 9
        return render(request, "menu.html", {"Total": Total, "form": form})
