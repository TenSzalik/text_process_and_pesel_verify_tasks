from django.http import HttpResponseBadRequest
from django.shortcuts import render

from domain.entities.pesel_entity import PeselEntity
from domain.managers.pesel_manager import PeselManager
from pesel_validator.forms import PESELForm


def pesel_validator_view(request):
    if request.method == "POST":
        form = PESELForm(request.POST, request.FILES)
        if form.is_valid():
            pesel_data = form.cleaned_data["pesel"]
            pesel_entity = PeselEntity(pesel_data)
            pesel = PeselManager(pesel_entity)

            if not pesel.is_valid():
                return HttpResponseBadRequest("Invalid PESEL")
            else:
                return render(
                    request,
                    "pesel_validator_result.html",
                    {
                        "pesel": f"PESEL is valid \n Data: {pesel.get_birth_date()}, gender: {pesel.get_gender()}"
                    },
                )

    else:
        form = PESELForm()
    return render(request, "pesel_validator_form.html", {"form_pesel": form})
