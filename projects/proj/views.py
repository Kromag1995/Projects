from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import assign_perm
from guardian.decorators import permission_required
from .models import Project, Chore
from .forms import ProjectForm, ChoreForm

@login_required()
def HomeView(request):
    #View para ver todos los projectos del usuario
    projects_list = Project.objects.filter(user=request.user)
    form = ProjectForm()
    context = {
        'form': form,
        'projects_list' : projects_list,
    }

    return render(request, 'proj/index.html', context)

@permission_required("proj.view_project", (Project,'id', 'proj_id'))
def ProjView(request,proj_id):
    #View para ver un projecto de forma individual con sus respectivas tareas
    project = Project.objects.get(pk=proj_id)
    form = ChoreForm()
    chores = Chore.objects.filter(project=project)
    context = {
        "project":project,
        "form": form,
        "chores": chores
    }
    return render(request, 'proj/proj.html', context)

@login_required()
def AddProjView(request):
    #View para crear projecto
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            user = request.user
            proj = form.save(commit=False)
            proj.user = user
            proj.save()
            print(user.has_perm('view_project',proj))
            assign_perm('delete_project',user, proj)
            assign_perm('change_project',user, proj)
            assign_perm('view_project',user, proj)
            print(user.has_perm('view_project',proj))
    return redirect('/proj/')

@login_required()
def DeleteProjView(request):
    #View para eliminar projectos
    if request.method == 'POST':
        project = Project.objects.get(pk=int(request.POST["project_id"]))
        if request.user.has_perm('delete_project', project):
            project.delete()
    return redirect('/proj/')


@permission_required("proj.change_project", (Project,'id', 'proj_id'))
def AddChoreView(request,proj_id):
    #View para crear tareas
    project = Project.objects.get(pk=proj_id)
    if request.method == 'POST':
        form = ChoreForm(request.POST)
        if form.is_valid():
            user = request.user
            chore = form.save(commit=False)
            chore.project = project
            chore.save()
            assign_perm('delete_chore',user, chore)
            assign_perm('change_chore',user, chore)
            assign_perm('view_chore',user, chore)
    return redirect(f'/proj/{proj_id}')


@login_required()
def DeleteChoreView(request,proj_id):
    #View para eliminar tareas
    if request.method == 'POST':
        chore = Chore.objects.get(pk=int(request.POST["chore_id"]))
        if request.user.has_perm('delete_chore', chore):
            chore.delete()
    return redirect(f'/proj/{proj_id}')

@login_required()
def DoneChoreView(request,proj_id):
    #View para marcar o desmarcar como hecha una tarea
    if request.method == 'POST':
        chore = Chore.objects.get(pk=int(request.POST["chore_id"]))
        if request.user.has_perm('change_chore', chore):
            chore.done = not(chore.done)
            chore.save()
    return redirect(f'/proj/{proj_id}')
