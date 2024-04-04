from django.urls import include, path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register(r'members', views.MemberView, 'member')
router.register(r'programs', views.ProgramView, 'program')
router.register(r'rewards', views.RewardView, 'reward')

program_router = routers.NestedSimpleRouter(
    router, r'programs', lookup='program')
program_router.register(
    r'members', views.ProgramMembersView, 'program-members')
program_router.register(
    r'rewards', views.ProgramRewardsView, 'program-rewards')

program_member_router = routers.NestedSimpleRouter(
    program_router, r'members', lookup='member')
program_member_router.register(
    r'member_rewards', views.HistoryView)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(program_router.urls)),
    path(r'', include(program_member_router.urls)),
]
