# chat/models.py
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user1 = models.CharField(max_length=255, blank=True, null=True)
    user2 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_full(self):
        return self.user1 and self.user2

    def __str__(self):
        return self.name