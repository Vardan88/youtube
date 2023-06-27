
from django.urls import path
from .views import PanCreateView, PanUpdateView, PanDeleteView, profile_view, RegisterView

app_name = "web"

urlpatterns = [
    path('pans/', PanCreateView.as_view(), name="create_pan"),  # Добавьте косую черту в конце
    path('pans/<pk>/', PanUpdateView.as_view(), name="update_pan"),  # Добавьте косую черту в конце
    path('pans/<pk>/delete/', PanDeleteView.as_view(), name="delete_pan"),  # Добавьте косую черту в конце
    path('profile/', profile_view, name="profile"),  # Добавьте косую черту в конце
    path('register/', RegisterView.as_view(), name="register"),  # Добавьте косую черту в конце
]
