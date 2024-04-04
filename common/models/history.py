from django.db import models


class History(models.Model):
    """Representation of a member redeeming a reward."""

    member = models.ForeignKey('common.Member',
                related_name='history', null=True, on_delete=models.SET_NULL)
    reward = models.ForeignKey('common.Reward',
                related_name='history', null=True, on_delete=models.SET_NULL)

    # Point value associated with this history
    value = models.IntegerField(default=None, null=True)

    # Associated time
    created_on = models.DateTimeField(auto_now_add=True)
