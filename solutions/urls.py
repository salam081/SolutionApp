
from django.urls import path
from .import views 

urlpatterns = [
      
      path('enter_solution<id>/', views.solution_view, name='solution'),
      path('problem_list/',views.problem_list_view, name= 'problem_list'),
      path('solution_list/',views.solution_list_view, name ='solution_list'),
      path('update/<id>/',views.updatesolution, name='update'),
      path('delete/<id>/',views.deletesolution, name='delete'),
      path('adopted_solutins_list/', views.adopted_solutions_list_view, name= 'adopted_solution_list'),
      path('adopted_solution/<id>', views.adopted_solution_view, name= 'adopted_solution'),


     
      
]