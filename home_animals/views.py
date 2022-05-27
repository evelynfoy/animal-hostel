""" Views """
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
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

    def get(self, request, slug):
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

    def post(self, request):
        offer_form = OfferCreateForm(data=request.POST)
        user = request.user.username
        guest_id = request.POST.get('animal')
        queryset = Animal.objects
        guest = get_object_or_404(queryset, id=guest_id)
        slug = str(user) + "-" + guest.slug
        offer = Offer.objects.filter(slug=slug)
        if offer:
            messages.add_message(request, messages.ERROR,
                                 'Offer already exists.')
            offer_form = OfferCreateForm(data=request.POST)
        else:
            if offer_form.is_valid():
                offer_form.instance.slug = slug
                offer_form.instance.user = request.user
                offer_form.instance.status = 'P'
                offer_form.save()
                messages.add_message(request, messages.SUCCESS,
                                    'Offer added successfully.')
            else:
                offer_form = OfferCreateForm(data=request.POST)
        return redirect('offers')


class OfferEdit(View):
    """ Edit Offer """
    def get(self, request, slug):
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

    def post(self, request, slug):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferEditForm(request.POST, instance=offer)
        if offer_form.is_valid():
            offer_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Offer changed successfully.')
        else:
            offer_form = OfferEditForm(data=request.POST)
        return redirect('offers')


class OfferDelete(View):
    """ Delete Offer """
    def get(self, request, slug):
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

    def post(self, request, slug):
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Offer deleted successfully.')
        return redirect('offers')
