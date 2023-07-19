from django.views import generic

from library.models import News


class NewsListView(generic.ListView):
    """Generic class-based view for a list of news."""
    model = News
    paginate_by = 5


class NewsDetailView(generic.DetailView):
    """Generic class-based detail view for the news."""
    model = News


class NewsCreateView(generic.CreateView):
    model = News
    fields = ['title', 'content', 'photo']
