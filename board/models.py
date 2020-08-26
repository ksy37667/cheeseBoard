from django.db import models
from accounts.models import User

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='최초 생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정된 시간')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']