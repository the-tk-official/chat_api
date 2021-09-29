from django.urls import path

from user_control.views import LoginView, RegisterView, RefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('refresh/', RefreshView.as_view(), name='refresh'),
]