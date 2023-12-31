from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about-page"),
    path("contact/", views.contact, name="contact-page"),

    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', views.NewsCreateView.as_view(), name='news-create'),

    path('sign-up', views.sign_up, name='sign_up'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
]
