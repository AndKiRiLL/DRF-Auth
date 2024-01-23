from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class ChoiseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choise
        fields = "__all__"