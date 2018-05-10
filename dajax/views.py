# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, shutil, json
from django.http import JsonResponse
from random import randint



def Form(request):
    return render(request, "dajax/form.html", {})

def Exchange(request):
	randomNumber = randint(1, 8)
	data = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'G'}
	#dict([(1, 2), (3, 4)])
	#data={"peter" : "1", "flora" : "2", "tam" : "3"}
	json_str = json.dumps(data)
	resp = json.loads(json_str)

	
	return JsonResponse(resp[str(randomNumber)], safe=False)
	#return HttpResponse("File(s) uploaded!")
	#return HttpResponseRedirect("/result/index")
    
