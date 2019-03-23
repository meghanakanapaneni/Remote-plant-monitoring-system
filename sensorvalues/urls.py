#importing url and views 
from django.conf.urls import include,url             
from . import views
#creating a url patterns( i.e., the path of the html pages)
urlpatterns = [
    url(r'^$', views.login ,name = "index"),          
    url(r'^index', views.index ,name = "index"),
    url(r'^get/', views.getdata ,name ="get"),
    url(r'^detail.html/(?P<pid1>[0-9]+)/', views.detail, name='detail'),
    url(r'^plantmap',views.plantmap),
    url(r'^temp',views.temp),
    url(r'^hum',views.hum),
    url(r'^moist',views.moist),
    url(r'^ult',views.ult),
    url(r'^rain',views.rain),
    url(r'^addplant', views.addplant),
    url(r'^login.html',views.login),
]
