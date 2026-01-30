from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'blog/starting_page.html')

def post_list(request):
    return render(request, 'blog/post_list.html')

def post_detail(request, post_id):
    return render(request, 'blog/post_detail.html', {'post_id': post_id})