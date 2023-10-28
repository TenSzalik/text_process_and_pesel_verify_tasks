from django.http import HttpResponse
from django.shortcuts import render

from domain.entities.word_prcessing_entity import WordProcessingEntity
from domain.managers.word_processing_manager import WordProcessingManager
from .forms import WordProcessingForm


def word_processing_view(request):
    if request.method == "POST":
        form = WordProcessingForm(request.POST, request.FILES)
        if form.is_valid():
            text_binary = form.cleaned_data["content"].read()
            word_processing_entity = WordProcessingEntity(content=text_binary)
            modified_text = WordProcessingManager(
                word_processing_entity
            ).shuffle_content()
            return HttpResponse(modified_text)
    else:
        form = WordProcessingForm()

    return render(request, "word_processing/word_processing_form.html", {"form": form})
