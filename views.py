from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_list(request):
    posts = Post.objects.all()
    data = [{"id": post.id, "title": post.title, "description": post.description} for post in posts]
    return JsonResponse(data, safe=False)


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {"id": post.id, "title": post.title, "description": post.description}
    return JsonResponse(data)
