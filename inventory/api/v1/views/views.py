from rest_framework.viewsets import ModelViewSet
from inventory.api.v1.serializers.serializers import (
    DepartmentSerializer,
    ItemsSerializer,
    ItemsLoanSerializer
)
from inventory.models import (
    Department, 
    Items, 
    ItemsLoan
)

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ItemsViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemsLoanViewSet(ModelViewSet):
    queryset = ItemsLoan.objects.all()
    serializer_class = ItemsLoanSerializer