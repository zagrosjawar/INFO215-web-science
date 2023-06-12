from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "bloglist.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "post_detail.html", context)
