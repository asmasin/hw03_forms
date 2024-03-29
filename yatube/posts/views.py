from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm
from posts.utils import page_nav
from .models import Group, Post, User


def index(request):
    """
    Функция обрабатывает запросы к главной странице,
    получает данные из модели Post и связанной модели Group,
    выводит 10 последних постов и рендерит их в шаблон.
    """
    post_list = Post.objects.select_related('group', 'author')
    page_obj = page_nav(request, post_list)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """
    Функция обрабатывает запросы к странице с публикациями группы,
    получает группу из модели и проверяет url к ней компановщиком slug,
    собирает словарь из данных и рендерит их в шаблон.
    """
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related('author')
    page_obj = page_nav(request, post_list)
    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    """
    Функция обрабатывает запросы к странице профиля пользователя,
    получает посты пользователя, собирает словарь и рендерит шаблон.
    """
    author = get_object_or_404(User, username=username)
    post_list = author.posts.select_related('author')
    page_obj = page_nav(request, post_list)
    context = {
        'author': author,
        'page_obj': page_obj,
    }

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    """
    Функция обрабатывает запросы к странице поста.
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }

    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    """
    Функция обрабатывает запросы к странице добавления поста.
    После успешной валидации формы добавляется пост, а автор
    перенаправляется на страницу профиля.
    """
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
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


@login_required
def post_edit(request, post_id):
    """
    Функция обрабатывает запросы к странице изменения поста.
    Авторы могут редактировать свои посты, чужие только просматривать.
    """
    post = get_object_or_404(Post, pk=post_id)
    is_edit = True
    if post.author != request.user:
        return redirect('posts:post_detail', post_id)

    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        form.save()

        return redirect('posts:post_detail', post_id)

    return render(
        request,
        'posts/create_post.html',
        {
            'post': post,
            'form': form,
            'is_edit': is_edit,
        }
    )
