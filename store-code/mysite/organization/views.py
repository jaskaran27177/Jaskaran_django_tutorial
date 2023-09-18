from django.shortcuts import render
from .models import Employee, Organization, Office
from django.views import generic
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from django.contrib.auth.models import User
from .serializer import (
    OrganizationSerializer,
    OfficeSerializer,
    EmployeeSerializer,
    UserSerializer,
)


# Create your views here.
class IndexView(generic.ListView):
    template_name = "organization/index.html"
    context_object_name = "all_list"

    def get_queryset(self):
        return Organization.objects.all()


# class DetailView(generic.DetailView):
#     model = Organization
#     template_name = "organization/detail.html"
#     context_object_name = "organization"


#     def get_queryset(self):
#         return Organization.objects.prefetch_related("offices")
class DetailView(View):
    def get(self, request, *args, **kwargs):
        organization = Organization.objects.prefetch_related("offices__employees").get(
            pk=kwargs["pk"]
        )
        serializer = OrganizationSerializer(organization)
        return JsonResponse(serializer.data, safe=False)
