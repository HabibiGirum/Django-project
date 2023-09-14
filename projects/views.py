from django.shortcuts import render,redirect
from .models import Project

from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context ={'projects':projects}
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:',projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj,'tags':tags})


def createProject(request):
    form=ProjectForm

    if request.method == 'POST':
    
        form =ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'forms':form}
    return render(request,"projects/project_form.html",context)