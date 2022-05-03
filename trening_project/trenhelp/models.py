from django.db import models
from django.urls import reverse

# Create your models here.

class Training(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trenhelp:trenhelp_detail', kwargs={'pk':self.pk})

class Exercise(models.Model):
    training = models.ForeignKey(Training,on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField(blank=False)
    reps = models.PositiveIntegerField(blank=False)
    weight = models.DecimalField(decimal_places=2,max_digits=10,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trenhelp:trenhelp_detail', kwargs={'pk':self.training.pk})
    

