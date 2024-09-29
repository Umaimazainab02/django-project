from django.urls import path

from . import views

urlpatterns = [
    path("",views.student_list, name="students"),
    path("all_students/", views.all_students, name="all_students")
]