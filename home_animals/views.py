''' Views '''
from django.shortcuts import render
from django.views import View
from .models import Animal


class GuestList(View):
    ''' Guest List '''
    template_name = 'index.html'

    def get(self, request):
        ''' Get view for displaying the Guests '''
        animal = Animal.objects.order_by('name')
        return render(request, self.template_name,
                      {'animal_list': animal})
