from django.urls import path
from . import views
urlpatterns = [
    path('api/courts/list', views.CourtList.as_view()),
]