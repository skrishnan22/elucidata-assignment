from django.conf.urls import url,include
from .views import upload,process_1,process_2

urlpatterns = [
    
    url(r'^upload/$',upload),
    url(r'^(?P<filename>.*)/process1/$',process_1),
    url(r'^(?P<filename>.*)/process2/$',process_2),
]
