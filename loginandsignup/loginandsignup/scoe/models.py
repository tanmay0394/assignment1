from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    seat_number = models.IntegerField()

    def __str__(self):
        return self.name
