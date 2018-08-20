# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sampleapp.tasks import test_celery

def home(request):
    test_celery.delay()
    return HttpResponse("Celery Demo!!")



