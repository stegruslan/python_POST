from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from workspaces.models import Workspace, User


class WorkspaceOwnerSerializer(
    serializers.ModelSerializer):
    admins = serializers.ListField(
        child=serializers.IntegerField()
    )
    members = serializers.ListField(
        child=serializers.IntegerField()
    )

    class Meta:
        model = Workspace
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"]
        )

    class Meta:
        model = User
        fields = '__all__'
