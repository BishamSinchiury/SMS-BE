from enum import Enum

class DepartmentsEnum(Enum):
    ADMIN = "admin"
    LAB = "lab"
    RECEPTION = "reception"
    SPORTS = "sports"
    LIBRARY = "library"
    KITCHEN = "kitchen"
    CONSTRUCTION = "construction"
    MAINTENANCE = "maintenance"
    GENERAL = "general"

    @classmethod
    def choices(cls):
        """
        Returns a tuple of (value, value) pairs where the display name matches the lowercase value.
        Suitable for Django model fields.
        """
        return [(member.value, member.value) for member in cls]