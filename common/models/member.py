from django.db import models


class Member(models.Model):
    """Representation of a rewards member. """

    name = models.CharField(blank=True, max_length=100)

    # Additional fields like email, phone #, etc.
    alias = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.alias
