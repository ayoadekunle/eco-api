from django.db import models
from colorfield.fields import ColorField


class Course(models.Model):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    title = models.CharField(max_length=255)
    code = models.CharField(max_length=55, unique=True, primary_key=True)
    is_starred = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    color = ColorField()

    def __str__(self):
        return self.title
