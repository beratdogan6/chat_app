from django.urls import path
from .views import Login, RegisterView, LogOutView
from chat.views.call_view import StartCall, EndCall
from chat.views.message_view import MessageView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('message/', MessageView.as_view()),
    path('start-call/', StartCall.as_view()),
    path('end-call/', EndCall.as_view()),
]
