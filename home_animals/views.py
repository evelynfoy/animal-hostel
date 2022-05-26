""" Views """
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import Animal, Offer
from .forms import OfferCreateForm, OfferEditForm, OfferDeleteForm


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
        return render(
            request,
            'pages/offers.html',
            {
                'offers': offers,
            }
        )


class OfferAdd(View):
    """ Add Offer """
    def get(self, request):
        return render(
            request,
            'pages/offer_add.html',
            {
                "offer_form": OfferCreateForm(),
            }
        )

    def post(self, request, *args, **kwargs):
        offer_form = OfferCreateForm(data=request.POST)
        user = request.user.username
        id = request.POST.get('animal')
        queryset = Animal.objects
        guest = get_object_or_404(queryset, id=id)
        slug = str(user) + "-" + guest.slug
        if offer_form.is_valid():
            offer_form.instance.slug = slug
            offer_form.instance.user = request.user
            offer_form.instance.status = 'P'
            offer_form.save()
        else:
            offer_form = OfferCreateForm(data=request.POST)
        return redirect('offers')


class OfferEdit(View):
    """ Edit Offer """
    def get(self, request, slug, *args, **kwargs):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferEditForm(instance=offer)
        return render(
            request,
            'pages/offer_edit.html',
            {
                "offer_form": offer_form,
                "offer": offer
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferEditForm(request.POST, instance=offer)
        user = request.user.username
        if offer_form.is_valid():
            offer_form.save()
        else:
            offer_form = OfferEditForm(data=request.POST)
        return redirect('offers')


class OfferDelete(View):
    """ Delete Offer """
    def get(self, request, slug, *args, **kwargs):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferDeleteForm(instance=offer)
        return render(
            request,
            'pages/offer_delete.html',
            {
                "offer_form": offer_form,
                "offer": offer
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer.delete()
        return redirect('offers')

