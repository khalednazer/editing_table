from .models import Stud
from rest_framework import serializers


class seruser(serializers.ModelSerializer):
    class Meta:
        model  = Stud
        fields ='__all__'