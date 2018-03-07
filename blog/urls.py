from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('write/', views.write),
    path('post/<int:pk>/', views.post),
    path('modify/<int:pk>/', views.modify),
    path('rest/posts/', views.PostList.as_view()),
    path('rest/posts/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view()),
]