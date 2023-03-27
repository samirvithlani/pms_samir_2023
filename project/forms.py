
from django import forms
from .models import Project,ProjectTeam,ProjectModule
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =Project
        fields ='__all__'
        
    

class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))
    
    class Meta:
        model =ProjectTeam
        fields ='__all__'

class CreateProjectModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'        