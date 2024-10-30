from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.http import Http404

from django.db.models import Q 

def Homepage(request):
    
    
    return render(request,'Homepage.html')
    
    

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.warning(request, "Both username and password are required")
            return render(request, "loginPage.html")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect("Homepage")
        else:
            messages.warning(request, "Invalid username or password")
    
    return render (request,'loginpage.html')


def Registerpage(request):
    
     

    
    
    
    if request.method == 'POST':
        username = request.POST['username']
        
        email = request.POST['email']
        Profile_Pic = request.POST['Profile_Pic']
        confirm_password = request.POST['confirm_password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST.get('user_type')

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('Registerpage')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return redirect('Registerpage')
            else:
                user = CustomUser.objects.create_user(
                username=username,
                email=email,
                Profile_Pic=Profile_Pic,
                password=password,
                user_type=user_type,
                
                )
                
                if user_type=='recuriters':
                    recuritersProfileModel.objects.create(user=user)
                    
                elif user_type=='seeker':
                    seekerProfileModel.objects.create(user=user)
                    
                
                return redirect("loginpage")
        else:
            return redirect('loginpage')

    return render(request, 'Registerpage.html')

def logoutPage(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("loginpage")



def profilePage(request):
    
    
    return render(request, "profilePage.html", )


def add_job(request):
    if request.method == 'POST':
        user = request.user  
        title = request.POST.get('title')
        number_of_opening = request.POST.get('Number_of_opening')
        category = request.POST.get('category')
        job_descriptions = request.POST.get('Job_descriptons')
        skill = request.POST.get('skill')
        image = request.FILES.get('Image')

       
        job = Jobmodel(
            user=user,
            title=title,
            Number_of_opening=number_of_opening,
            category=category,
            Job_descriptons=job_descriptions,
            skill=skill,
            Image=image
        )
        
        
        job.save()

        return redirect('job_feed')  

    return render(request, 'add_job.html')

def created_JOb(request):
    jobs = Jobmodel.objects.all()  
    return render(request, 'created_JOb.html', {'jobs': jobs})

def job_feed(request):
    jobs = Jobmodel.objects.all()  # Fetch all job listings
    context = {
        'jobs': jobs
    }
    return render(request, 'job_feed.html', context)


def deleteJob(req,job_id):

    Jobmodel.objects.filter(id=job_id).delete()

    return redirect('created_JOb')


def applyJob(req, job_id):

    job =  Jobmodel.objects.get(id=job_id)

    context = {
        'job':job,
    }

    if req.method == 'POST':
        cover = req.POST.get('cover')
        skills = req.POST.get('skills')
        resume = req.FILES.get('resume')

        apply = Application(
            user = req.user,
            job = job,
            cover = cover,
            skills = skills,
            resume = resume
        )
        
        apply.save()
        return redirect('job_feed')


    return render(req, 'apply_job.html',context)


def searchJob(req):

    query = req.GET.get('query')

    if query:
        jobs = Jobmodel.objects.filter(Q(title__icontains = query)
                                        |Q(skill__icontains = query))

    else:
        jobs = Jobmodel.objects.none()

    context = {
        'query': query,
        'jobs': jobs,
    }

    return render(req, 'search.html', context)




    
    