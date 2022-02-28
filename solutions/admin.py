from django.contrib import admin
from . models import Solution


class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'solution']
admin.site.register(Solution,SolutionAdmin)


