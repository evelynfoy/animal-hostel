''' Views '''
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Animal
# from .forms import GuestDetailForm


class GuestList(View):
    ''' Guest List '''
    template_name = 'index.html'

    def get(self, request):
        ''' Get view for displaying the Guests '''
        animal = Animal.objects.order_by('name')
        return render(request, self.template_name,
                      {'animal_list': animal})


class GuestDetail(View):

    ''' Guest List '''

    def get(self, request, slug, *args, **kwargs):
        queryset = Animal.objects
        guest = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "guest_detail.html",
            {
                "guest": guest,
            }
        )
