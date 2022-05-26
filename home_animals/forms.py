""" Form """
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Offer


class OfferForm(forms.ModelForm):
    """ Offer Form """
    class Meta:
        """ Meta """
        model = Offer
        fields = ('animal', 'pitch', 'basis', 'weeks')
        labels = {
                    'animal': _('Guest'),
                    'pitch': _('Why I would make a great owner'),
                    'basis': _('Adoption or Fostering'),
                    'weeks': _('If fostering please enter number of weeks:')
                }