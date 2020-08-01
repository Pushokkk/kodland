from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsLstView.as_view(), name='index'),
    path('new/', views.PostCreateView.as_view(), name='new-post'),
    path('<pk>/', views.PostDetailView.as_view(), name='post'),
]
