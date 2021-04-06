from rest_framework.routers import DefaultRouter

from app.views import StudentViewSet

router = DefaultRouter()
router.register(r'', StudentViewSet)
urlpatterns = router.urls


