from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

@staff_member_required
def write(request):
    return render(request, 'blog/write.html')

def post(request, pk):
    return render(request, 'blog/post.html', {'pk': pk})

@staff_member_required
def modify(request, pk):
    return render(request, 'blog/modify.html', {'pk': pk})

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        print("TESTEST")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            password = request.data.get('password')
            user = authenticate(username="admin", password=password)
            login(request, user)
            if request.user.is_superuser:
                instance = self.get_object()
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=403)
        except:
            return Response(status=403)