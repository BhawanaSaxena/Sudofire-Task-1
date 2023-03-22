from django.urls import path, include
#from .views import apifunc,home_page
from api1.views import Companyviewset
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r"Companies",Companyviewset)

urlpatterns = [
 path("",include(router.urls))
 ]

 #     path("api1/",apifunc,name = "api1"),
#     path('home/',home_page)