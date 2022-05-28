from django.db import models

class threeDmodels(models.Model):
    name = models.CharField(max_length=100)
    modelfile = models.FileField(upload_to='mymodel/')

    # def __str__(self):
    #     return self.name

