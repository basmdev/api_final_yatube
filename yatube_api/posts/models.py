from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель Group."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title[:35]


class Post(models.Model):
    """Модель Post."""

    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text[:35]


class Comment(models.Model):
    """Модель Comment."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:35]


class Follow(models.Model):
    """Модель Follow."""

    user = models.ForeignKey(
        User,
        related_name="follower",
        on_delete=models.CASCADE,
    )
    following = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text[:35]

    class Meta:
        constraints = (
            models.UniqueConstraint(
                name="unique_follow", fields=("user", "following")
            ),
        )
