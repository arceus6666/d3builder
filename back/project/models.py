
from __future__ import unicode_literals
# from django.db import models
from djongo import models  # Note the import method for mongo models

# Create your models here.


# class Student(models.Model):  # Collection name
#     # Auto updated when data is inserted
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
#     # Auto updated when data is altered
#     updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

#     # Documents
#     name = models.CharField(max_length=20, null=True)
#     age = models.IntegerField(default=10, null=True)
#     roll_number = models.CharField(max_length=20, null=True)

#     def __str__(self):
#         return self.name


# class Project(models.Model):
#     medium_url = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.medium_url


class User(models.Model):
    first_name = models.CharField(default='',max_length=200)
    last_name = models.CharField(default='',max_length=200)
    username = models.CharField(max_length=200)
    image = models.CharField(default='0',max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    language = models.CharField(default='en',max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    role = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Build(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    info = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    stype = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    itype = models.IntegerField()
    rarity = models.IntegerField()
    image = models.CharField(max_length=200)
    info = models.TextField()

    def __str__(self):
        return self.name


class BuildGems(models.Model):
    id_build = models.CharField(max_length=200)
    id_gem1 = models.CharField(max_length=200)
    id_gem2 = models.CharField(max_length=200)
    id_gem3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BuildCubes(models.Model):
    id_build = models.CharField(max_length=200)
    id_item1 = models.CharField(max_length=200)
    id_item2 = models.CharField(max_length=200)
    id_item3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BuildItems(models.Model):
    id_build = models.CharField(max_length=200)
    id_item1 = models.CharField(max_length=200)
    id_item2 = models.CharField(max_length=200)
    id_item3 = models.CharField(max_length=200)
    id_item4 = models.CharField(max_length=200)
    id_item5 = models.CharField(max_length=200)
    id_item6 = models.CharField(max_length=200)
    id_item7 = models.CharField(max_length=200)
    id_item8 = models.CharField(max_length=200)
    id_item9 = models.CharField(max_length=200)
    id_item10 = models.CharField(max_length=200)
    id_item11 = models.CharField(max_length=200)
    id_item12 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BuildSkills(models.Model):
    id_build = models.CharField(max_length=200)
    id_skill1 = models.CharField(max_length=200)
    id_skill2 = models.CharField(max_length=200)
    id_skill3 = models.CharField(max_length=200)
    id_skill4 = models.CharField(max_length=200)
    id_skill5 = models.CharField(max_length=200)
    id_skill6 = models.CharField(max_length=200)
    id_skill7 = models.CharField(max_length=200)
    id_skill8 = models.CharField(max_length=200)
    id_skill9 = models.CharField(max_length=200)
    id_skill10 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class VoteBuildUser(models.Model):
    id_build = models.CharField(max_length=200)
    id_user = models.CharField(max_length=200)

    def __str__(self):
        return self.name
