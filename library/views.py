from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import generic
from django.contrib.auth import login, logout, authenticate

from .models import News
from .forms import RegisterForm


def base(request):
    return render(request, template_name="library/base.html")


def index(request):
    news = News.objects.all()[:5]
    context = {"news": news}
    return render(request, template_name="library/index.html", context=context)


def index2(request):
    data = {"header": "Hello Django", "message": "Welcome to Python", "title": "Beetroot page"}
    data["book_list"] = [
        ("Learning Python", "Mark Lutz", 1643),
        ("Head-First Python", "Paul Barry", 622),
        ("Python Distilled", "David Beazley", 352),
    ]
    data["cool_books"] = [
        {"title": "Learning Python", "author": "Mark Lutz", "price": 20.99, "image": "https://m.media-amazon.com/images/I/51ycFmfAeKL._SX198_BO1,204,203,200_QL40_ML2_.jpg"},
        {"title": "Head-First Python", "author": "Paul Barry", "price": 20.99, "image": "https://m.media-amazon.com/images/I/519QwuI5qKL._SX198_BO1,204,203,200_QL40_ML2_.jpg"},
        {"title": "Python Distilled", "author": "David Beazley", "price": 20.99, "image": "https://m.media-amazon.com/images/P/B094CMKN2J.01._SCLZZZZZZZ_SX500_.jpg"},
    ]
    return render(request, template_name="library/index.html", context=data)


def about(request):
    return TemplateResponse(request, "library/about.html")


def contact(request):
    return TemplateResponse(request, "library/contact.html")


class NewsListView(generic.ListView):
    """Generic class-based view for a list of news."""
    model = News
    paginate_by = 10


class NewsDetailView(generic.DetailView):
    """Generic class-based detail view for the news."""
    model = News


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
