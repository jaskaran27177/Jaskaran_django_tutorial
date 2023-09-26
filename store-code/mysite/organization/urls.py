from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet)
app_name = "organization"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", include(router.urls)),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
