# from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    home_active = 'active'
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))