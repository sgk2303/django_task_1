from django.http import JsonResponse
from django.db.models import Max
from .models import Department, Employee

# Create your views here.
def highest_paid_employee(request):
    # Query the database for the highest paid employee in each department
    departments = Department.objects.annotate(highest_salary=Max('employees__salary')).order_by('name')

    # Create a list of dictionaries containing the highest paid employee in each department
    results = []
    for department in departments:
        result = {}
        highest_paid_employee = department.employees.filter(salary=department.highest_salary).first()
        result['name'] = highest_paid_employee.name
        result['department'] = department.name
        result['salary'] = str(highest_paid_employee.salary)
        results.append(result)

    # Return the results as a JSON response
    return JsonResponse({'results': results})
