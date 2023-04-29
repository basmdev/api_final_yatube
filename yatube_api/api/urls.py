from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register(r"^posts", PostViewSet, basename="posts")
router.register(r"^groups", GroupViewSet, basename="group")
router.register(
    r"^posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
router.register(r"^follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
