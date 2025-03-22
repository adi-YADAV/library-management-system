from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Admin(AbstractUser):
    email = models.EmailField(unique=True)

    # Fix naming conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_admin_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_admin_users_permissions",
        blank=True
    )

    def __str__(self):
        return self.email
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
