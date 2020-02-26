from django.urls import path

from . import views 

urlpatterns=[
    path("",views.home,name="home"),
    path("add", views.add, name="add"),
    path("fourth", views.fourth, name="fourth"),
    path("fifth", views.fifth, name="fifth"),
    path("seventh", views.seventh, name="seventh"),
    path("eighth", views.eighth, name="eighth"),
    path("ninth", views.ninth, name="ninth"),
    path("tenth", views.tenth, name="tenth"),
    path("eleventh", views.eleventh, name="eleventh"),

]