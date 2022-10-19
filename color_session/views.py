# from django.shortcuts import render
# from django.http import HttpResponse

from django.http import HttpResponse
from django.template import Template, Context
import random
import socket
from http import cookies

def index(request):
    color_list = ['purple', 'black', 'white']

    # val = request.META['HTTP_COOKIE']
    # cookie_data = cookies.SimpleCookie()
    # cookie_data.load(val)
    # print(cookie_data)

    if not request.session.get('color'):
        color = random.choice(color_list)
        request.session['color'] = color
        return HttpResponse(color + " is set to session")
    return HttpResponse(request.session['color'] + " from session via django \"" + socket.gethostname() + "\"")
