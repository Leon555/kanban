from django.db import models

# Create your models here.
class PClint(models.Model):
    project_name = models.CharField(max_length=32)
    build_time = models.DateTimeField(auto_now=True)

    project_url = models.CharField(max_length=512)
    error = models.IntegerField()
    warning = models.IntegerField()
    info = models.IntegerField()
    note = models.IntegerField()

    def __str__(self):
        return self.project_name

class CodeDex(models.Model):
    project_name = models.CharField(max_length=32)
    build_time = models.DateTimeField(auto_now=True)

    project_url = models.CharField(max_length=512)
    error = models.IntegerField()
    warning = models.IntegerField()

    def __str__(self):
        return self.project_name
