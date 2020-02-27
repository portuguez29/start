from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/user',LeadViewSet,'users')

urlpatterns = router.urls