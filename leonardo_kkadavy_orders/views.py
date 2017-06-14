# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from leonardo.decorators import require_auth
from django.db import transaction
from leonardo import forms, messages
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from .models import KkadavyOrders, KkadavyProducts
from .forms import KkadavyOrderFormSet
from leonardo.forms.views import CreateView


class KkadavyOrderCreate(CreateView):
    model = KkadavyOrders
    fields = ['jmeno', 'prijmeni', 'telefon', 'email']
    template_name = "leonardo_kkadavy_orders/kkadavyorders_form.html"

    def get_context_data(self, **kwargs):
        data = super(KkadavyOrderCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['orderproducts'] = KkadavyOrderFormSet(self.request.POST)
        else:
            data['orderproducts'] = KkadavyOrderFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderproducts = context['orderproducts']
        with transaction.atomic():
            self.object = form.save()

            if orderproducts.is_valid():
                orderproducts.instance = self.object
                orderproducts.save()
        return super(KkadavyOrderCreate, self).form_valid(form)

