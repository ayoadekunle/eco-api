from django.urls import path
from teachers import views

urlpatterns = [
    path('', views.teacher_list),
    path('<int:pk>', views.teacher_detail),
    path('<int:pk>/courses/', views.teacher_course_list),
]
