from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView
)
from django.urls import path, reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(),
        name='signup',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done'),
        ),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            success_url=reverse_lazy('users:password_reset_done'),
        ),
        name='password_reset_form'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'
    ), 
]

# from re import template
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import path

# from . import views

# app_name = 'users'

# urlpatterns = [
#     path(
#         'signup/',
#         views.SignUp.as_view(template_name='users/signup.html'),
#         name='signup'
#     ),
#     path(
#         'login/',
#         LoginView.as_view(template_name='users/login.html'),
#         name='login'
#     ),
#     path(
#         'logout/', LogoutView.as_view(template_name='users/logged_out.html'),
#         name='logout'
#     ),
# ]
