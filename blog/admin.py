from django.contrib import admin
from .models import Post

# Models registered for "Blog" app
admin.site.register(Post)