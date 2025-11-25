from django.contrib.auth.models import User
from rest_framework import generics, permissions

from tasks.models import Task
from tasks.permissions import IsOwnerOrReadOnly
from tasks.serializers import TaskSerializer, UserSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """This view should return a list of all the tasks for the currently authenticated user."""
        user = self.request.user
        return Task.objects.filter(owner=user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
