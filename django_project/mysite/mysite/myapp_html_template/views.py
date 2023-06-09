from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request from mysite/mysite/urls.py
# index.html from templates
def indexHTML(request):
    return render(request, "index.html", {})
