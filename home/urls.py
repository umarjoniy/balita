from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('blog-single/<slug:slug>/', blog_single),
    path('category/', category)
]
