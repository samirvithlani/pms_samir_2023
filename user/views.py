from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ManagerCreationForm,DeveloperCreationForm
from .models import User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView
from project.models import Project

# Create your views here.
class ManagerRegisterView(CreateView):
    form_class = ManagerCreationForm
    model = User
    template_name = 'user/manager_register.html'
    success_url = '/user/login/'
    
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class DeveloperRegisterView(CreateView):
    form_class = DeveloperCreationForm
    model = User
    template_name = 'user/developer_register.html'
    success_url = '/user/login/'
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)    


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager/dashboard'
            else:
                return '/user/developer/dashboard'

class ManagerDashboardView(ListView): 
            
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()
        sort_by = self.request.GET.get('sort_by', 'title')
        direction = self.request.GET.get('direction', 'asc')
        print(".....",sort_by)
        print(".....",direction)
        if direction == 'asc':
            project = project.order_by(sort_by)
        elif direction == 'desc':
            project = project.order_by(f'-{sort_by}')
        

        
        
        return render(request, 'user/manager_dashboard.html',{
            'projects':project,
        })

    template_name = 'user/manager_dashboard.html'
    
class DeveloperDashBoardView(ListView):
    
    
    
     def get(self, request, *args, **kwargs):
       
        #get assigned project to loggedin developer
        projects = Project.objects.all().values()
        #user_tasks =
        

        
        
        return render(request, 'user/developer_dashboard.html',{
            
        })   
     template_name = 'user/developer_dashboard.html'
    
        