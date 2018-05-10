# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os, shutil, json
from django.http import JsonResponse
from result.ASL import predict, cam_predict

# processing here (ooen Result Link)
def Index(request):
	translateResult = predict()
	return render(request, "result/index.html", {'result':translateResult})
	#return HttpResponse("<h1>"+translateResult+"</h1>")

def CamPredict(request):
	translate = cam_predict()	
	data = {'letter':translate}
	json_str = json.dumps(data)
	resp = json.loads(json_str)	
	return JsonResponse(resp['letter'], safe=False)

    