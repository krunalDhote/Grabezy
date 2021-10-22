from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Contact,Electronic,Grocery,Fashion
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.

#Outer Pages
def entry(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        issue=request.POST['issue']
        if len(fname)<2 or len(lname)<2 or len(email)<10 or len(phone)<10 or len(issue)<4:
            params={'msg':'Something wents wrong, Fill the form Correctly!'}
            return render(request,'contact.html',params)
        else:
            contact=Contact(fname=fname,lname=lname,email=email,phone=phone,issue=issue)
            contact.save()
            params={'msg':'Thank For Contact Us'}
    return render(request,'contact.html')

def termofuse(request):
    return render(request,'termofuse.html')

def privacy(request):
    return render(request,'privacy.html')

def service(request):
    return render(request,'services.html')

#Inner Pages
@login_required(login_url='/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/')
def search(request):
    allProds=[]
    Products=[]
    query=request.GET['search']
    if len(query)>30:
        allProds=[]
    elif len(query)!=0:
        allProdsFname=Fashion.objects.filter(product_name__icontains=query)
        allProdsEname=Electronic.objects.filter(product_name__icontains=query)
        allProdsGname=Grocery.objects.filter(product_name__icontains=query)

        allProdsFcat=Fashion.objects.filter(catagory__icontains=query)
        allProdsEcat=Electronic.objects.filter(catagory__icontains=query)
        allProdsGcat=Grocery.objects.filter(catagory__icontains=query)

        Products=allProdsFname.union(allProdsFname,allProdsEname,allProdsFcat,allProdsEcat)
        n=len(Products)
        allProds.append([Products,range(1,n)])
    if len(Products)==0:
        allProds=[]
        messages.error(request,'Please search valid content')
    params={'allProds':allProds,'query':query}
    return render(request,'search.html',params)

@login_required(login_url='/')
def cart(request):
    return render(request,'cart.html')

@login_required(login_url='/')
def checkout(request):
    return render(request,'checkout.html')

@login_required(login_url='/')
def tracker(request):
    return render(request,'tracker.html')

#Product Pages
@login_required(login_url='/')
def electronics(request):
    allProds=[]
    catprod=Electronic.objects.values('catagory','id')
    cats={item['catagory'] for item in catprod}
    for cat in cats:
        prod=Electronic.objects.filter(catagory=cat)
        n=len(prod)
        allProds.append([prod,range(1,n)])
    params={'allProds':allProds}
    
    return render(request,'electronics.html',params)

@login_required(login_url='/')
def grocery(request):
    return render(request,'grocery.html')

@login_required(login_url='/')
def fashion(request):
    allProds=[]
    catprod=Fashion.objects.values('catagory','id')
    cats={item['catagory'] for item in catprod}
    for cat in cats:
        prod=Fashion.objects.filter(catagory=cat)
        n=len(prod)
        allProds.append([prod,range(1,n)])
    params={'allProds':allProds}
    return render(request,'fashion.html',params)

#Authentication Pages
def handlesignup(request):
    if request.method=='POST':
        #Get The Post Parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']

        #Check for errorneous inputs
        if len(username)>15:
            params={'msg':'Username must be under 15 character'}
            return render(request,'login.html',params)
        if username.isalnum(): #alphanumeric
            params={'msg':'Username must be alphanumeric ex: user@1,user_1,etc'}
            return render(request,'login.html',params)
        
        #create the user
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        params={'msg':'Your Grabezy account has been successfully created, Login Here!'}
        return render(request,'login.html',params)
    else:
        return HttpResponse('404 - Not Found')

def home(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            params={'msg':'Invalid username or password, Try again!'}
            return render(request,'login.html',params)
    else:
        return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/') 
def profile(request):
    return render(request,'profile.html')

