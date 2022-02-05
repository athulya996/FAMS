from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    group = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    semester = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    group = models.CharField(max_length=100)


class Group(models.Model):
    group_no = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    group_teacher = models.CharField(max_length=100)
    total_score = models.FloatField(default=0)


class Program(models.Model):
    name = models.CharField(max_length=100)
    rule = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    limitations_of_participations = models.IntegerField()


class Result(models.Model):
    program = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    mark = models.IntegerField()
    group = models.ForeignKey(Student, on_delete=models.CASCADE)
