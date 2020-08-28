from rest_framework import serializers
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


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

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data