from django.db import models
from inventory.constants import DepartmentsEnum
from core.models import Auditable
from django.utils import timezone

# Create your models here.
class Department(Auditable):
    name = models.CharField(
        max_length=20,
        choices=DepartmentsEnum.choices(),
        default=DepartmentsEnum.GENERAL.value
    )
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Items(Auditable):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    exp_date = models.DateField()
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE,
        related_name="items"
        )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

class ItemsLoan(models.Model):
    item = models.ForeignKey(
        Items, 
        on_delete=models.SET_NULL,  # Set to NULL if the item is deleted
        related_name="itemloans", 
        null=True  # Allows the foreign key to be NULL
    )
    borrower_name = models.CharField(
        max_length=100
        )  
    borrower_contact = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
        )
    borrow_qty = models.IntegerField(
        default=1
        )  
    loan_date = models.DateField(
        default=timezone.now
        ) 
    return_date = models.DateField() 
    status = models.CharField(
        max_length=20,
        choices=[
            ('borrowed', 'Borrowed'), 
            ('returned', 'Returned'),
            ('in_stock', 'In_stock')
            ],
        default='in_stock'
    ) 
    returned_on = models.DateField(
        blank=True, 
        null=True
        )  

    def __str__(self):
        return f"{self.item.name} loaned to {self.borrower_name}"

    def is_overdue(self):
        """Check if the loan is overdue."""
        return self.status == 'borrowed' and self.return_date < timezone.now().date()

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
