from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    ministry = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
