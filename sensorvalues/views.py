#Importing models and render,http response(from database)
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers

#Function for login page
tem=[]
hum=[]
ult=[]
year=[]
day=[]
hour=[]
minute=[]
month=[]
rain=[]

def login(request):
    return render(request,'sensorvalues/login.html')
def plantmap(request):
	received_data=Plant.objects.all()[len(Plant.objects.all())-1]
	data=Plant.objects.all()[len(Plant.objects.all())-2]
	received11_data=weather.objects.all()[len(weather.objects.all())-1]
	rain_data=str(received11_data.rain)
	moisture=str(data.moisture)
	moisture1=str(received_data.moisture)
	z=plantid.objects.all()[len(plantid.objects.all())-1]
        number=str(z.pid)
        k=int(number)
        x=plantid.objects.all()[len(plantid.objects.all())-k]
	y=plantid.objects.all()[len(plantid.objects.all())-k+1]
	u=str(x.latitude)
	r=str(x.longitude)
	s=str(y.latitude)
	t=str(y.longitude)
	context={'moist':moisture,'moist11':moisture1,'rain':rain_data,'u':u,'r':r,'s':s,'t':t}
	return render(request,'sensorvalues/plantmap.html',context)
        
def index(request):
        #Retriving past 8 objects from database where each object contains all sensors values of Plant1
	received_data=weather.objects.all()[len(weather.objects.all())-1]
	temperature=str(received_data.temperature)
	humidity=str(received_data.humidity)
	context={'tem':temperature,'hum':humidity}
	return render(request,'sensorvalues/index.html',context)
def detail(request,pid1):

  
	h = (list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',Plant.objects.filter(pid=pid1)))))[::-1])
	h1 = (list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',plantid.objects.filter(pid=pid1)))))[::-1])
	received_data=weather.objects.all()[len(weather.objects.all())-1]
	temp=str(received_data.temperature)
	hum=str(received_data.humidity)
	rain=str(received_data.rain)
	ult=str(received_data.waterlevel)
	if len(h) == 0:
		return render(request, "sensorvalues/detail.html",{'moisture':"None",'ph':"None",'pid':pid1,'tem':temp,'hum':hum,'rain':rain,'ult':ult})
        #return JsonResponse({"loc":html, "values":html1}, safe=False)
	return render(request, "sensorvalues/detail.html",{'moisture':h[0]['fields']['moisture'],'ph':h[0]['fields']['ph'],'pid':pid1,'tem':temp,'hum':hum,'rain':rain,'ult':ult})

def getdata(request):
        #Using GET request method for getting sensor values from sensor.py file 
	if request.method=='GET' :
                #Storing the values 
		tem_value=request.GET['sensorvalues']
		hum_value=request.GET['humidity']
		moisture=request.GET['soilmoisture']
		moisture1=request.GET['soilmoisture1']
		ult_value=request.GET['ultrasonic']
		rain_value=request.GET['rain']
		year=request.GET['year']
		month=request.GET['month']
		day=request.GET['day']
		hour=request.GET['hour']
		minute=request.GET['minute']
		ph=request.GET['ph']
		
		w = weather.objects.create(temperature=tem_value,humidity=hum_value,waterlevel=ult_value,rain=rain_value,day=day,month=month,year=year,hour=hour,minute=minute)
		p = Plant.objects.create(pid=plantid.objects.get(pid=1),moisture=moisture,ph=ph)
		p.save()
		p1 = Plant.objects.create(pid=plantid.objects.get(pid=2),moisture=moisture1,ph=ph)
		p1.save()
                #Creating objects t,t1 in database
	
		#If data is stored succesfully then ot will return that data saved in db
		return HttpResponse("data saved in db")
	else:
                #Otherwise it will return error
		return HttpResponse("error")
         	#Template is rendered with request and context
@csrf_exempt
def addplant(request):
   
        if request.method == "POST":
           
            latitude = request.POST['a2']
            longitude = request.POST['a3']
            p = plantid.objects.count()
            plant = plantid.objects.create(pid = p+1,latitude = latitude,longitude = longitude)
            plant.save()
            return HttpResponse("Successfully saved")
            
        return render(request,'sensorvalues/addplant.html')

def temp(request):
         
	#for i in range(1,2):
	received_data=weather.objects.all()[weather.objects.count()-8:weather.objects.count()]
				
	context={'received_data':received_data}
	
	return render(request,'sensorvalues/temp.html',context)    	#Template is rendered with request and context
def hum(request):
         #Retriving past 8 objects from database where each object contains all sensors values of Plant1
	
	received_data=weather.objects.all()[weather.objects.count()-8:weather.objects.count()]
			    
				
	
	context={'received_data':received_data}
	return render(request,'sensorvalues/hum.html',context)      	#Template is rendered with request and context
def moist(request):
         #Retriving past 8 objects from database where each object contains all sensors values of Plant1
	
	received_data=Plant.objects.all()[Plant.objects.count()-8:weather.objects.count()]
				
				
	context={'received_data':received_data}
	
	
	return render(request,'sensorvalues/moist.html',context)    	#Template is rendered with request and context
def ult(request):
	
	received_data=weather.objects.all()[weather.objects.count()-8:weather.objects.count()]
				
				
	context={'received_data':received_data}	
	return render(request,'sensorvalues/ult.html',context)          	#Template is rendered with request and context
def rain(request):
         #Retriving past 8 objects from database where each object contains all sensors values of Plant1
	
	received_data=weather.objects.all()[weather.objects.count()-8:weather.objects.count()]
				
				
	context={'received_data':received_data}
	return render(request,'sensorvalues/rain.html',context)    	#Template is rendered with request and context






