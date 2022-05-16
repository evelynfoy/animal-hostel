''' urls for Home Animal app '''

from django.urls import path
from . import views


urlpatterns = [
    path('', views.GuestList.as_view(), name='home'),
    path('guest_detail/<slug:slug>/', views.GuestDetail.as_view(), name='guest_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]