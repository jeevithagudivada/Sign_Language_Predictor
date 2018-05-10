# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, shutil
import base64
from base64 import decodestring
import re, io, json
from binascii import a2b_base64
from result.ASL import cam_predict
from django.http import JsonResponse
from random import randint
from django.views.decorators.csrf import csrf_exempt
import time



def Take(request):
    return render(request, "cam/camera.html", {})

def Capture(request):

	datauri = request.POST['imageDataField']
	'''
	datauri.replace(' ', '+')
	#dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
	datauri.replace('data:image/jpeg;base64,', '')
	#image_data = dataUrlPattern.match(datauri).group(2)
	image_data = datauri.encode()
	data = base64.b64decode(image_data)
	
	#imgData = datauri.split(",")[1]
	#imgData = imgData.replace(' ', '+');
	
	#imgdata = imgdata.encode()
	#imgdata = base64.b64decode(imgData.encode())

	#imgData= base64.b64encode(imgData.encode('utf-8'))
	
	#print (request.FILES)	
	newpath = settings.BASE_DIR+'/media/cam/cam.jpg'
	
	
	with open(newpath, 'wb+') as f:
		f.write(data)
	#fh.write(datauri.split(",")[1].decode('base64'))
	#output = open(newpath, 'wb')
	#output.write(img_str)
	#base64.decodestring(image_64_encode)
	

	
	#output.close()
	'''
	newpath = settings.BASE_DIR+'/media/cam/cam.jpg'
	data_url_pattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
	signature_data = data_url_pattern.match(datauri).group(2)
	
	signature_data = bytes(signature_data, 'UTF-8')
	signature_data = decodestring(signature_data)
	f = open(newpath, 'wb')
	f.write(signature_data)
	f.close()
	
	return HttpResponse(signature_data)

	#return HttpResponseRedirect("/result/index")

@csrf_exempt
def AutoCapture(request):
	datauri = request.POST['imgBase64']
	#datauri = request.POST['imageDataField']	
	#json_data = json.loads(request.body)
	#datauri = json_data['imgBase64']
	newpath = settings.BASE_DIR+'/media/cam/cam.jpg'
	data_url_pattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
	signature_data = data_url_pattern.match(datauri).group(2)
		
	signature_data = bytes(signature_data, 'UTF-8')
	signature_data = decodestring(signature_data)
	f = open(newpath, 'wb')
	f.write(signature_data)
	f.close()
		
	translate = cam_predict()	
	data = {'letter':translate}
	json_str = json.dumps(data)
	resp = json.loads(json_str)	
	#return JsonResponse(resp['letter'], safe=False)
	return JsonResponse(resp['letter'], safe=False)
	'''
	randomNumber = randint(1, 8)
	data = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'G'}
	#dict([(1, 2), (3, 4)])
	#data={"peter" : "1", "flora" : "2", "tam" : "3"}
	json_str = json.dumps(data)
	resp = json.loads(json_str)

	
	return JsonResponse(resp[str(randomNumber)], safe=False)

	'''

	#return HttpResponseRedirect("/result/index")
    
