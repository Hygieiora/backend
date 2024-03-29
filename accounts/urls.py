from django.urls import path

from .views import *

urlpatterns = [
    path("", api_root),
    path("users/", UsersList.as_view(), name="account-view"),
    path("users/<int:pk>/", UserDetail.as_view(), name="account-detail"),
    path("register/", RegisterUserView.as_view(), name="auth-register"),
    path("login/", MyObtainTokenPairView.as_view(), name="auth-login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]