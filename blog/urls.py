from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail-page'),
]