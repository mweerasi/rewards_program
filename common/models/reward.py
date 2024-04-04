from django.db import models


class Reward(models.Model):
    """Representation of a reward for a rewards program."""

    # Name of the reward
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
