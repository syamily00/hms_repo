from django.shortcuts import render

# Create your views here.
def getregistrationpage(request):
    return render(request,'patient_registration.html')

def getprofilepage(request):
    return render(request,'patient_profile.html')

