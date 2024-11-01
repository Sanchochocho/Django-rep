from django.shortcuts import redirect, render
from .models import Post, Genre

def post_list(request):
    genre_id = request.GET.get('genre_id')
    if genre_id != None:
        posts = Post.objects.filter(genre__id=genre_id)
    else:
        posts = Post.objects.all()
    
    genres = Genre.objects.all()
    context = {
        "posts": posts,
        "genres": genres
    }

    return render(request, 'posts/post_list.html', context)

def post(request, id):

    post = Post.objects.get(id = id)

    context = {
        "post": post,
    }

    return render(request, 'posts/post.html', context)

def create_post(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        genre = request.POST.get('genre')
        image = request.FILES.get('image')

        genre = Genre.objects.get(id=genre)
        Post.objects.create(title=title,
                            content=content,
                            genre=genre,
                            image=image)
        return redirect('post_list')

    genres = Genre.objects.all()

    context = {
        "genres": genres
    }

    return render(request, 'posts/post_create.html', context)