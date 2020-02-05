from django.contrib import admin

# Register your models here.
from .models import Candidate, Press, Promise

class CandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'party',
        'number',
        'region',
    )
    list_display_links = (
        'name',
    )
class PressAdmin(admin.ModelAdmin):
    list_display= (
        'candidate',
        'headline',
        'where',
        'link',
  
    )
    list_display_links = (
        'candidate',
    )

class PromAdmin(admin.ModelAdmin):
    list_display=(
        'candidate',
        'more_info',
    )
    list_display_links = (
        'candidate',
    )

admin.site.register(Candidate, CandAdmin)
admin.site.register(Press, PressAdmin)
admin.site.register(Promise, PromAdmin)