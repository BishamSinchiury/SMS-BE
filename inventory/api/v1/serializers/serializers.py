from rest_framework import serializers
from inventory.models import Department, Items, ItemsLoan

class DepartmentSerializer(
    serializers.ModelSerializer
    ):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = [
            "created_at",
        ]

class ItemsSerializer(
    serializers.ModelSerializer
    ):
    class Meta:
        model = Items
        fields = '__all__'

class ItemsLoanSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = ItemsLoan
        fields = '__all__'  