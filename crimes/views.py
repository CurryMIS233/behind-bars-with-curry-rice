# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from crimes.models import *
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Create your views here.


def area_crime_chart(request):
    def crime_type_to_readable_crime_type(crime_type):
        if crime_type == 'AgainstWomen':
            return 'Crimes against women'
        elif crime_type == 'AutoTheft':
            return 'Auto theft'
        elif crime_type == 'SeriousFraud':
            return 'Serious fraud'
        elif crime_type == 'Murder':
            return 'Murder'

    area = request.GET['area']
    crime_type = request.GET['crime_type']
    crimes = []

    if crime_type == 'AgainstWomen':
        crimes = AgainstWomen.objects.filter(area=area)
    elif crime_type == 'AutoTheft':
        crimes = AutoTheft.objects.filter(area=area)
    elif crime_type == 'SeriousFraud':
        crimes = SeriousFraud.objects.filter(area=area)
    elif crime_type == 'Murder':
        crimes = Murder.objects.filter(area=area)

    years = list(map(lambda crime: crime.year, crimes))
    counts = list(map(lambda crime: crime.count, crimes))

    bar_chart = px.bar(crimes, x=years, y=counts,
                       title=crime_type_to_readable_crime_type(crime_type) + " in " + area + " between 2001-2010", labels={'x': 'Year', 'y': 'Number of crimes'})
    plot = pio.to_html(bar_chart, include_plotlyjs=False, full_html=False)

    return render(request, 'area_crime_chart.html', {'plot': plot})


def select_area(request):
    if request.GET['crime_type']:
        crime_type = request.GET['crime_type']
        areas = []
        if crime_type == 'AgainstWomen':
            crimes = AgainstWomen.objects.all()
            areas = list(map(lambda crime: crime.area, crimes))
            # Eliminate the non-unique values
            areas = list(set(areas))
        elif crime_type == 'AutoTheft':
            crimes = AutoTheft.objects.all()
            areas = list(map(lambda crime: crime.area, crimes))
            areas = list(set(areas))
        elif crime_type == 'SeriousFraud':
            crimes = SeriousFraud.objects.all()
            areas = list(map(lambda crime: crime.area, crimes))
            areas = list(set(areas))
        elif crime_type == 'Murder':
            crimes = Murder.objects.all()
            areas = list(map(lambda crime: crime.area, crimes))
            areas = list(set(areas))
        else:
            print('Error! Make sure you are reuqestiong an existing crime type!')

        return render(request, 'select_area.html', {'areas': areas, 'crime_type': crime_type})


def select_crime(request):
    return render(request, "select_crime.html")
