"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp_static.views import index
from myapp_html_template.views import indexHTML
from myapp_blog_dynamic.views import indexDynamic
from myapp_blog_MVT.views import blog_post, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("myapp_static/", index, name="index"),
    path("myapp_html_template/", indexHTML, name="indexHTML"),
    path("myapp_blog_dynamic/", indexDynamic, name="indexDynamic"),
    path("myapp_blog_MVT/", blog_post, name="blog_post"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]

# after running the server (macOS): python3 manage.py runserver
# on the browser -->
# to run the myapp_static: http://127.0.0.1:8000/myapp_static/
# to run the myapp_html_template: http://127.0.0.1:8000/myapp_html_template/
# to run the myapp_html_template: http://127.0.0.1:8000/myapp_blog_dynamic/
# to run the myapp_html_template: http://127.0.0.1:8000/myapp_blog_MVT

