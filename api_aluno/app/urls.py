from django.urls import path

from app.views import StudentListAndCreate, StudentChangeAndDelete


urlpatterns = [
    path('', StudentListAndCreate.as_view()),
    path('<int:pk>/', StudentChangeAndDelete.as_view()),
]