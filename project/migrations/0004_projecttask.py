# Generated by Django 4.1.7 on 2023-04-10 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projectmodule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('estimeted_hours', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectmodule')),
            ],
            options={
                'db_table': 'project_task',
            },
        ),
    ]