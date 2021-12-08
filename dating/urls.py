from django.http import request
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('dating/', views.index, name='dating'),
    path('', views.home, name='home'),
    path('dating-detail/success', views.confirm_registration, name='confirm-registration'),
    path('dating-detail/<slug:friend_slug>', views.dating_detail,
     name='dating-detail')
]