from django.urls import path

from . import views


urlpatterns = [
    path('test_one/', views.test_view_one),
]