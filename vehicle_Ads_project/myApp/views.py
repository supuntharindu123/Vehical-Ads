from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .form import RegisterForm,LoginForm,ResetPwdForm,UpdateProfileForm,UploadimgForm,PostAdForm,ContactForm,SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,update_session_auth_hash
from .models import Test,Ads,Faq
from django.core.mail import send_mail
import stripe
from django.http import HttpResponse

stripe.api_key="sk_test_51Qm6IMCGbMJ2nIHIbmmF1PV5xuo4850hZ8ys1LStv4myq2HkB6VWmasr1g573h8jAC8Ew8TdeZlSMMxYu7A4JQ2m00IZKbukCe"

# Create your views here.
def home(request):
    form=SearchForm()
    context={
        'form':form
    }
    return render(request, 'home.html',context)

def viewvehicle(request,pk):
    viewvehicle=Ads.objects.get(pk=pk)
    vehicle=Ads.objects.all()
    vehicle01=vehicle.filter(vehicle_type=viewvehicle.vehicle_type)
    vehicle02=vehicle.filter(vehicle_make=viewvehicle.vehicle_make)
    vehicle03=vehicle.filter(manufacture_year=viewvehicle.manufacture_year)

    if vehicle01 | vehicle02 | vehicle03:
        recent=vehicle01 | vehicle02 | vehicle03


    context={
        'viewvehicle':viewvehicle,
        'recent':recent
        
    }
    
    return render(request, 'view.html',context)


def vehicle(request,type):
    if type=='Car':
        ads=Ads.objects.filter(vehicle_type="Car").order_by('-date')
    elif type=='Motorcycle':
        ads=Ads.objects.filter(vehicle_type="Motorcycle").order_by('-date')
    elif type=='Truck':
        ads=Ads.objects.filter(vehicle_type="Truck").order_by('-date')
    elif type=='SUV':
        ads=Ads.objects.filter(vehicle_type="SUV").order_by('-date')
    elif type=='Van':
        ads=Ads.objects.filter(vehicle_type="Van").order_by('-date')
    elif type=='Three Wheel':
        ads=Ads.objects.filter(vehicle_type="Three Wheel").order_by('-date')
    elif type=='Bus':
        ads=Ads.objects.filter(vehicle_type="Bus").order_by('-date')
    elif type=='Tractor':
        ads=Ads.objects.filter(vehicle_type="Tractor").order_by('-date')
    elif type=='Other':
        ads=Ads.objects.filter(vehicle_type="Other").order_by('-date')
    else:
        ads = Ads.objects.all().order_by('-date')  
        
    
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            vehicle_type = form.cleaned_data.get('vehicle_type')
            vehicle_make = form.cleaned_data.get('vehicle_make')
            model = form.cleaned_data.get('model')
            min_manufacture_year = form.cleaned_data.get('Min_manufacture_year')
            max_manufacture_year = form.cleaned_data.get('Max_manufacture_year')
            min_price = form.cleaned_data.get('Min_price')
            max_price = form.cleaned_data.get('Max_price')

            # Build the query based on form fields
            ads = Ads.objects.all().order_by('-date')  # Start with the default ordering
            
            if vehicle_type != 'Select Type':
                ads = ads.filter(vehicle_type=vehicle_type)
            else:
                ads=ads
            if vehicle_make != 'Select Make':
                ads = ads.filter(vehicle_make=vehicle_make)
            else:
                ads=ads
            if model:   
                ads = ads.filter(model=model)
            if min_manufacture_year!="Select Min Year":
                ads = ads.filter(manufacture_year__gte=min_manufacture_year)
            else:
                ads=ads
            if max_manufacture_year!="Select Max Year":
                ads = ads.filter(manufacture_year__lte=max_manufacture_year)
            else:
                ads=ads
            if min_price:
                ads = ads.filter(price__gte=min_price)
            if max_price:
                ads = ads.filter(price__lte=max_price)

            if not ads:
                messages.error(request, "No results found")
            else:
                messages.success(request, "Search results found")

    context = {
        'ads': ads,
        'form': form
    }
    return render(request, 'vehicle.html', context)



def register(request):
    print("helloWorld")
    form=RegisterForm()
    print(form)
    if(request.method == 'POST'):
        form=RegisterForm(request.POST)
        if (form.is_valid()):
            messages.success(request,"Register Successfully")
            form.save()
            return redirect('login')
    
    context={
        'form':form,
    }
    return render(request,'register.html',context)


def updateuser(request):
    myuser=request.user
    print(myuser.first_name)
    form=UpdateProfileForm(instance=myuser)
    if(request.method == 'POST'):
        form=UpdateProfileForm(request.POST,instance=myuser)
        if (form.is_valid()):
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('profile')
    context={
        'form': form,
    }
    return render(request,'updateuser.html',context)

def login(request):
    form=LoginForm()
   
    if(request.method == 'POST'):
        form=LoginForm(request,request.POST)
        print(form)
        if (form.is_valid()):
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(username)
            user=authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"Login successfully !")
                return redirect('profile')
        else:
            messages.error(request,"Authentication failed !")      
    context={
        'form':form
    }
    return render(request,'login.html',context)

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    messages.success(request,"Logout successfully !")
    return redirect('login')



@login_required(login_url='/login')
def pwdReset(request):
    print(request.user)
    form=ResetPwdForm(request.user)
    if(request.method == 'POST'):
        form=ResetPwdForm(request.user,request.POST)
        if (form.is_valid()):
            messages.success(request,"Password Reset Successfully !")
            form.save()
            update_session_auth_hash(request,form.user)
            redirect('profile')
        else:
            messages.error(request,"Reset Failed!")
    context={
        'form':form,
    }
    return render(request, 'pwdReset.html',context)



@login_required(login_url='/login')
def profile(request):
    userpost=Ads.objects.filter(username=request.user).order_by('-date')

    context={
        'user':request.user,
        'userpost':userpost,
        'user':request.user
    }
    return render(request, 'profile.html',context)






@login_required(login_url='/login')
def postAds(request):
    
    myuser=request.user
    form=PostAdForm(initial={
    'username': myuser.username
})
    if (request.method=='POST'):
        form=PostAdForm(request.POST,request.FILES)
       
        if form.is_valid():
            ad = form.save(commit=False)
            ad.username = request.user.username
            ad.save()
            messages.success(request,"Advertisement posted successfully !")
            return redirect('profile')
        else:
            messages.error(request,"Advertisement failed to post !")
    context={
        'form':form,
    }
    return render(request, 'postads.html',context)

@login_required(login_url='/login')
def deletepost(request,pk):
    post=get_object_or_404(Ads,pk=pk)
    post.delete()
    messages.success(request,"Advertisement deleted successfully !")
    return redirect('profile')

@login_required(login_url='/login')
def updatepost(request,pk):
    post=get_object_or_404(Ads,pk=pk)
    print(post)
    form=PostAdForm(instance=post)
    if (request.method=='POST'):
        form=PostAdForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            ad=form.save(commit=False)
            ad.username = request.user.username
            ad.save()
            messages.success(request,"Advertisement updated successfully !")
            return redirect('profile')
        else:
            messages.error(request,"Advertisement failed to update !")
    context={
        'form':form
    }
    return render(request, 'editpost.html',context)

@login_required(login_url='/login')
def deleteuser(request):
    user=get_object_or_404(User,username=request.user)
    user.delete()
    post=Ads.objects.filter(username=request.user)
    post.delete()
    messages.success(request,"User deleted successfully !")
    return redirect('login')


def forgetpwd(request):
    return render(request,'')

@login_required(login_url='/login')
def contact(request):
    myuser=request.user
    form=ContactForm(instance=myuser)
    if request.method == 'POST' :
         form=ContactForm(request.POST)
         if (form.is_valid()):
             username=form.cleaned_data["username"]
             email=form.cleaned_data["email"]
             message=form.cleaned_data["message"]
             contact=form.save(commit=False)
             contact.username=myuser.username
             contact.email=myuser.email
             contact.save()
             send_mail(f"This Message from contact in VehicleAds.com by {username}",message,email,["supunkumarasena1125@gmail.com"])
             messages.success(request,"Contact form submitted successfully!")
             return redirect('vehicle')
         else:
             messages.error(request,"Contact form failed to submit!")
    context={
        'form':form
    }
    return render(request, 'contact.html',context)

def faq(request):
    faq=Faq.objects.all()
    context={
        'faq':faq
    }
    return render(request, 'faq.html',context)

def terms(request):
    return render(request, 'terms.html')
def aboutus(request):
    return render(request, 'aboutus.html')


