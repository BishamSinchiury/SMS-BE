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
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    class Meta:
        model = Items
        fields = '__all__'
        read_only_fields = [
            "created_at",
        ]
    def to_representation(self, instance):
        """Customize output when returning data (GET)."""
        representation = super().to_representation(instance)
        # Replace department ID with its name
        if instance.department:
            representation['department'] = instance.department.name
        return representation

class ItemsLoanSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = ItemsLoan
        fields = '__all__'
        read_only_fields = [
            "created_at",
        ]
    def to_representation(self, instance):
        """Customize GET response to show item name instead of item ID."""
        representation = super().to_representation(instance)
        if instance.item:
            representation['item'] = instance.item.name
        return representation