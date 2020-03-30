from rest_framework import generics
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from braces.views import CsrfExemptMixin

from .models import User, Build, Skill, Item, BuildGems, BuildCubes, BuildItems, BuildSkills, VoteBuildUser
# from .serializers import ProjectSerializer, StudentSerializer, UserSerializer
from .serializers import UserSerializer, BuildSerializer, SkillSerializer, ItemSerializer, BuildGemsSerializer, BuildCubesSerializer, BuildItemsSerializer, BuildSkillsSerializer, VoteBuildUserSerializer

# @csrf_exempt


# class ListProject(CsrfExemptMixin, generics.ListCreateAPIView):
# class ListProject(generics.ListCreateAPIView):
#     # authentication_classes = []
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# @csrf_exempt


# class DetailProject(CsrfExemptMixin, generics.RetrieveUpdateDestroyAPIView):
# class DetailProject(generics.RetrieveUpdateDestroyAPIView):
#     # authentication_classes = []
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# class ListStudent(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

mainview = '''
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>D3Builder api</title>
  <style>
    html,
    body {
      height: 100%;
    }

    body {
      margin: 50px;
      font-size: 100%;
      line-height: 1.5;
      font-family: Calibri;
      background: #334d50;
      background: -webkit-linear-gradient(to right, #cbcaa5, #334d50);
      background: linear-gradient(to right, #cbcaa5, #334d50);

    }

    *,
    *:before,
    *:after {
      box-sizing: border-box;
    }

    .cf:before,
    .cf:after {
      content: " ";
      display: table;
    }

    .cf:after {
      clear: both;
    }

    .cf {
      *zoom: 1;
    }

    .wrapper {
      width: 50%;
      margin: 50px auto;
      background: #fff;
      padding: 2em;
    }

    ul {
      counter-reset: my-counter;
      list-style-type: none;
    }

    ul ol {
      margin-left: 0.9em;
    }

    ul li {
      line-height: 1.5;
    }

    ul li::before {
      font-weight: 700;
      text-transform: uppercase;
      padding-right: 3px;
    }

    h1 {
      font-family: "Fjalla One", sans-serif;
      font-size: 3em;
      text-transform: uppercase;
      text-align: center;
      font-weight: 400;
      color: rgb(25, 159, 158);
      border-bottom: 1px solid rgb(25, 159, 158);
      margin-bottom: 1em;
    }

    a {
      font-size: 2em;
      color: #cbcaa5;
      text-decoration: none;
    }

  </style>
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
    integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
</head>

<body>
  <div class="wrapper">
    <h1>List of available pages</h1>
    <ul>
      <li><a href="/api/user"><i class="fas fa-angle-right"></i> Users section</a></li>
      <li><a href="/api/build"><i class="fas fa-angle-right"></i> Builds section</a></li>
      <li><a href="/api/skill"><i class="fas fa-angle-right"></i> Skills section</a></li>
      <li><a href="/api/item"><i class="fas fa-angle-right"></i> Items section</a></li>
      <li><a href="/api/buildgems"><i class="fas fa-angle-right"></i> Build - Gems conection section</a></li>
      <li><a href="/api/buildcubes"><i class="fas fa-angle-right"></i> Build - Cube items conection section</a></li>
      <li><a href="/api/builditems"><i class="fas fa-angle-right"></i> Build - Items conection section</a></li>
      <li><a href="/api/buildskills"><i class="fas fa-angle-right"></i> Build - Skills conection section</a></li>
      <li><a href="/api/votebuilduser"><i class="fas fa-angle-right"></i> Vote - Build - User conection section</a></li>
    </ul>
  </div>
</body>

</html>

'''

def index(req):
  return HttpResponse(mainview)

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListBuild(generics.ListCreateAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class DetailBuild(generics.RetrieveUpdateDestroyAPIView):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class ListSkill(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class DetailSkill(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ListItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DetailItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListBuildGems(generics.ListCreateAPIView):
    queryset = BuildGems.objects.all()
    serializer_class = BuildGemsSerializer


class DetailBuildGems(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildGems.objects.all()
    serializer_class = BuildGemsSerializer


class ListBuildCubes(generics.ListCreateAPIView):
    queryset = BuildCubes.objects.all()
    serializer_class = BuildCubesSerializer


class DetailBuildCubes(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildCubes.objects.all()
    serializer_class = BuildCubesSerializer


class ListBuildItems(generics.ListCreateAPIView):
    queryset = BuildItems.objects.all()
    serializer_class = BuildItemsSerializer


class DetailBuildItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildItems.objects.all()
    serializer_class = BuildItemsSerializer


class ListBuildSkills(generics.ListCreateAPIView):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer


class DetailBuildSkills(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer


class ListVoteBuildUser(generics.ListCreateAPIView):
    queryset = VoteBuildUser.objects.all()
    serializer_class = VoteBuildUserSerializer


class DetailVoteBuildUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoteBuildUser.objects.all()
    serializer_class = VoteBuildUserSerializer
