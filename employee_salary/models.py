from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key= True)
    employee_name = models.CharField(max_length=50)
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees_department')
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee_name