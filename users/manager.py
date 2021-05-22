"""
This file is used for creating custom user manager for the correspondent custom user.
"""
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Class for creating custom manager for managing custom user.
    """

    def create_user(self, email=None, password=None, status="ACTIVE", role=None, **extra_fields):
        """
        Function for creating user w.r.t custom user.
        """
        user = self.model(
            email=self.normalize_email(email)
        )
        user.status = status
        user.role = role
        user.is_superuser = False
        user.is_active = True
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Function for creating super user.
        """
        user = self.create_user(
            email,
            password,
            status='ACTIVE'
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
