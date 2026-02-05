from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404

all_posts = Post.objects.all().order_by('-date')

def get_date(post):
    return post.date

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/starting_page.html', {'latest_posts': latest_posts})

def post_list(request):
    return render(request, 'blog/all-posts.html', {'all_posts': all_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post})