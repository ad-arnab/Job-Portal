from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myproject.Views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Homepage/', Homepage,name='Homepage'),
    path('loginpage/', loginpage,name='loginpage'),
    path('', Registerpage,name='Registerpage'),
    path('logoutPage', logoutPage,name='logoutPage'),
    path('profilePage', profilePage,name='profilePage'),
    path('skillMatchingPage', skillMatchingPage,name='skillMatchingPage'),
    path('edit_profile', edit_profile,name='edit_profile'),
    path('editjob/<int:job_id>/', editjob, name='edit_job'),
    
    
    path('add_job', add_job, name='add_job'),
    path('applied_jobs', applied_jobs, name='applied_jobs'),
    path('created_JOb', created_JOb, name='created_JOb'),
    path('job_feed', job_feed, name='job_feed'),
    path('deleteJob/<int:job_id>',deleteJob, name="deleteJob"),
    path('applyJob/<int:job_id>',applyJob, name="applyJob"),
    path('searchJob/',searchJob, name="searchJob"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
