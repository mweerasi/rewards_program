from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import (
    Member,
    Program,
    Reward,
    ProgramMembership,
    ProgramReward,
    History,
)


class MemberTests(APITestCase):
    def test_create_member(self):
        url = reverse('member-list')
        data = {'name': 'John Doe', 'alias': 'johndoe'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 1)
        self.assertEqual(Member.objects.get().name, 'John Doe')

    def test_get_member(self):
        member = Member.objects.create(name='Jane Doe', alias='janedoe')
        url = reverse('member-detail', args=[member.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Doe')


class ProgramTests(APITestCase):
    def test_create_program(self):
        url = reverse('program-list')
        data = {'name': 'Loyalty Program'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Program.objects.count(), 1)
        self.assertEqual(Program.objects.get().name, 'Loyalty Program')

    def test_get_program(self):
        program = Program.objects.create(name='Rewards Program')
        url = reverse('program-detail', args=[program.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Rewards Program')


class RewardTests(APITestCase):
    def test_create_reward(self):
        url = reverse('reward-list')
        data = {'name': 'Free Coffee'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reward.objects.count(), 1)
        self.assertEqual(Reward.objects.get().name, 'Free Coffee')

    def test_get_reward(self):
        reward = Reward.objects.create(name='50% Discount')
        url = reverse('reward-detail', args=[reward.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '50% Discount')


class ProgramMembershipTests(APITestCase):
    def setUp(self):
        self.program = Program.objects.create(name='Test Program')
        self.member = Member.objects.create(name='Test Member', alias='testmember')

    def test_create_program_membership(self):
        url = reverse('program-members-list', args=[self.program.id])
        data = {'member': self.member.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgramMembership.objects.count(), 1)
        self.assertEqual(ProgramMembership.objects.get().member.name, 'Test Member')

    def test_get_program_membership(self):
        membership = ProgramMembership.objects.create(program=self.program, member=self.member)
        url = reverse('program-members-detail', args=[self.program.id, membership.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['member_name'], 'testmember')


class ProgramRewardTests(APITestCase):
    def setUp(self):
        self.program = Program.objects.create(name='Test Program')
        self.reward = Reward.objects.create(name='Test Reward')

    def test_create_program_reward(self):
        url = reverse('program-rewards-list', args=[self.program.id])
        data = {'reward': self.reward.id, 'cost': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgramReward.objects.count(), 1)
        self.assertEqual(ProgramReward.objects.get().reward.name, 'Test Reward')

    def test_get_program_reward(self):
        program_reward = ProgramReward.objects.create(program=self.program, reward=self.reward, cost=200)
        url = reverse('program-rewards-detail', args=[self.program.id, program_reward.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reward_name'], 'Test Reward')


class HistoryTests(APITestCase):
    def setUp(self):
        self.program = Program.objects.create(name='Test Program')
        self.member = Member.objects.create(name='Test Member', alias='testmember')
        self.reward = Reward.objects.create(name='Test Reward')
        self.program_membership = ProgramMembership.objects.create(program=self.program, member=self.member, points=1000)
        self.program_reward = ProgramReward.objects.create(program=self.program, reward=self.reward, cost=500)

    def test_create_history(self):
        url = reverse('history-list', args=[self.program.id, self.program_membership.id])
        data = {'reward': self.reward.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(History.objects.count(), 1)
        self.assertEqual(History.objects.get().reward.name, 'Test Reward')

    def test_get_history(self):
        history = History.objects.create(member=self.member, reward=self.reward, value=500)
        url = reverse('history-detail', args=[self.program.id, self.program_membership.id, history.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['member_name'], 'Test Member')
        self.assertEqual(response.data['reward_name'], 'Test Reward')
