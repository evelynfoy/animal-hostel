""" Views """
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Animal, Offer
# from .forms import GuestDetailForm


class GuestList(View):
    """ Guest List """

    def get(self, request):
        """ Get view for displaying the Guests """
        animals = Animal.objects.order_by('name')
        return render(
            request,
            "pages/index.html",
            {
                "guest_list": animals
            }
        )


class GuestDetail(View):

    """ Guest List """

    def get(self, request, slug, *args, **kwargs):
        queryset = Animal.objects
        guest = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            'pages/guest_detail.html',
            {
                'guest': guest,
            }
        )


class OffersList(View):

    """ Offer List """

    def get(self, request):
        offers = Offer.objects.order_by('slug')
        # offer = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            'pages/offers.html',
            {
                'offers': offers,
            }
        )

