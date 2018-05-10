# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

def Index(request):
    return render(request, "home/index.html", {})

def About(request):
    return render(request, "home/about.html", {})

def Contact(request):
    return render(request, "home/contact.html", {})

def Tutorial(request):
    return render(request, "home/tutorial.html", {})
