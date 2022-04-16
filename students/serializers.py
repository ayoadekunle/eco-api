from rest_framework import serializers

from courses.serializers import CourseSerializer
from users.serializers import UserDetailsSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    user = UserDetailsSerializer()

    class Meta:
        model = Student
        fields = '__all__'
