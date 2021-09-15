from django.db import models

# Create your models here.
from django.db import models



class sci1(models.Model):
    ProjectId = models.CharField(max_length  =200,null=True)
    Name = models.CharField(max_length=200,null=True)
    Reference = models.CharField(max_length = 200,null=True)
    ref = models.CharField(max_length = 200,null=True)
    #date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.ProjectId
        return self.Name
        return self.Reference


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
