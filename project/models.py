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
           
