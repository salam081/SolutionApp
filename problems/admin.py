from django.contrib import admin

from .models import ProblemType, Problem, ProblemLocation, Cause, App, Title

admin.site.register(Problem)
admin.site.register(ProblemType)
admin.site.register(ProblemLocation)
admin.site.register(Cause)
admin.site.register(App)
admin.site.register(Title)


 