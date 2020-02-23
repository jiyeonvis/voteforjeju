from django.contrib import admin

# Register your models here.
from .models import Candidate, Press, Promise, BRpromise
from markdownx.admin import MarkdownxModelAdmin

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

class BRpromAdmin(admin.ModelAdmin):
    list_display=(
        'party',
        'link',
    )
    list_display_links = (
        'party',
    )

admin.site.register(Candidate, CandAdmin)
admin.site.register(Press, PressAdmin)
admin.site.register(Promise, PromAdmin)
admin.site.register(BRpromise, BRpromAdmin)