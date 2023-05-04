from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    
    
    def __str__(self):
        return str(self.roll_number) +''+ str(self.name) +''+ str(self.marks)