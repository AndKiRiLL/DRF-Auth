from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListStudents.as_view()),
    path('create/', CreateStudents.as_view()),
    path('<int:pk>/', CRUDStudents.as_view()),

    path('class/', ListClass.as_view()),
    path('class/create/', CreateClass.as_view()),
    path('class/<int:pk>/', CRUDClass.as_view()),

    path('course/', ListCourse.as_view()),
    path('course/create/', CreateCourse.as_view()),
    path('course/<int:pk>/', CRUDCourse.as_view()),

    path('choise/', ListChoise.as_view()),
    path('choise/create/', CreateChoise.as_view()),
    path('choise/<int:pk>/', CRUDChoise.as_view()),
]