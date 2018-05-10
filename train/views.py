# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os, shutil
from random import *

def Form(request):
    return render(request, "train/form.html", {})

def Upload(request):
	folder = request.POST['folder']
	#newpath = settings.BASE_DIR+'/media/'+ folder
	newpath = settings.BASE_DIR+'/result/tensorflow/tf_files/media/'+ folder
	
	'''
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	else:
		shutil.rmtree(newpath) 		
		os.makedirs(newpath)
	'''
	if not os.path.exists(newpath):
		os.makedirs(newpath)

	for count, x in enumerate(request.FILES.getlist("files")):
		extension = os.path.splitext(x.name)[1]			
		with open(newpath+'/'+folder+'_' + str(randint(500,100000))+extension.lower(), 'wb+') as destination:
				for chunk in x.chunks():
					destination.write(chunk)	
	
	return HttpResponse("File(s) uploaded!")
