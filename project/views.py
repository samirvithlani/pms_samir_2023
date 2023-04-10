from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *
# Create your views here.
class ProjectCreationView(CreateView):
    form_class =ProjectCreationForm
    model = Project
    template_name = 'project/project_create.html'
    success_url = '/project/list_project/'
    def form_valid(self, form):
        return super().form_valid(form)
    

class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'
    
    def get(self, request, *args, **kwargs):
        print("called....")
        input = request.GET.get('input')
        print(input)
        project=[]
        if input:
            project = Project.objects.filter(title__icontains=input)
            print(project)
            return render(request, self.template_name, {'project':project})
        else:
            project = Project.objects.all()    
            return render(request, self.template_name, {'project':project})
    
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/list_project/'
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project_detail'
    
    labels=[]
    data =[]
    project = Project.objects.all().values_list('title',flat=True)
    time = Project.objects.all().values_list('estimated_time',flat=True)
    for i in project:
        labels.append(i)
    for i in time:
        data.append(i)
    
             
    
    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
        return render(request, self.template_name, {'project_detail': self.get_object(),'team':team,'labels':self.labels,'data':self.data})
    
      
    
class ProjectDeleteView(DeleteView):
    model = Project
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project/'    
   
class ProjectTeamCreationView(CreateView):
    model = ProjectTeam
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project/'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
        
class Create_Project_team(CreateView):
    model = ProjectTeam
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project/'

class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
class ProjectTeamByProject(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
    def get_queryset(self):
        return super().get_queryset().filter(Project_id=self.kwargs['pk'])    

    
class CreateProjectModule(CreateView):
    model = ProjectModule
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'
    
        

class ProjectModuleListByProject(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'
    
    
    def get_queryset(self):
        return super().get_queryset().filter(project_id=self.kwargs['pk'])    
    


    
    
            