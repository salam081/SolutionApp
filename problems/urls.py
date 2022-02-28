from django.urls import path
from .import views



urlpatterns = [
     path('home/', views.home_view, name='home'),
     path('problems/', views.Problem_view, name='problems'),
     path('search/', views.search, name='search'),
     path('adopt_solutions/<id>/', views.adopt_solutions_view, name='adopt_solutions'),
     path('problem_exists/<id>/', views.problem_exists_view, name='problem_exists'),
     

]