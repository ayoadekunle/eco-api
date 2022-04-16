from django.urls import path
from students import views

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>/', views.student_detail),
    path('<int:pk>/courses/', views.student_course_get),
    path('<int:pk>/courses/<str:course_pk>/', views.student_course_post),
]
