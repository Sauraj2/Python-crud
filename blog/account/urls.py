from django.urls import path
from account.views import Register_View

urlpatterns = [
    path('register/',Register_View.as_view())
]