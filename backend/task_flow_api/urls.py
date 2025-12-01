"""
URL configuration for task_flow_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views as drf_jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("tasks.urls")),
    path("api/token/", drf_jwt_views.TokenObtainPairView.as_view()),
    path("api/token/refresh/", drf_jwt_views.TokenRefreshView.as_view()),
    path("api/token/verify/", drf_jwt_views.TokenVerifyView.as_view()),
    path("api/docs/", SpectacularSwaggerView.as_view(), name="docs"),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema")

]
