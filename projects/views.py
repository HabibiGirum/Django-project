from django.shortcuts import render

def projects(request):
    page ='Projects'
    return render(request, 'projects/projects.html',{'page':page})

def project(request,pk):
    return render(request,'single-project.html')
