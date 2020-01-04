from django.shortcuts import render, get_object_or_404, redirect
from posts.models import BlogPost, Comment, Tag, Category
from projects.models import Project
from django.core.paginator import Paginator
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.contrib.postgres.search import SearchVector
from django.db.models import Count
from django.contrib.auth.models import User


def home(request):
    posts = BlogPost.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'posts': posts})


def blog(request):
    all_posts = BlogPost.objects.all().order_by('-id')

    if request.method == 'GET' and 'cat' in request.GET:
        search_vector = SearchVector(
            'author__username', 'category__name', 'title', 'tags__name', 'content')
        post_list = BlogPost.objects.all().annotate(cat=search_vector).filter(
            cat=request.GET['cat']).order_by('-id')
    else:
        post_list = all_posts

    paginator = Paginator(post_list, 4)
    tags = Tag.objects.all()
    categories = Category.objects.all().annotate(posts_count=Count('blogpost'))


    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # Search for blog post
    if request.method == 'GET' and 'cat' in request.GET:
        # If result:
        if post_list:
            return render(request, 'blog/blog.html', {
                'posts': posts,
                'all_posts': all_posts,
                'range': range(posts.paginator.num_pages+1),
                'tags': tags,
                'categories': categories,
                'selected_category': request.GET['cat']
            })
        # If no result:
        return render(request, 'blog/blog.html', {
            'posts': posts,
            'all_posts': all_posts,
            'range': range(posts.paginator.num_pages+1),
            'tags': tags,
            'categories': categories,
            'selected_category': 'There are no results that match your search.'
        })
    # No search:
    return render(request, 'blog/blog.html', {
        'posts': posts,
        'all_posts': all_posts,
        'range': range(posts.paginator.num_pages+1),
        'tags': tags,
        'categories': categories
    })


def post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    posts = BlogPost.objects.all().order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all().annotate(posts_count=Count('blogpost'))

    hit_count = HitCount.objects.get_for_object(post)
    HitCountMixin.hit_count(request, hit_count)

    if request.method == "POST":
        if request.user.is_authenticated:
            comment = Comment.objects.create(
                post=post,
                author=request.user,
                text=request.POST['comment'],
            )
            selected_category = "Comment submitted."
            comment.save()

        return render(request, 'blog/post.html', {'post': post, 'posts': posts, 'tags': tags, 'categories': categories, 'selected_category': selected_category})

    return render(request, 'blog/post.html', {'post': post, 'posts': posts, 'tags': tags, 'categories': categories})
