from rest_framework import routers
from .api import AzsViewSet


router = routers.DefaultRouter()
router.register("api/get_dt", AzsViewSet, 'dt')


urlpatterns = router.urls
