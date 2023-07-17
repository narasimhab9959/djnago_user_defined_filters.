from django.shortcuts import render

# Create your views here.




def Userdefined(request):
    d={'data':'nArasImha Is Full StacK DeveLopeR'}
    return render(request,'usdf.html',d)