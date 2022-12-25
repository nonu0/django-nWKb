from django.db import models

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    address = models.IntegerField()

    def __str__(self):
        return 'hospital' + str(self.name)

class Departments(models.Model):
    name = models.CharField(max_length=10)
    head = models.CharField(max_length=20)
    members_total = models.BigIntegerField()
    occupation = models.CharField(max_length=10)

    def __str__(self):
        return 'department' + str(self.name)

class Staff(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

# class Patient(models.Model):
# class Admin(models.Model):
