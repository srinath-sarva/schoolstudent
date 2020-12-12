from django.shortcuts import render
from django.http import HttpResponse
from .models import *

mark=marks.objects.all()
students=student.objects.all()
   

for i in mark:
    sum=i.social+i.science+i.english+i.maths+i.physics 
    i.total=sum 
  
def login(request):
    return render(request,"accounts/login.html")
def register(request):
    return render(request,"accounts/register.html")
def  studentdetails(request):
    

        
    
    return render(request,"accounts/studentdetails.html",{'students':students,'marks':mark})

def  studentmarks(request):
    
    return render(request,"accounts/studentmarks.html",{"students":students,"marks":mark})

def activate(request):
    if request.method=="POST":
        pame=request.POST["student"]
        print(pame)
    for i in mark:
        if(i.regid.name==pame):
            name=i.regid.name
            email=i.regid.email
            social=i.social 
            regid=i.regid.regid
            gender=i.regid.gender 
            break 
            

    return render(request,"accounts/studentdetails.html",{"students":students,"name":name,"social":social,"email":email,"gender":gender,"regid":regid,"i":i})



