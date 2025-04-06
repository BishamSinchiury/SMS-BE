from django.core.management.base import BaseCommand
from inventory.models import Department, DepartmentsEnum

class Command(BaseCommand):
    help = 'Populates the Department model with data from DepartmentsEnum'

    def handle(self, *args, **kwargs):
        # Iterate over DepartmentsEnum and create a department for each enum value
        for department_name in DepartmentsEnum:
            department, created = Department.objects.get_or_create(
                name=department_name.value, 
                defaults={
                    'description': f'{department_name.value.capitalize()} department',
                    'is_active': True
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created department: {department_name.value}'))
            else:
                self.stdout.write(self.style.WARNING(f'Department {department_name.value} already exists'))

