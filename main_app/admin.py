from django.contrib import admin
from .models import Case,Comment,Component,Photo, Profile
# Register your models here.
admin.site.register(Case)
admin.site.register(Comment)
admin.site.register(Component)
admin.site.register(Photo)
admin.site.register(Profile)

