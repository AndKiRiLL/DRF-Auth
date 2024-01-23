from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import *

###### Students ######
class ListStudents(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [AllowAny]

class CreateStudents(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [IsAdminUser]

class CRUDStudents(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [IsAdminUser]

###### Class ######
class ListClass(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers
    permission_classes = [AllowAny]

class CreateClass(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers
    permission_classes = [IsAdminUser]

class CRUDClass(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers
    permission_classes = [IsAdminUser]

###### Course ######
class ListCourse(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [AllowAny]

class CreateCourse(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAdminUser]

class CRUDCourse(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAdminUser]

###### Choise ######
class ListChoise(ListAPIView):
    queryset = Choise.objects.all()
    serializer_class = ChoiseSerializers
    permission_classes = [AllowAny]

class CreateChoise(CreateAPIView):
    queryset = Choise.objects.all()
    serializer_class = ChoiseSerializers
    permission_classes = [IsAdminUser]

class CRUDChoise(RetrieveUpdateDestroyAPIView):
    queryset = Choise.objects.all()
    serializer_class = ChoiseSerializers
    permission_classes = [IsAdminUser]