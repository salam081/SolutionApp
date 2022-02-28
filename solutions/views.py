from django.shortcuts import render, redirect, get_object_or_404
from . models import Solution
from .forms import  SolutionForm
from problems.models import Problem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def solution_view(request, id):
    problem = Problem.objects.get(id=id)

    if request.method == 'POST':
        solution = request.POST.get('solution')

        if solution != '': 
            obj = Solution.objects.create(problem_id = problem.id,solution = solution,created_by = request.user)
            obj.save()
            Problem.objects.filter(id=id).update(attempted=True)
            return redirect('/solution/problem_list')
        # else:
        #     print('No Solution')
    context = {'problem':problem}
    return render(request,'solutions/solutions.html',context)  

@login_required
def problem_list_view(request):
    problems = Problem.objects.filter(adopted=False)
    context = {'problems':problems}
    return render(request, 'solutions/problem_table.html', context)


@login_required
def solution_list_view(request):
    problems = Problem.objects.filter(adopted=False)
    context = {'problems':problems}
    return render(request, 'solutions/solution_list.html', context)
     
@login_required
def updatesolution(request, id):
    obj = Solution.objects.get(id=id)
    if request.method == 'POST':
        solution = request.POST.get('solution')
        Solution.objects.filter(id=id).update(solution=solution)
        return redirect('/solution/solution_list')
    context = {"obj":obj}
    return render(request, 'solutions/update.html',context)   

@login_required 
def deletesolution(request, id): 
    obj = get_object_or_404(Solution, id=id)
    if request.method == 'POST':
        obj.delete() 
        return redirect('solution_list')   
    return render(request, 'solutions/delete.html',{'obj':obj})

# @login_required
def adopted_solutions_list_view(request):
    problems = Problem.objects.filter(adopted=True)
    context = {'problems':problems}
    return render(request, 'solutions/adopted_solution_list.html', context)



def adopted_solution_view(request, id):
    problem = Problem.objects.get(id=id)
    context = {'problem':problem}
    return render(request, 'solutions/adopted_solution.html', context)


