from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField()
    current_class = models.CharField(max_length=20)
    section = models.CharField(max_length=5)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.current_class}-{self.section})"