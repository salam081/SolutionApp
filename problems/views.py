from django.shortcuts import render, redirect
from .models import *
from .forms import ProblemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
# new comments
def home_view(request):
    context = {}
    return render(request, 'problems/home.html', context)



@login_required
def Problem_view(request):
    form = ProblemForm(request.POST or None) 
    if form.is_valid():
        app = form.cleaned_data.get('app')
        title = form.cleaned_data.get('title')  
        problem = Problem.objects.filter(app=app, title=title, adopted=True)
        for p in problem:
            problem_id = p.id
        if problem:
            return redirect('problem_exists', id=problem_id)
        else:
            obj = form.save(commit=False)
            obj.created_by = request.user 
            obj.save()
            form  = ProblemForm()
            messages.info(request, 'Your complaint  was successfuly submitted') 
    context = {"form":form}
    return render(request,'problems/problems.html',context)


@login_required
def search(request):
    if request.method =="POST":
        searched = request.POST.get('searched')
        if search != '' and search is not None:
            problems =  Problem.objects.filter(title__title__icontains=searched)
            context = {'searched':searched,'problems':problems}
            return render(request,'problems/search_problem.html',context)
    else:
        return render(request,'problems/search_problem.html',{})



@login_required
def adopt_solutions_view(request, id):
    problem = Problem.objects.filter(id=id)
    if request.method =='POST':
        
        problem.update(adopted=True)
        return redirect('solution_list')
    return render(request, 'problems/adopt.html', {'problem':problem})    

@login_required
def problem_exists_view(request, id):
    problem = Problem.objects.get(id=id)
    context =  {'problem':problem}
    return render(request, 'problems/exists.html',context)


               