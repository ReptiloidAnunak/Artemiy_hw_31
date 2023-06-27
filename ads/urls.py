from django.urls import path

from ads import views

urlpatterns = [
    path('', views.index),
    path('ad/', views.AdsListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/', views.AdsDetailView.as_view()),
    path('ad/<int:pk>/update/', views.ad_update_view),
    path('ad/<int:pk>/delete/', views.AdDelete.as_view()),
    path('cat/', views.CategoriesView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdate.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDelete.as_view()),
    path('selection/', views.SelectionsViewList.as_view()),
    path('selection/create/', views.SelectionCreateView.as_view()),
    path('selection/<int:pk>/', views.SelectionDetailView.as_view()),
    path('selection/<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('selection/<int:pk>/delete/', views.SelectionDeleteView.as_view()),

]