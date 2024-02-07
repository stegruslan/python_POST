from django.urls import path

from .views import SignUpView, CreateWorkspaceView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('workspace/create/', CreateWorkspaceView.as_view())
]