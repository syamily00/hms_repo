from django.urls import path
from . import views
app_name="firstapp"

urlpatterns=[
    path('login/',views.getloginpage,name="login_user"),
    path('login_master',views.getmasterpage,name="master"),
    path('changepassword/',views.getchangepassword,name="changepassword"),
    path('settings/',views.getsettingspage,name="settings"),
    path('profile/',views.getprofilepage,name="profile"),
    path('demo/',views.getdemopage,name="demo")
]