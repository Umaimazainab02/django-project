from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("about/", views.blog_about, name="blog_about"),
    path("all_blog/", views.all_blogs, name="all_blogs"),
    path("create_blog/", views.create_blog, name="create_blog")
]
 