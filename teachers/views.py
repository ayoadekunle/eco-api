from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


@csrf_exempt
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def teacher_detail(request, pk):

    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        teacher.delete()
        return HttpResponse(status=204)
