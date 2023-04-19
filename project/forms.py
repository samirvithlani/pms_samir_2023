
from django import forms
from .models import Project,ProjectTeam,ProjectModule,ProjectTask
from user.models import User
from django.forms.widgets import DateTimeInput
from django.forms.widgets import DateInput



class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =Project
        fields ='__all__'
        widgets={
            'start_date':DateInput(attrs={'type':'date'}),
            'completion_date':DateInput(attrs={'type':'date'}),
        }
        
    

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))
    
    class Meta:
        model =ProjectTeam
        fields ='__all__'

class CreateProjectModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'        

class CreateProjectTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields = '__all__'        