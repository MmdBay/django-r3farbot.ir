from django.urls import path
from .views import create, confirm

urlpatterns = [
    path("create", create),
    path("confirm/", confirm)
]
