from rest_framework.viewsets import ModelViewSet
from inventory.api.v1.serializers.serializers import (
    DepartmentSerializer,
    ItemsSerializer,
    ItemsLoanSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
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
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['department']  # Add department filtering
    pagination_class = LimitOffsetPagination  # Or your preferred pagination

class ItemsLoanViewSet(ModelViewSet):
    queryset = ItemsLoan.objects.all()
    serializer_class = ItemsLoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item = serializer.validated_data['item']
        borrow_qty = serializer.validated_data['borrow_qty']
        status = serializer.validated_data.get('status', 'borrowed')  # Get status

        if status == 'borrowed':
            if borrow_qty > item.quantity:
                raise serializers.ValidationError("Borrow quantity exceeds available stock.")
            # Deduct item quantity if the status is borrowed
            item.quantity -= borrow_qty
            item.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        elif status == 'expense':
            # Handle expense case: Deduct the item from inventory
            item.quantity -= borrow_qty
            item.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        return_type = request.data.get('return_type')  # 'full' or 'partial'
        returned_qty = request.data.get('quantity')  # Used in partial return


        if return_type == 'full':
            # Add all borrowed quantity back
            item = instance.item
            item.quantity += instance.borrow_qty
            item.save()
            instance.delete()
            return Response({"message": "Item fully returned and loan record deleted."}, status=status.HTTP_200_OK)

        elif return_type == 'partial':
            if not returned_qty:
                raise ValidationError("Partial return must include 'returned_qty'.")

            if returned_qty > instance.borrow_qty:
                raise ValidationError("Returned quantity cannot exceed borrowed quantity.")

            # Add returned quantity to item
            item = instance.item
            item.quantity += returned_qty
            item.save()

            # Update remaining borrow quantity
            instance.borrow_qty -= returned_qty
            instance.save()

            return Response({"message": "Partial return processed."}, status=status.HTTP_200_OK)

        else:
            return super().update(request, *args, **kwargs)


