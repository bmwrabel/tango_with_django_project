# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    html= 'Rango says hey there partner!<br/>' + '<a href="/rango/about">About</a>'
    return HttpResponse(html)

def about(request):
    html= 'Rango says here is the about page.<br/>' + '<a href="/rango/">Index</a>'
    return HttpResponse(html)