from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Organization, Office, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    Email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ["name", "Email"]

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_Email(self, obj):
        return obj.user.email


class OfficeSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Office
        fields = ["address", "employees"]


class OrganizationSerializer(serializers.ModelSerializer):
    offices = OfficeSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ["name", "address", "offices"]
