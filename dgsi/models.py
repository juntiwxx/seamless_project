from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    ACADEMIC_YEAR =	models.IntegerField(max_length=4)
    SEMESTER =	models.IntegerField(max_length=1)

    def __str__(self):
        return self.ACADEMIC_YEAR    
