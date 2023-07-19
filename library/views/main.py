from django.shortcuts import render
from django.template.response import TemplateResponse

from library.models import News


def index(request):
    news = News.objects.all()[:5]
    context = {"news": news}
    return render(request, template_name="library/index.html", context=context)


def about(request):
    return TemplateResponse(request, "library/about.html")


def contact(request):
    return TemplateResponse(request, "library/contact.html")
