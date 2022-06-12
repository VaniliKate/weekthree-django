from django.contrib import admin
from .models import Profile,Projects,Rates,Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Rates)
admin.site.register(Comments)
