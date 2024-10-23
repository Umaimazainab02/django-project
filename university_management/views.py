from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    student_list = [
        {"name": "umaima", "roll": "ooo2"},
        {"name": "zainab", "roll": "ooo3"},
    ]
    return render(request, 'about.html', {'data': student_list})

def contact(request):
    return render(request, 'contact.html')
