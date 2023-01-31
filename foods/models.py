# models.py
from django.db import models
from datetime import datetime, timedelta
from markdownx.models import MarkdownxField

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Convert HTML to markdown
import markdownify


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep = models.CharField(max_length=255)
    cook = models.CharField(max_length=255)
    servings = models.IntegerField(default=1, null=True, blank=True)
    image = models.ImageField(upload_to="media/")
    ingredients = MarkdownxField()
    directions = MarkdownxField()
    notes = models.TextField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def formatted_ingredients(self):
        return markdownify(self.ingredients)

    @property
    def formatted_directions(self):
        return markdownify(self.directions)
