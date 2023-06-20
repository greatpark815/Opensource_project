from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    
    path('',views.main, name="main"),
    path('info_NC',views.info_NC,name="info_NC"),
    path('info_FC',views.info_FC,name="info_FC"),
    path('info_Jangseong',views.info_Jangseong,name="info_Jangseong"),
    path('success',views.complete,name="complete")
]
