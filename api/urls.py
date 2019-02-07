from .views import ObjectifViewSet, ObjectifChoiceViewSet, SportChoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'objectif', ObjectifViewSet, basename='objectif')
router.register(r'objectif_choice', ObjectifChoiceViewSet, basename='objectif_choice')
router.register(r'sport_choice', SportChoiceViewSet, basename='sport_choice')
urlpatterns = router.urls
