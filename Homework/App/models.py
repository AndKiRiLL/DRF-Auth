from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=30)
    year = models.SmallIntegerField()
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Choise(models.Model):
    number = models.SmallIntegerField()
    def __str__(self):
        return str(self.number)

class Student(models.Model):
    fio = models.CharField(max_length=60)
    age = models.SmallIntegerField()
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    choises = models.ForeignKey(Choise, on_delete=models.CASCADE)
    group = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.fio

