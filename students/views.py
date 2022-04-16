from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from courses.models import Course
from courses.serializers import CourseSerializer
from students.models import Student
from students.serializers import StudentSerializer


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)


@csrf_exempt
def student_course_post(request, pk, course_pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "POST":
        try:
            course = Course.objects.get(pk=course_pk)
            serializer = CourseSerializer(course)
            student.courses.add(course)
            return JsonResponse(serializer.data, status=200)
        except Course.DoesNotExist:
            return JsonResponse({'course': "Course does not exist"}, status=404)


@csrf_exempt
def student_course_get(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        courses = student.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
