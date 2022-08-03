from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<post_id>/edit/', views.post_edit, name='post_edit'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # path(
    #     'logout/',
    #      LogoutView.as_view(
    #         template_name='users/logged_out.html'),
    #         name='logout'
    #      ),
    # path(
    #     'login',
    #      LoginView.as_view(
    #         template_name='users/login.html'),
    #         name='login'
    #      ),
    # path(
    #     'password_change/',
    #     PasswordChangeView.as_view(
    #         template_name='users/password_change_form.html'),
    #         success_url=reverse_lazy('users:password_change_done'),
    #         name='password_change_form',
    # ),
    # path(
    #     'password_change/done/',
    #     PasswordChangeDoneView.as_view(
    #         template_name='users/password_change_done.html'),
    #     name='password_change_done',
    # ),
    # path(
    #     'password_reset/',
    #     PasswordResetView.as_view(
    #         template_name='users/password_reset_form.html'),
    #         success_url=reverse_lazy('users:password_reset_done'),
    #         name='password_reset',
    # ),
    # path(
    #     'password_reset/done/',
    #     PasswordResetDoneView.as_view(
    #         template_name='users/password_reset_done.html'),
    #         name='password_reset_done',
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     PasswordResetConfirmView.as_view(
    #         template_name='users/password_reset_confirm.html'),
    #         success_url=reverse_lazy('users:password_reset_complete'),
    #         name='password_reset_confirm'
    # ),
    # path(
    #     'reset/done/',
    #     PasswordResetCompleteView.as_view(
    #         template_name='users/password_reset_complete.html'),
    #         name='password_reset_complete'
    # ),
]
