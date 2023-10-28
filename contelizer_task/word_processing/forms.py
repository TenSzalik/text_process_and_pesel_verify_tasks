from django import forms


class WordProcessingForm(forms.Form):
    """ Form dedicated for content to shuffle
    """
    content = forms.FileField()
