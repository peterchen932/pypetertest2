from django import http

def home(request):
    return http.HttpResponse('Hi pyPeter, Hello World!')
