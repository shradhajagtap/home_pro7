from django.db import models


class Employee(models.Model):
    EMPLOYEE_LOCATION = [("pune", "PUNE"), ("mumbai", "MUMBAI"), ("nashik", "NASHIK"), ("nagpur", "NAGPUR")]
    EMPLOYEE_SALARY = [("under 5000", "UNDER 5000"), ("under 10000","UNDER 10000"),
                       ("under 15000","UNDER 15000"), ("under 20000", "UNDER 20000"),("under 30000", "UNDER 30000")]
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=20)
    employee_location_mode = models.CharField(max_length=20, choices=EMPLOYEE_LOCATION)
    employee_salary_mode = models.CharField(max_length=20, choices=EMPLOYEE_SALARY)
    working_time = models.IntegerField()
