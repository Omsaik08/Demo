from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student

def homepage(request):
    return render(request,'index.html')

def insert(request):
    if request.method=='POST':
        #print("yes")
        roll=request.POST['sroll']
        name=request.POST['sname']
        per=request.POST['sper']
    
        st=student(roll=roll,name=name,per=per)
        st.save()

        return redirect('/')
    else:
        return render(request,'insert.html')  

def show(request):
    data= student.objects.all()

    return render(request,'show.html',{'d':data})


def update(request):
        if request.method=='POST':
            ids=request.POST['id']
            roll=request.POST['nroll']
            name=request.POST['nname']
            per=request.POST['nper']
        
            student.objects.filter(id=ids).update(roll=roll,name=name,per=per)
            return redirect('/')
        else:
            return render(request,'update.html')  

def delete(request):
    if request.method=='POST':
            ids=request.POST['id']
            student.objects.filter(id=ids).delete()
            return redirect('/')
    else:
        return render(request,'delete.html')  

    
    


