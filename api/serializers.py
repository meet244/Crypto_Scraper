from rest_framework import serializers
from rest_framework import serializers
from .models import Task


# Define the TaskSerializer class
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
