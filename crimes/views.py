# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from crimes.models import Rape

# Create your views here.

def all_rapes(request):
    rape_list = Rape.objects.all()
    return render(request, "demo.html", {'rape_list': rape_list})
