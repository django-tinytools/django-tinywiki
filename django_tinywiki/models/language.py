from django.db import models

class WikiLanguage(models.Model):
    code = models.CharField(max_length=16,unique=True,null=False,blank=False)
    name = models.CharField(max_length=128,null=False,blank=False)
    is_builtin = models.BooleanField(default=False)
