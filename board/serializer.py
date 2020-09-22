from rest_framework import serializers
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')

    # print(author)
    class Meta:
        model = Board
        # fields = '__all__'
        fields = ('id','title', 'content', 'username', 'created_at', 'updated_at')



# 최초의 (부모가 존재하지 않는) 댓글만 가져오는 serializer
class BoardOnlySerializer(serializers.ModelSerializer):
    parent_comment = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'parent_comment')

    def get_parent_comment(self, obj):
        parent_comment = obj.comments.filter(parent=None)
        serializer = CommentSerializer(parent_comment, many=True)
        return serializer.data



class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']

# instance.reply를 통해 자식 댓글을 불러오고, self.__class__를 통해 직렬화가 이루어진다.
# 직렬화 과정 중에 재귀호출이 일어난다(직렬화 -> 호출 -> 직렬화 ->호출 계속 반복)
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data