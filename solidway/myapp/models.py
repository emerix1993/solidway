"""Django model for representing an item.
This model defines a simple representation of an item with a name field."""

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
