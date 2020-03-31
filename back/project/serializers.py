from rest_framework import serializers
# from .models import Project, Student, User
from .models import User, Build, Skill, Item, BuildGems, BuildCubes, BuildItems, BuildSkills, VoteBuildUser


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'medium_url',
#             'description',
#         )
#         model = Project


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'name',
#             'age',
#             'roll_number',
#             'created_at',
#             'updated_at'
#         )
#         model = Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            '_id',
            'first_name',
            'last_name',
            'username',
            'image',
            'password',
            'email',
            'language',
            'registration_date',
            'role'
        )
        model = User


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            '_id',
            'name',
            'user',
            'info'
        )
        model = Build


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            '_id',
            'name',
            'image',
            'stype',
            'info'
        )
        model = Skill


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            '_id',
            'name',
            'itype1',
            'itype2',
            'rarity',
            'image',
            'info'
        )
        model = Item


class BuildGemsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'id_build',
            'id_gem1',
            'id_gem2',
            'id_gem3'
        )
        model = BuildGems


class BuildCubesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'id_build',
            'id_item1',
            'id_item2',
            'id_item3'
        )
        model = BuildCubes


class BuildItemsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'id_build',
            'id_item1',
            'id_item2',
            'id_item3',
            'id_item4',
            'id_item5',
            'id_item6',
            'id_item7',
            'id_item8',
            'id_item9',
            'id_item10',
            'id_item11',
            'id_item12',
        )
        model = BuildItems


class BuildSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'id_build',
            'id_skill1',
            'id_skill2',
            'id_skill3',
            'id_skill4',
            'id_skill5',
            'id_skill6',
            'id_skill7',
            'id_skill8',
            'id_skill9',
            'id_skill10'
        )
        model = BuildSkills


class VoteBuildUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'id_build',
            'id_user'
        )
        model = VoteBuildUser
