from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from EncenderLed.models import iluminacion

def EncenderLed(request):
	variableON = request.GET.get('B_ON', '')
	variableOFF = request.GET.get('B_OFF', '')
	if variableON and variableON == 'True':  
		b = iluminacion.objects.get(id=1)
		b.led=1
		b.save()
		ON=1
		return render(request, 'encender_led.html',{'var': 'bombillaON'})
	if variableOFF and variableOFF == 'False':
		b = iluminacion.objects.get(id=1)
		b.led = 0
		b.save()
		OFF=0
		return render(request, 'encender_led.html',{'var': 'bombillaOFF'})
	b = iluminacion.objects.get(id=1)
	if b.led==1:
		return render(request, 'encender_led.html', {'var': 'bombillaON'}) 
	if b.led==0:
		return render(request, 'encender_led.html', {'var': 'bombillaOFF'})
	return render(request, 'encender_led.html', {'var1': b.led})

	#crear página de error: 'error.html'
