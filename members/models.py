from django.db import models

# Create your models here.
class MembersModel(models.Model):
        # fields of the model
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.IntegerField()
    date_of_birth = models.DateField()
    baptized = models.DateField()
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name