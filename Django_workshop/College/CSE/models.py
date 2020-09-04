from django.db import models


class CseStudentRegister(models.Model):
    student_name = models.CharField(max_length=10)
    phone_num = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.student_name


class Faculty(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
