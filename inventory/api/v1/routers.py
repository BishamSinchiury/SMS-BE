from rest_framework.routers import DefaultRouter
from inventory.api.v1.views.views import (
    DepartmentViewSet,
    ItemsViewSet,
    ItemsLoanViewSet
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'items', ItemsViewSet, basename='items')
router.register(r'items-loan', ItemsLoanViewSet, basename='items-loan')

urlpatterns = router.urls