
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model =User
        fields = fields = ('username', 'email', 'password1', 'password2','age','salary')
    
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user

class DeveloperCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model =User
        fields = fields = ('username', 'email', 'password1', 'password2','age','salary')
    
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user    