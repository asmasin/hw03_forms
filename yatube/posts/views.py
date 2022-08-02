from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from posts.forms import PostForm

from .const import POST_COUNT
from .models import Group, Post, User


def index(request):
    """Функция обрабатывает запросы к главной странице,
    получает данные из модели Post и связанной модели Group,
    выводит 10 последних постов и рендерит их в шаблон."""
    post_list = Post.objects.select_related('group', 'author')
    paginator = Paginator(post_list, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Функция обрабатывает запросы к странице с публикациями группы,
    получает группу из модели и проверяет url к ней компановщиком slug,
    собирает словарь из данных и рендерит их в шаблон."""
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related('author')
    paginator = Paginator(post_list, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    """"""
    author = get_object_or_404(User, username=username)
    post_list = author.posts.select_related('author')
    post_count = post_list.count()
    paginator = Paginator(post_list, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'post_list': post_list,
        'post_count': post_count,
        'page_obj': page_obj,
    }

    return render(request, 'posts/profile.html', context)


@login_required
def post_detail(request, post_id):
    """"""
    post = get_object_or_404(Post, pk=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    # paginator = Paginator(post_count, POST_COUNT)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'post': post,
        'post_count': post_count,
               }

    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    """"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('posts:profile', post.author)

        return render(
            request,
            'posts/create_post.html',
            {
                'form': form,
            }
        )

    form = PostForm()

    return render(
        request,
        'posts/create_post.html',
        {
            'form': form,
        }
    )


@login_required
def post_edit(request, post_id):
    """"""
    post = get_object_or_404(Post, pk=post_id)
    is_edit = True
    if post.author != request.user:
        return redirect('posts', post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()

            return redirect('posts:profile', post.author)

        return render(
            request,
            'posts/create_post.html',
            {
                'post': post,
                'form': form,
                'is_edit': is_edit,
            }
        )

    form = PostForm(instance=post)

    return render(
        request,
        'posts/create_post.html',
        {
            'post': post,
            'form': form,
            'is_edit': is_edit,
        }
    )
