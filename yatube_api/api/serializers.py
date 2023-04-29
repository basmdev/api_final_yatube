from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import CurrentUserDefault

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = ("id", "text", "author", "created", "post")
        read_only_fields = ("post",)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username",
        read_only=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ("id", "user", "following")
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Подписка уже активна!",
            ),
        )

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError("Подписка невозможна!")
        return data
