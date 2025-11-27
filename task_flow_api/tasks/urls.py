from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register(r"tasks", views.TaskViewSet, basename="task")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls))
]