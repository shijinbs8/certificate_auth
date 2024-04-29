from django.db import models

# Create your models here.
class Employee(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=200)
    department_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    joining_date = models.DateField()
    leaving_date = models.DateField()
    worked_in = models.TextField()
    tl_review = models.TextField()
    dh_review = models.TextField()
    feedback = models.TextField()
    certificate=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
       return self.name


class Skill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='skills')
    skill = models.CharField(max_length=100)
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.skill