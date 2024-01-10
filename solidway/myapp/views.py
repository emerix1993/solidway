from django.shortcuts import render
from .models import Item

"""Module containing a function to display a list of items.
This module uses Django to visualize a list of items on a web page."""


def item_list(request):
    items = Item.objects.all()
    return render(request, "myapp/item_list.html", {"items": items})
