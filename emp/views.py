from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
   if request.method == "POST":
      first_name = request.POST.get('firstname')
      last_name = request.POST.get('lastname')
      username = request.POST.get('username')
      password = request.POST.get('password')
      if first_name=="" and last_name=="" and username=="" and password=="":
        messages.error(request,"please fill all fields")
        return redirect('/')

      employ = User.objects.filter(username = username)
      if employ.exists():
         messages.error(request,"this name is already taken")
         return redirect('/')


      use = User.objects.create(

         first_name = first_name,
         last_name = last_name,
         username = username,
         
      )
      use.set_password(password)
      use.save()

      return redirect('/login/')
   return render(request,'regi.html',{})

def login_page(request):
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      if  username=="" and password=="":
       messages.error(request,"please fill all fields")
       return redirect("/login/")
      if not User.objects.filter(username = username).exists():
         messages.error(request,"invalid user")

      user = authenticate(username = username , password = password )
      if user is None:
         messages.error(request,"invalid submition")
      else:
         login(request,user)
         return redirect('/empdetail/')   

   return render(request,'login.html',)

def logout(request):
   return redirect('/login/')

@login_required(login_url="/")
def  empdetail(request):

   if request.method == "POST":
      employeename = request.POST.get('employeename')
      phone = request.POST.get('phone')
      email = request.POST.get('email') 
      age = request.POST.get('age')
      employeeresume = request.FILES.get('file')
      empphoto = request.FILES.get('empphoto')

      user = Employee.objects.create(
      employeename = employeename,
      phone = phone,
      email = email,
      age = age,
      employeeresume = employeeresume,
      empphoto= empphoto
        )
      user.save()
      return redirect('/employdata')
   
   
   return render(request,"empdetail.html",{})  

@login_required(login_url="/")
def empdata(request):
   employ = Employee.objects.all()
   if request.method == "POST":
      search = request.POST.get('search')
      if search:
         employ = employ.filter(employeename__icontains = search)
         
         
   return render(request,'employeedata.html',{'employ':employ})
def empdata1(request,id):
   employ = Employee.objects.get(id=id)
   return render(request,'empdat1.html',{'employ':employ})

def deletemployee(request,id):
   qureyset = Employee.objects.get(id = id)
   qureyset.delete()
   return redirect('/employdata')

# def search(request):
 
#    context = {}  # Initialize context

#    if request.method == "POST":
#       search = request.POST.get('search')
#       if search:
#          name = Employee.filter(employeename__icontains="rahul" )
#          context={
#          'name':name
#          }
      
#    return render(request,'search.html',context)
   

def update(request,id):
   employ = Employee.objects.get(id=id)

   if request.method=="POST":
      employeename = request.POST.get('employeename')
      phone = request.POST.get('phone')
      email = request.POST.get('email')

      employ.employeename = employeename
      employ.phone = phone
      employ.email = email
      employ.save()
      return redirect('/employdata')
   return render(request,'update.html',{'employ':employ})