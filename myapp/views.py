from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html") # This is the response that will be sent to the client

# Create your views here.
def todo(request):
    return render(request, "todos.html") # This is the response that will be sent to the client