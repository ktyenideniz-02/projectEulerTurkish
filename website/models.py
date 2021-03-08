from django.conf import settings
from django.db import models
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    text = models.TextField(help_text = 'Use $$...$$ format when entering mathematical equations. For example: $$x^2=4$$')
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title