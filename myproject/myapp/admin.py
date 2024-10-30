from django.contrib import admin
from myapp.models import *


admin.site.register(CustomUser)

admin.site.register(Jobmodel)
admin.site.register(recuritersProfileModel)
admin.site.register(seekerProfileModel)
admin.site.register(Application)