from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Department

@api_view(['GET','POST','PUT','DELETE'])
def highest_paid_employee(request):
        # Create a list of dictionaries containing the highest paid employee in each department
        highest_paid_employees = []
        departments = Department.objects.all()
        for department in departments:
            # Query the database for the highest paid employee in each department
            highest_paid_employee = Employee.objects.filter(employee_department_id=department).aggregate(Max('employee_salary'))
            highest_paid_employee = Employee.objects.filter(employee_salary=highest_paid_employee['employee_salary__max'], employee_department=department).first()
            highest_paid_employees.append({
                'department': department.department_name,
                'employee_name': highest_paid_employee.employee_name,
                'employee_salary': highest_paid_employee.employee_salary
            })
        # Return the results as a response
        return Response(highest_paid_employees)
