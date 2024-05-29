# This file is used to define the URL routes for the book app.

from django.urls import path, re_path
from.views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view()),
    #book list view
    re_path(r'^(?P<pk>\d+)/$', BookDetail.as_view()),
    
    
]