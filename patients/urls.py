from django.urls import path
from . import views
app_name="patient"

urlpatterns=[
    path('patients/',views.getregistrationpage,name="patient_reg"),
    path('patients_profile',views.getprofilepage,name="profile")
]