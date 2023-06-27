
from django.contrib import admin
from django.urls import path, include

from authentication import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('ads.urls')),
    path('user/', views.UserListView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<pk>/', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]