from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="news/%Y/%m/%d/")

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular news instance."""
        return reverse('news-detail', args=[str(self.id)])
