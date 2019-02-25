from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path('task/', views.ListTask.as_view()),
    #path('task/<int:pk>', ),
    path('archived/', views.ListArchived.as_view()),
    #path('archived/<int:pk>', )
]
