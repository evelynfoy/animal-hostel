""" Contains three forms used by the Offer CRUD functionality """
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Offer


class OfferCreateForm(forms.ModelForm):
    """
        Defines the 'Make an Offer form' which alters the field names
        displayed to make the form more user friendly
        Based on Model : Offer
    """
    class Meta:
        """ Meta """
        model = Offer
        fields = ('animal', 'pitch', 'basis', 'weeks')
        labels = {
            'animal': _('Guest'),
            'pitch': _('Why I would make a great owner'),
            'basis': _('Adoption or Fostering'),
            'weeks': _('If fostering please enter number of weeks (optional):')
        }


class OfferEditForm(forms.ModelForm):
    """
        Defines the 'Edit form' which alters the field names
        displayed to make the form more user friendly.
        It does not include the Animal name so it cannot be altered
        Based on Model : Offer
    """
    class Meta:
        """ Meta """
        model = Offer
        fields = ('pitch', 'basis', 'weeks')
        labels = {
            'pitch': _('Why I would make a great owner'),
            'basis': _('Adoption or Fostering'),
            'weeks': _('If fostering please enter number of weeks (optional):')
        }


class OfferDeleteForm(forms.ModelForm):
    """
        Defines the 'Delete Offer form' which alters the field names
        displayed to make the form more user friendly.
        It does not include the Animal name so it cannot be altered.
        It also sets the fields displayed to disabled.
        Based on Model : Offer
    """
    class Meta:
        """ Meta """
        model = Offer
        fields = ('pitch', 'basis', 'weeks')
        labels = {
            'pitch': _('Why I would make a great owner'),
            'basis': _('Adoption or Fostering'),
            'weeks': _('If fostering please enter number of weeks (optional):')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pitch"].disabled = True
        self.fields["basis"].disabled = True
        self.fields["weeks"].disabled = True
