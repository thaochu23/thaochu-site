from django.shortcuts import render
from .models import Device
from home.models  import Post
from django.http import HttpResponse

import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def on_off_Device(request):
	if request.session.has_key('username'):
		if 'on_motor' in request.POST:
			GPIO.output(pin, 1)
		elif 'off_motor' in request.POST:
			GPIO.output(pin, 0)
		return render(request, 'motor/action.html')
	else:
		return render(request, '/')

# Create your views here.
def motor_motor(request):
	if request.session.has_key('username'):
		return render(request, 'motor/motor.html', {'Devices': Device.objects.all(), 'posts': Post.objects.all()})
	else:
		return render(request, '')
def controlDevice(request, id):
	if request.session.has_key('username'):
		device_action = Device.objects.get(id=id)
		return render(request, 'motor/action.html', {'device_action': device_action})
	else:
		return render(request, '')
