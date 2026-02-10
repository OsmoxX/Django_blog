from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm

all_posts = Post.objects.all().order_by('-date')

def get_date(post):
    return post.date

# Create your views here.
class StartingPageView(ListView):
    template_name = 'blog/starting_page.html'
    model = Post
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-date')[:3]

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/starting_page.html', {'latest_posts': latest_posts})

class PostListView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-date')

# def post_list(request):
#     return render(request, 'blog/all-posts.html', {'all_posts': all_posts})

class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)


    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[post.slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {'post': post})

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)






    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect(reverse('starting-page'))
