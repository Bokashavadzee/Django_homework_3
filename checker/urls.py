from django.urls import path
from .views import check

urlpatterns = [
    path("<int:id>/", check)
]