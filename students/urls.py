from django.urls import path
from students import views

urlpatterns = [
    path('', views.student_list),
    path('<int:pk>', views.student_detail),
]
