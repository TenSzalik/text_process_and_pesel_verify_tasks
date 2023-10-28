from django import forms


class PESELForm(forms.Form):
    """ Form dedicated for PESEL's number
    """
    pesel = forms.IntegerField()
