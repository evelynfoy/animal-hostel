''' urls for Home Animal app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.GuestList.as_view(), name='home'),
    path('guest/<slug:slug>/', views.GuestDetail.as_view(), name='guest_detail'),
    path('offers/', views.OffersList.as_view(), name='offers'),
    path('offer/add/', views.OfferAdd.as_view(), name='add_offer'),
    path('offer/edit/<slug:slug>', views.OfferEdit.as_view(), name='edit_offer'),
    path('offer/delete/<slug:slug>', views.OfferDelete.as_view(), name='delete_offer'),
]
