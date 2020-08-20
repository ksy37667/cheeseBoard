from django.db import models
from django.conf import settings
# # Create your models here.


class Post(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='글쓴이')
    title = models.CharField(max_length=128)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)