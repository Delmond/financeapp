from news import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'news', views.FeedViewSet, basename="news")

urlpatterns = router.urls