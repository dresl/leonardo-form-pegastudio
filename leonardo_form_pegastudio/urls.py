from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^objednavka/pridat/$', views.PegastudioOrderCreate.as_view(), name='objedn_list'),
]
