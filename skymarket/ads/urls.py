from django.urls import include, path
from rest_framework_nested import routers
from ads.views import AdViewSet, CommentViewSet

ads_router = routers.SimpleRouter()
ads_router.register(r"ads", AdViewSet)

ads_router.register("ads", AdViewSet, basename="ads")
comments_router = routers.NestedSimpleRouter(ads_router, r"ads", lookup="ad")
comments_router.register(r"comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]