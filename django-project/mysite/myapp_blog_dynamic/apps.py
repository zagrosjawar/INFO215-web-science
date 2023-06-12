from django.apps import AppConfig


class MyappBlogDynamicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp_blog_dynamic'
