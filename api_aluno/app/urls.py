from django.urls import path

from app.views import student_list, student_delete


urlpatterns = [
    path('', student_list),
    path('<int:pk>/', student_delete),
]