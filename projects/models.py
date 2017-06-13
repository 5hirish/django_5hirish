from django.db import models
import datetime
# Create your models here.


class AddProject(models.Model):

    default_link = "https://github.com/5hirish"
    default_file = "proj_0.jpg"

    project_id = models.AutoField(primary_key=True, db_column='pId')
    project_title = models.CharField(max_length=120, null=False, db_column='Title')
    project_start = models.DateField(null=False, db_column='Start_Date')
    project_end = models.DateField(default=datetime.date.today, null=False, db_column='End_Date')
    project_file = models.CharField(default=default_file, max_length=50, null=False, db_column='FileName')
    project_url = models.CharField(default=default_link, max_length=250, null=False, db_column='Link')
    project_tech = models.CharField(max_length=250, null=False, db_column='Tech')
    project_description = models.TextField(null=False, db_column='Description')

    class Meta:
        db_table = 'Projects'
