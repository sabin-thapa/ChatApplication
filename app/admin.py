from django.contrib import admin

# Register your models here.
from app.models import Message, UserProfile

admin.site.register(Message)
admin.site.register(UserProfile)
