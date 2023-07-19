from .auth import sign_up
from .main import about, contact, index
from .news import NewsListView, NewsDetailView, NewsCreateView
from .books import BookListView, BookDetailView, BookCreate


__all__ = [
    "sign_up",
    "about",
    "contact",
    "index",
    "NewsDetailView",
    "NewsListView",
    "NewsCreateView",
    "BookListView",
    "BookDetailView",
    "BookCreate",
]
