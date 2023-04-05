from rest_framework import routers
from .api import AzsViewSet


"""Создадим дефолтный роутер"""
router = routers.DefaultRouter()
"""Зарегистрируем api url с queryset'ом"""
router.register("api/get_dt", AzsViewSet, 'dt')


urlpatterns = router.urls
