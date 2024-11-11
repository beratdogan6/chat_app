from django.urls import path
from .views import Login, RegisterView, LogOutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
