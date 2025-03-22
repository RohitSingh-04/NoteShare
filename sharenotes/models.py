from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    shared = models.BooleanField(default=False)
    shared_with = models.ManyToManyField(User, related_name='shared_with', blank=True)

    def __str__(self):
        return self.title
