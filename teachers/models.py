from django.db import models
from users.models import User
from courses.models import Course


class Teacher(models.Model):
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.get_full_name()
