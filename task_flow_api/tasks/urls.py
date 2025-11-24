from django.urls import path
from tasks import views


urlpatterns = [
    path("tasks/", views.TaskList.as_view(), name="task_list"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="task_details"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user_detail"),
]