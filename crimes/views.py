# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from crimes.models import *

# Create your views here.


def analyze(request):
    if request.GET['crimeType']:
        crimeType = request.GET['crimeType']
        crimes = []
        if crimeType == 'Rape':
            crimes = Rape.objects.all()
        elif crimeType == 'SexualHarassment':
            crimes = SexualHarassment.objects.all()
        elif crimeType == 'AutoTheft':
            crimes = AutoTheft.objects.all()
        elif crimeType == 'SeriousFraud':
            crimes = SeriousFraud.objects.all()
        elif crimeType == 'Murder':
            crimes = Murder.objects.all()
        else:
            print('Error! Make sure you are reuqestiong an existing crime type!')

        return render(request, 'index-results.html', {'crimes': crimes})


def index(request):
    return render(request, "index.html")
