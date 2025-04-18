from django.urls import path,include
from .views import BookListCreateApiView,BookDetailApiView
urlpatterns = [
    path("books/",BookListCreateApiView.as_view(),name="booklist"),
    path("book/<int:pk>/",BookDetailApiView.as_view(),name="book-detail")
]