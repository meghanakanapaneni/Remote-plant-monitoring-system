#importing url and admin 
from django.conf.urls import include,url
from django.contrib import admin
#creating url patterns for the app sensorvalues
urlpatterns = [
    url(r'^sensorvalues/', include('sensorvalues.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('sensorvalues.urls'))
]

