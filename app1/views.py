from django.shortcuts import render

# Create your views here.
def getloginpage(request):
    return render(request,'login.html')

def getmasterpage(request):
    return render(request,'master.html')  

def getchangepassword(request):
    return render(request,'changepassword.html') 

def getsettingspage(request):
    return render(request,'settings.html')  

def getprofilepage(request):
    return render(request,'profile.html')          
