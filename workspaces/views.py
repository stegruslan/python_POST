from django.db import transaction
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from workspaces.choices import RoleChoice
from workspaces.models import Workspace, WorkspaceRole
from serializers import WorkspaceOwnerSerializer
from workspaces.models import Workspace


class CreateWorkspaceView(CreateAPIView):
    serializer_class = WorkspaceOwnerSerializer
    queryset = Workspace.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            workspace = serializer.save()
            WorkspaceRole(workspace=workspace, user=request.user, role=RoleChoice.OWNER).save()

