from datetime import timezone
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
from django.core.files.storage import FileSystemStorage
from django.db.models import Q 

def Homepage(request):

    total_jobs = Jobmodel.objects.all().count()
    total_users = CustomUser.objects.all().count()
    total_applications = Application.objects.all().count()

    context = {
        'total_jobs': total_jobs,
        'total_users': total_users,
        'total_applications': total_applications,
    }
    
    
    return render(request,'Homepage.html',context)
    
    

def loginpage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('Homepage') 
            else:
                return redirect('loginpage')

        except CustomUser.DoesNotExist:
            return redirect('loginpage')

    return render(request, 'loginpage.html')
    


def Registerpage(request):
    if request.method=='POST':
        
        username = request.POST['username']
        email = request.POST['email']
        Profile_Pic = request.FILES.get('Profile_Pic')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST.get('user_type')
    
        
        if password==confirm_password:
            
            
            user=CustomUser.objects.create_user(
                username=username,
                email=email,
                Profile_Pic=Profile_Pic,
                password=password,
                user_type=user_type,
                
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recuriters':
                recuritersProfileModel.objects.create(user=user)
            
            return redirect("loginpage")
            
    return render(request,"Registerpage.html")
    
     

    
    
    
    

def logoutPage(request):
    logout(request)
    
    return redirect("loginpage")



def profilePage(request):

    Seeker = seekerProfileModel.objects.all()  # Fetch all job listings
    context = {
        'Seeker': Seeker
    }
    
    
    return render(request, "profilePage.html", context)


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
    jobs = Jobmodel.objects.all()  
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
        return redirect('applied_jobs')


    return render(req, 'apply_job.html',context)


def searchJob(req):

    query = req.GET.get('query')

    if query:
        jobs = Jobmodel.objects.filter(Q(title__icontains = query)
                                        |Q(skill__icontains = query)
                                        |Q(Job_descriptons__icontains = query))

    else:
        jobs = Jobmodel.objects.none()

    context = {
        'query': query,
        'jobs': jobs,
    }

    return render(req, 'search.html', context)




def edit_profile(request):
    user=request.user
    if request.method=="POST":
        
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        user.contact_no = request.POST.get('contact_no')
        # user.skills = request.POST.get('skills')
        # user_skills = CustomUser.SKILLS 
        
        
       
        user.Profile_Pic=request.FILES.get('Profile_Pic')
        user.save()
        
        return redirect('profilePage',)
    
    
    return render(request,'edit_profile.html')



def editjob(req,job_id):
    current_user=req.user
   
    if req.method == 'POST':
        
        job_id=req.POST.get('job_id')
        
        job=Jobmodel(
            id=job_id,
            user=current_user,
            title=req.POST.get('title'),
            Number_of_opening=req.POST.get('Number_of_opening'),
            category=req.POST.get('category'),
            Job_descriptons=req.POST.get('Job_descriptons'),
            skill=req.POST.get('skill'),
            Image=req.FILES.get('Image'),

        )
        job.save()
        return redirect('created_JOb')
        
    jobs=Jobmodel.objects.get(id=job_id)
    
    context={
        'job':jobs,
    }
    
    return render(req,'editJob.html',context)

def skillMatchingPage(request):
    
    user=request.user
    
    mySkill=user.seekerProfile.skills
    jobs=Jobmodel.objects.filter(skill=mySkill)
    context={
        'jobs':jobs
    }
    print(mySkill)
    
    return render(request,"skillMatchingPage.html",context)

def applied_jobs(request):
    
    if request.user.is_authenticated:
        
        applications = Application.objects.filter(user=request.user)

        
        return render(request, 'applied_jobs.html', {'applications': applications})

    else:
        
        return redirect('login')  




    
    