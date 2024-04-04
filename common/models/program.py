from django.db import models


class Program(models.Model):
    """Representation of a rewards program."""

    # Name of the rewards program
    name = models.CharField(blank=True, max_length=100)

    # Additional fields like company, etc.
    def __str__(self):
        return self.name


class ProgramMembership(models.Model):
    """Representation of a member of a rewards program. """
    program = models.ForeignKey('common.Program',
                related_name='memberships', on_delete=models.CASCADE)
    member = models.ForeignKey('common.Member',
                related_name='memberships', on_delete=models.CASCADE)

    # Total points currently achieved by member for the program
    points = models.IntegerField(default=0)


class ProgramReward(models.Model):
    """Representation for a program reward."""
    program = models.ForeignKey('common.Program',
                related_name='program_rewards', on_delete=models.CASCADE)
    reward = models.ForeignKey('common.Reward',
                related_name='program_rewards', on_delete=models.CASCADE)

    # The cost for this reward in this program
    cost = models.IntegerField(default=100)

    # Max number of times reward can be claimed
    max_claim = models.IntegerField(default=None, null=True)
