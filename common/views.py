from django.http import HttpResponse
from rest_framework import viewsets

from .models import (
    History,
    Member,
    Program,
    ProgramMembership,
    ProgramReward,
    Reward,
)
from .serializer import (
    HistorySerializer,
    MemberSerializer,
    ProgramSerializer,
    ProgramMemberSerializer,
    ProgramRewardSerializer,
    RewardSerializer,
)


def index(request):
    return HttpResponse("Hello, world. You're at the members index.")

class MemberView(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('name')
    serializer_class = MemberSerializer


class ProgramView(viewsets.ModelViewSet):
    """
    API endpoint that allows reward programs to be viewed or edited.
    """
    queryset = Program.objects.all().order_by('name')
    serializer_class = ProgramSerializer


class RewardView(viewsets.ModelViewSet):
    """
    API endpoint that allows rewards to be viewed or edited.
    """
    queryset = Reward.objects.all().order_by('name')
    serializer_class = RewardSerializer


class ProgramMembersView(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be added to programs.
    """
    queryset = ProgramMembership.objects.all()
    serializer_class = ProgramMemberSerializer

    def get_queryset(self):
        return ProgramMembership.objects.filter(
            program = self.kwargs['program_pk']
        )


class ProgramRewardsView(viewsets.ModelViewSet):
    """
    API endpoint that allows rewards to be added to programs.
    """
    queryset = ProgramReward.objects.all()
    serializer_class = ProgramRewardSerializer

    def get_queryset(self):
        return ProgramReward.objects.filter(
            program = self.kwargs['program_pk']
        )


class HistoryView(viewsets.ModelViewSet):
    """
    API endpoint to link a member and a reward.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        return History.objects.filter(
            member__memberships = self.kwargs['member_pk'],
            reward__program_rewards__program = self.kwargs['program_pk'],
        )
