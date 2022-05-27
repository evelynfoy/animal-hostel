"""
    Contains all the main views for the home_animals application
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Animal, Offer
from .forms import OfferCreateForm, OfferEditForm, OfferDeleteForm


class GuestList(View):
    """
        Lists all the guests/animals in the database and renders them on the
        index.html page
    """

    def get(self, request):
        """
            Get function for the Guest List view.
            Retrieves the list of animals from the database in animal name
            order.
            Returns list of animal objects, request and index.html template to
            be rendered.
        """
        animals = Animal.objects.order_by('name')
        return render(
            request,
            "pages/index.html",
            {
                "guest_list": animals
            }
        )


class GuestDetail(View):

    """
        Displays a single guest/animal from the database and renders them on
        the guest_details.html page
    """

    def get(self, request, slug):
        """
            Get function for the Guest Detail view.
            Retrieves the animal selected from the database using slug
            passed in.
            Parameters:
                Request
                Slug field
            Returns:
                Animal model object
                Request object
                guest_detail.html template
        """
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

    """
        Lists all the offers in the database and renders them on the
        offers.html page
    """

    def get(self, request):
        """
            Get function for the Offers view.
            Retrieves the list of offers from the database for the user signed
            in.
            Parameters:
                Request
            Returns:
                List of Offer model objects
                Request object
                offers.html template
        """
        offers = Offer.objects.order_by('slug')
        return render(
            request,
            'pages/offers.html',
            {
                'offers': offers,
            }
        )


class OfferAdd(View):
    """
        Displays an empty offer form, validates details entered and
        adds an Offer model object to the database if valid.
        If offer already exists it sends a flash message.
    """
    def get(self, request):
        """
            Get function for the add offer view.
            Retrieves the offer selected from the database using slug
            passed in.
            Parameters:
                Request
                Slug field
            Returns:
                Request object
                offer_add.html template
                offer_form
        """
        return render(
            request,
            'pages/offer_add.html',
            {
                "offer_form": OfferCreateForm(),
            }
        )

    def post(self, request):
        """
            Post function for the add offer view.
            Creates an offer form from the data on the request passed it.
            Gets the user logged in.
            Generates a new slug field (animal name  + '-' + user name).
            Checks if an offer record already exists for that slug.
            If not and the form is valid then
                Sets the status to 'P' - Pending.
                Sets the user to the user logged in.
                Sets the slug to that generated.
                Saves the new offer to the database.
            Otherwise if record found for slug
                Send a flash message informing the user that the offer elready
                exists.
            Otherwise - form is invalid
                Returns Add offer page

            Parameters:
                Request
            Model:
                Offer
            Returns:
                redirects to offers view
        """
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
    """
        Retrieves the offer record for the slug passed in and
        displays the details on an offer form
    """

    def get(self, request, slug):
        """
            Get function for the edit offer view.
            Retrieves the offer selected from the database using the slug
            passed in.
            Creates an offer form from the data in the offer object.

            Parameters:
                Request
                Slug field
            Model:
                Offer
            Returns:
                Request object
                offer_edit.html template
                offer_form
                offer object
        """
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferEditForm(instance=offer)
        return render(
            request,
            'pages/offer_edit.html',
            {
                "offer_form": offer_form,
                "offer": offer,
            }
        )

    def post(self, request, slug):
        """
            Post function for the edit offer view.
            Retrieves the offer selected from the database using the slug
            passed in.
            Creates an offer edit form passing both the request data and
            the offer object retrieved.
            If the form is valid then the changed details are saved to the
            database and a flash message is sent to the user.
            Otherwise it returns the edit offer page.
            Then it redirects the user to the List Offers view

            Parameters:
                Request
            Model:
                Offer
            Returns:
                redirects to offers view
        """
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
    """
        Retrieves the offer record for the slug passed in and
        displays the details on an delete offer form.
        If the user clicks the delete button the offer is deleted,
        the user is returned to the List Offers view and a flash message
        is sent.
    """
    def get(self, request, slug):
        """
            Get function for the delete offer view.
            Retrieves the offer selected from the database using the slug
            passed in.
            Creates a delete offer form from the data in the offer object.

            Parameters:
                Request
                Slug field
            Model:
                Offer
            Returns:
                Request object
                offer_delete.html template
                offer_form
                offer object
        """
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer_form = OfferDeleteForm(instance=offer)
        return render(
            request,
            'pages/offer_delete.html',
            {
                "offer_form": offer_form,
                "offer": offer,
            }
        )

    def post(self, request, slug):
        """
            Post function for the delete offer view.
            Retrieves the offer selected from the database using the slug
            passed in.
            Deletes the offer retrieved from the database.
            Then it redirects the user to the List Offers view and sends a
            flash message.

            Parameters:
                Request
            Model:
                Offer
            Returns:
                redirects to offers view
        """
        queryset = Offer.objects
        offer = get_object_or_404(queryset, slug=slug)
        offer.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Offer deleted successfully.')
        return redirect('offers')
