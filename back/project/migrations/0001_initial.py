# Generated by Django 2.2.11 on 2020-03-31 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('info', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='BuildCubes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_build', models.CharField(max_length=200, unique=True)),
                ('id_item1', models.CharField(max_length=200)),
                ('id_item2', models.CharField(max_length=200)),
                ('id_item3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BuildGems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_build', models.CharField(max_length=200, unique=True)),
                ('id_gem1', models.CharField(max_length=200)),
                ('id_gem2', models.CharField(max_length=200)),
                ('id_gem3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BuildItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_build', models.CharField(max_length=200, unique=True)),
                ('id_item1', models.CharField(max_length=200)),
                ('id_item2', models.CharField(max_length=200)),
                ('id_item3', models.CharField(max_length=200)),
                ('id_item4', models.CharField(max_length=200)),
                ('id_item5', models.CharField(max_length=200)),
                ('id_item6', models.CharField(max_length=200)),
                ('id_item7', models.CharField(max_length=200)),
                ('id_item8', models.CharField(max_length=200)),
                ('id_item9', models.CharField(max_length=200)),
                ('id_item10', models.CharField(max_length=200)),
                ('id_item11', models.CharField(max_length=200)),
                ('id_item12', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BuildSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_build', models.CharField(max_length=200, unique=True)),
                ('id_skill1', models.CharField(max_length=200)),
                ('id_skill2', models.CharField(max_length=200)),
                ('id_skill3', models.CharField(max_length=200)),
                ('id_skill4', models.CharField(max_length=200)),
                ('id_skill5', models.CharField(max_length=200)),
                ('id_skill6', models.CharField(max_length=200)),
                ('id_skill7', models.CharField(max_length=200)),
                ('id_skill8', models.CharField(max_length=200)),
                ('id_skill9', models.CharField(max_length=200)),
                ('id_skill10', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('itype1', models.IntegerField()),
                ('itype2', models.IntegerField()),
                ('rarity', models.IntegerField()),
                ('image', models.CharField(max_length=200, unique=True)),
                ('info', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('image', models.CharField(max_length=200, unique=True)),
                ('stype', models.IntegerField()),
                ('info', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('image', models.CharField(default='0', max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('language', models.CharField(default='en', max_length=200)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('role', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VoteBuildUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('id_build', models.CharField(max_length=200)),
                ('id_user', models.CharField(max_length=200)),
            ],
        ),
    ]
