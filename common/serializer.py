from django.db.models import F
from rest_framework import serializers

from .models import (
    History,
    Member,
    Program,
    ProgramMembership,
    ProgramReward,
    Reward,
)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    # If no `alias` given, use name as alias


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'


class ProgramMemberSerializer(serializers.ModelSerializer):
    program = serializers.PrimaryKeyRelatedField(read_only=True)
    member = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all())
    member_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProgramMembership
        fields = '__all__'

    def get_member_name(self, obj: ProgramMembership) -> str:
        return obj.member.alias

    def create(self, validated_data):
        if ('program' not in validated_data or
                not validated_data['program']):
            program = Program.objects.get(
                pk=self.context["view"].kwargs['program_pk'])
            validated_data['program'] = program

        return super().create(validated_data)



class ProgramRewardSerializer(serializers.ModelSerializer):
    program = serializers.PrimaryKeyRelatedField(read_only=True)
    reward = serializers.PrimaryKeyRelatedField(
        queryset=Reward.objects.all())
    reward_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProgramReward
        fields = '__all__'

    def get_reward_name(self, obj: ProgramReward) -> str:
        return obj.reward.name

    def create(self, validated_data):
        if ('program' not in validated_data or
                not validated_data['program']):
            program = Program.objects.get(
                pk=self.context["view"].kwargs['program_pk'])
            validated_data['program'] = program

        return super().create(validated_data)


class HistorySerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(read_only=True)
    reward = serializers.PrimaryKeyRelatedField(
        queryset=Reward.objects.all())

    class Meta:
        model = History
        fields = '__all__'

    def create(self, validated_data):
        if ('program' not in validated_data or
                not validated_data['program']):
            program = Program.objects.get(
                pk=self.context["view"].kwargs['program_pk'])
            validated_data['program'] = program

        if ('member' not in validated_data or
                not validated_data['member']):
            member = Member.objects.get(
                pk=self.context["view"].kwargs['member_pk'])
            validated_data['member'] = member

        # Reduce point total for claiming reward
        # Skipping server-side check for point total > 0
        validated_data['value'] = ProgramReward.objects.get(
            program=validated_data['program'],
            reward=validated_data['reward'],
        ).cost

        program_member = ProgramMembership.objects.get(
            program=validated_data['program'],
            member=validated_data['member'],
        )
        program_member.points = F("points") - validated_data['value']
        program_member.save()

        validated_data.pop('program')

        return super().create(validated_data)
