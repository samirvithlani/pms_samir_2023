from django.db import models
from user.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    estimated_time = models.IntegerField()
    start_date = models.DateField()
    completion_date = models.DateField()
    
    class Meta:
        db_table = 'project'
    
    def __str__(self):
        return self.title                    
        
class ProjectTeam(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'project_team'

class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=100)
    description = models.TextField()
    estimeted_hours = models.IntegerField()
    status = models.CharField(max_length=100)
    startDate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'project_module'
    
    def __str__(self):
        return self.moduleName

class ProjectTask(models.Model):
    module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=100)
    description = models.TextField()
    estimeted_hours = models.IntegerField()
    status = models.CharField(max_length=100)
    startDate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'project_task'
    
    def __str__(self):
        return self.taskName    


                   
