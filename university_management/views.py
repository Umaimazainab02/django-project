from django.http import HttpResponse

def index(request):
    return HttpResponse("Wellcome to our home page")


def about(request):
    return HttpResponse('<h1> Welcome to our about page.... </h1>')

def contact(request):
    return HttpResponse('<h1> Welcome to our contact page.... </h1>')