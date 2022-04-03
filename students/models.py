from django.db import models
from users.models import User
from courses.models import Course


class Student(models.Model):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.get_full_name()
