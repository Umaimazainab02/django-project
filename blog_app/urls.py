from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("about/", views.blog_about, name="blog_about"),
    path("all_blog/", views.all_blogs, name="all_blogs"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("login/",auth_view.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/",auth_view.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
]
 