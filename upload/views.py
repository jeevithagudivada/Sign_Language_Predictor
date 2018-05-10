# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, shutil

def Form(request):
    return render(request, "upload/form.html", {})

def Upload(request):
	newpath = settings.BASE_DIR+'/media/input'
	'''
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	else:
		shutil.rmtree(newpath) 		
		os.makedirs(newpath)	
	'''
	

	for count, x in enumerate(request.FILES.getlist("files")):
		extension = os.path.splitext(x.name)[1]			
		with open(newpath+'/input'+extension.lower(), 'wb+') as destination:
				for chunk in x.chunks():
					destination.write(chunk)	
	
	#return HttpResponse("File(s) uploaded!")
	return HttpResponseRedirect("/result/index")
    
