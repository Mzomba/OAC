from django.db import models

# Create your models here.

class Category(models.Model):
    # fields of the model
    name = models.CharField(max_length=100)
    class Meta:
        # this is used to set the plural name of the model
        ordering = ['name']
        verbose_name_plural = "Categories"
    # this is used to set the singular name of the model
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name
class MembersModel(models.Model):
        # fields of the model
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='members', default=None, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.IntegerField()
    date_of_birth = models.DateField()
    baptized = models.DateField()
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Members"
        # this is used to set the plural name of the model
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name