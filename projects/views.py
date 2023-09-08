from django.shortcuts import render

def projects(request):
    return render(request, 'projects.html')

def project(request,pk):
    return render(request,'single-project.html')
