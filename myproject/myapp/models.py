from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    USER=[
        ('recuriters', 'Recuriters'),
        ('seeker', 'Seeker'),
        
    ]
    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('data science', 'Data Science'),
        ('cyber security', 'Cyber Security'),
        ('digital marketing', 'Digital Marketing'),
        ('cloud computing', 'Cloud Computing'),

    ]

    
    user_type=models.CharField(max_length=100,null=True,choices=USER)
    skills = models.CharField(choices=SKILLS, max_length=100, null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)

class seekerProfileModel(models.Model):

     SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('data science', 'Data Science'),
        ('cyber security', 'Cyber Security'),
        ('digital marketing', 'Digital Marketing'),
        ('cloud computing', 'Cloud Computing'),

    ]
     
     user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='seekerProfile')
     skills = models.CharField(choices=SKILLS, max_length=100, null=True)

     
     def __str__(self):
        return f"{self.user.username}"   
    
    
    
    
    
    
     

    

class recuritersProfileModel(models.Model):
    
   
    
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='recuritersProfile')
    
    
    def __str__(self):
        return f"{self.user.username}"   
    
    

    



class Jobmodel(models.Model):

    category_choice=[
        ('full_time','Full_time'),
        ('part_time','Part_time'),
        
    ]

    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('data science', 'Data Science'),
        ('cyber security', 'Cyber Security'),
        ('digital marketing', 'Digital Marketing'),
        ('cloud computing', 'Cloud Computing'),

    ]


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=100,null=True)
    Number_of_opening = models.PositiveIntegerField(null=True)
    category = models.CharField(choices=category_choice, max_length=100,null=True)
    Job_descriptons = models.TextField(max_length=200,null=True)
    skill=models.CharField(choices=SKILLS,max_length=200,null=True)
    Image = models.ImageField(upload_to="Media/Job_image", null=True)

    

    
class Application(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Jobmodel,on_delete=models.CASCADE,null=True)
    cover = models.CharField(max_length=500, null=True)
    skills = models.CharField(max_length=100, null=True)
    resume = models.ImageField(upload_to='Media/Resume', null=True)

    



    

    


    