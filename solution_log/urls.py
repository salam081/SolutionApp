
from django.contrib import admin
from django.urls import path, include 
# from problems.views  import Problem_view, home_view
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('problem/',include('problems.urls')),
    path('solution/', include('solutions.urls')),
    path('profile/', user_views.profile, name = 'profile'),
    path('report/', include('Report.urls')),
    
     
      
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

