from django.contrib import admin

# Register your models here.
from .models import Candidate, Press, Promise

admin.site.register(Candidate)
admin.site.register(Press)
admin.site.register(Promise)