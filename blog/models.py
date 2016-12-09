from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(help_text='Publish date', auto_created=True)
    content = models.TextField(max_length=10000)
    publisher = models.ForeignKey("auth.User")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=(self.id,))