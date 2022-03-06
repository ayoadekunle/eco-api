from django.db import models
from users.models import User


class Student(models.Model):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
