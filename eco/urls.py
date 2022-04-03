from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'auth/register/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
    path(
        'auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
]
