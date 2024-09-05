from django.urls import path
from account.views import LoginView, Register_View

urlpatterns = [
    path('register/',Register_View.as_view()),
    path('login/',LoginView.as_view())
]