from django.contrib import admin

# Register your models here.

# from .models import Project, Student
from .models import User, Build, Skill, Item, BuildGems, BuildCubes, BuildItems, BuildSkills, VoteBuildUser


admin.site.register(User)
admin.site.register(Build)
admin.site.register(Skill)
admin.site.register(Item)
admin.site.register(BuildGems)
admin.site.register(BuildCubes)
admin.site.register(BuildItems)
admin.site.register(BuildSkills)
admin.site.register(VoteBuildUser)
# model has been registered to admin
