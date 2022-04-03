from rest_framework import serializers

from courses.serializers import CourseSerializer
from users.serializers import UserDetailsSerializer
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    user = UserDetailsSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'
