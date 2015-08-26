from django import http

def home(request):
    return http.HttpResponse('This the project pypetertest2, Hello World!')
