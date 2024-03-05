from django.http import HttpResponse
from django.template import loader
def home_views(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def login_views(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def signup_views(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())
def scrapbook_views(request):
    template=loader.get_template('scrapbook.html')
    return HttpResponse(template.render())
def timecapsule_views(request):
    template=loader.get_template('timecapsule.html')
    return HttpResponse(template.render())
def maps_views(request):
    template=loader.get_template('maps.html')
    return HttpResponse(template.render())
def albums_views(request):
    template=loader.get_template('albums.html')
    return HttpResponse(template.render())
def layout1_views(request):
    template=loader.get_template('layout1.html')
    return HttpResponse(template.render())
def layout2_views(request):
    template=loader.get_template('template1.html')
    return HttpResponse(template.render())