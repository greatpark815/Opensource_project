from django.urls import path
from . import views

app_name = "sign"
urlpatterns = [
    path("",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("signup",views.signup_view,name="signup"),
    path("gotomain",views.gotomain,name="gotomain"),
    
]