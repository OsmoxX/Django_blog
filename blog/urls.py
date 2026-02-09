from django.urls import path
from . import views
from .views import StartingPageView, PostDetailView, PostListView

urlpatterns = [
    path('', StartingPageView.as_view(), name='starting-page'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail-page'),
]