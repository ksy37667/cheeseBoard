from django.db import models
from accounts.models import User

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, related_name='authors',on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='최초 생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정된 시간')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# parent 기본값이 None인 이유는 처음 댓글은 부모 댓글이 없기 때문
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply',  null=True, blank=True)
    content = models.CharField(max_length=100)
    create_at= models.DateTimeField(verbose_name='작성시간', auto_now_add=True)