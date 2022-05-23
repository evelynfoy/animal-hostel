""" Form """
from django import forms
from .models import Offer


class OfferForm(forms.ModelForm):
    """ Offer Form """
    class Meta:
        """ Meta """
        model = Offer
        fields = ('animal', 'pitch', 'basis', 'weeks')
