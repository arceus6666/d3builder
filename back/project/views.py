from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response

from .helper import makeResponse, modelValidator

from .models import User, Build, Skill, Item, BuildGems, BuildCubes, BuildItems, BuildSkills, VoteBuildUser

from .serializers import UserSerializer, BuildSerializer, SkillSerializer, ItemSerializer, BuildGemsSerializer, BuildCubesSerializer, BuildItemsSerializer, BuildSkillsSerializer, VoteBuildUserSerializer


def index(req):
    f = open('project/index.html', 'r')
    mainview = f.read()
    f.close()
    return HttpResponse(mainview)


class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def userbyid(request, uid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = User.objects.get(_id=uid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, UserSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = User.objects.get(_id=uid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListBuild(generics.ListCreateAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


def buildbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = Build.objects.get(_id=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, BuildSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = Build.objects.get(_id=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListSkill(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


def skillbyid(request, sid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = Skill.objects.get(_id=sid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, SkillSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = Skill.objects.get(_id=sid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def itembyid(request, iid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = Item.objects.get(_id=iid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, ItemSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = Item.objects.get(_id=iid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json

def getGems(request):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = Item.objects.get(itype1=1)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, ItemSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = Item.objects.get(itype1=1).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json

class ListBuildGems(generics.ListCreateAPIView):
    queryset = BuildGems.objects.all()
    serializer_class = BuildGemsSerializer


def buildgemsbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = BuildGems.objects.get(id_build=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, BuildGemsSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = BuildGems.objects.get(id_build=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListBuildCubes(generics.ListCreateAPIView):
    queryset = BuildCubes.objects.all()
    serializer_class = BuildCubesSerializer


def buildcubesbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = BuildCubes.objects.get(id_build=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, BuildCubesSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = BuildCubes.objects.get(id_build=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListBuildItems(generics.ListCreateAPIView):
    queryset = BuildItems.objects.all()
    serializer_class = BuildItemsSerializer


def builditemsbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = BuildItems.objects.get(id_build=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, BuildItemsSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = BuildItems.objects.get(id_build=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListBuildSkills(generics.ListCreateAPIView):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer


def buildskillsbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = BuildSkills.objects.get(id_build=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, BuildSkillsSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = BuildSkills.objects.get(id_build=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json


class ListVoteBuildUser(generics.ListCreateAPIView):
    queryset = VoteBuildUser.objects.all()
    serializer_class = VoteBuildUserSerializer


def votebuiluserdbyid(request, bid=''):
    method = request.method
    json = makeResponse(None, 500, 'Something wrong happened')
    try:
        queryset = VoteBuildUser.objects.get(id_build=bid)
    except:
        return makeResponse(None, 204, 'No Element Found')
    if method == 'GET':
        data = queryset.__json__
        json = makeResponse(data, 200, 'Element Found')
    elif method == 'DELETE':
        data = queryset.__json__
        queryset.delete()
        json = makeResponse(data, 200, 'Element Deleted')
    elif method == 'PUT':
        validated = modelValidator(queryset, request, VoteBuildUserSerializer)
        if validated is None:
            json = makeResponse(None, 406, 'Wrong arguments')
        else:
            validated.save()
            data = VoteBuildUser.objects.get(id_build=bid).__json__
            json = makeResponse(data, 200, 'Element Updated')
    return json
