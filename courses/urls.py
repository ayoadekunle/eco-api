from django.urls import path
from courses import views

urlpatterns = [
    path('', views.course_list),
    path('<str:pk>/', views.course_detail),
]
