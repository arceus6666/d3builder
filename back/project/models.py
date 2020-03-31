
from __future__ import unicode_literals
from djongo import models


class User(models.Model):
    _id = models.CharField(max_length=200)
    first_name = models.CharField(default='', max_length=200)
    last_name = models.CharField(default='', max_length=200)
    username = models.CharField(max_length=200, unique=True)
    image = models.CharField(default='0', max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    language = models.CharField(default='en', max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    role = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    @property
    def __json__(self):
        return {
            '_id': self._id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'image': self.image,
            'password': self.password,
            'email': self.email,
            'language': self.language,
            'registration_date': self.registration_date,
            'role': self.role
        }


class Build(models.Model):
    _id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    info = models.TextField(default="")

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            '_id': self._id,
            'name': self.name,
            'user': self.user,
            'info': self.info
        }


class Skill(models.Model):
    _id = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200, unique=True)
    stype = models.IntegerField()
    info = models.TextField(default="")

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            '_id': self._id,
            'name': self.name,
            'image': self.image,
            'stype': self.stype,
            'info': self.info
        }


class Item(models.Model):
    _id = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    itype1 = models.IntegerField()
    itype2 = models.IntegerField()
    rarity = models.IntegerField()
    image = models.CharField(max_length=200, unique=True)
    info = models.TextField(default="")

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            '_id': self._id,
            'name': self.name,
            'itype1': self.itype1,
            'itype2': self.itype2,
            'rarity': self.rarity,
            'image': self.image,
            'info': self.info
        }


class BuildGems(models.Model):
    id_build = models.CharField(max_length=200, unique=True)
    id_gem1 = models.CharField(max_length=200)
    id_gem2 = models.CharField(max_length=200)
    id_gem3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            'id_build': self.id_build,
            'id_gem1': self.id_gem1,
            'id_gem2': self.id_gem2,
            'id_gem3': self.id_gem3
        }


class BuildCubes(models.Model):
    id_build = models.CharField(max_length=200, unique=True)
    id_item1 = models.CharField(max_length=200)
    id_item2 = models.CharField(max_length=200)
    id_item3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            'id_build': self.id_build,
            'id_item1': self.id_item1,
            'id_item2': self.id_item2,
            'id_item3': self.id_item3
        }


class BuildItems(models.Model):
    id_build = models.CharField(max_length=200, unique=True)
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

    @property
    def __json__(self):
        return {
            'id_build': self.id_build,
            'id_item1': self.id_item1,
            'id_item2': self.id_item2,
            'id_item3': self.id_item3,
            'id_item4': self.id_item4,
            'id_item5': self.id_item5,
            'id_item6': self.id_item6,
            'id_item7': self.id_item7,
            'id_item8': self.id_item8,
            'id_item9': self.id_item9,
            'id_item10': self.id_item10,
            'id_item11': self.id_item11,
            'id_item12': self.id_item12
        }


class BuildSkills(models.Model):
    id_build = models.CharField(max_length=200, unique=True)
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

    @property
    def __json__(self):
        return {
            'id_build': self.id_build,
            'id_skill1': self.id_skill1,
            'id_skill2': self.id_skill2,
            'id_skill3': self.id_skill3,
            'id_skill4': self.id_skill4,
            'id_skill5': self.id_skill5,
            'id_skill6': self.id_skill6,
            'id_skill7': self.id_skill7,
            'id_skill8': self.id_skill8,
            'id_skill9': self.id_skill9,
            'id_skill10': self.id_skill10,
        }


class VoteBuildUser(models.Model):
    value = models.BooleanField()
    id_build = models.CharField(max_length=200)
    id_user = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def __json__(self):
        return {
            'value': self.value,
            'id_build': self.id_build,
            'id_user': self.id_user
        }
