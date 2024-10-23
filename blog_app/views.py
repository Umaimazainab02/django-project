from django.shortcuts import render, redirect
from .forms import AddBlogForm
from .models import Add_Blog
# Create your views here.

def blog_home(request):
    return render(request, 'blog_home.html')

def blog_about(request):
    return render(request, 'blog_about.html')

def all_blogs(request):
    all_blog = Add_Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs': all_blog})

def create_blog(request):
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)
            
            blog.created_by = request.user
            
            blog.save()
            
            return redirect("blog_home")
        
    form = AddBlogForm()  
    
    return render(request,"create_blog.html", {"form": form})  
    