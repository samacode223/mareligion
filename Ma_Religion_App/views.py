from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models,serializers
# Create your views here.
def GetIndex(request):
    return HttpResponse("<center><h1>Ma Religion <h1/><center/>")

@api_view(['GET'])
def GetTroisTestament(request):
    result =models.TroisTestament.objects.all()
    serializer = serializers.TroisTestamentSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetPasHadith(request):
    result =models.PasHadith.objects.all()
    serializer = serializers.PasHadithSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetLaPriere(request):
    result =models.LaPriere.objects.all()
    serializer = serializers.LaPriereSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetLeJeun(request):
    result =models.LeJeun.objects.all()
    serializer = serializers.LeJeunSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetLaZakat(request):
    result =models.LaZakat.objects.all()
    serializer = serializers.LaZakatSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetLeHadj(request):
    result =models.LeHadj.objects.all()
    serializer = serializers.LeHadjSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetGrandSujet(request):
    result =models.GrandSujet.objects.all()
    serializer = serializers.GrandSujetSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetQuestionReponse(request):
    result =models.QuestionReponse.objects.all()
    serializer = serializers.QuestionSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetAvisCommentaire(request):
    result =models.AvisCommentaire.objects.all()
    serializer = serializers.AvisCommentaireSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetFrere(request):
    result =models.Frere.objects.all()
    serializer = serializers.FrereSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetTroisTestament(request):
    result =models.TroisTestament.objects.all()
    serializer = serializers.TroisTestamentSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetLaSoure(request):
    result =models.LaSource.objects.all()
    serializer = serializers.LaSourceSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetAutre(request):
    result =models.Autre.objects.all()
    serializer = serializers.AutreSerializer (result, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GetPreche(request):
    result =models.Preche.objects.all()
    serializer = serializers.PrecheSerializer (result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def PostAvisCommentaire(request):
    serializer = serializers.AvisCommentaireSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) # pyright: ignore[reportUndefinedVariable]
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # pyright: ignore[reportUndefinedVariable]
@api_view(['POST'])
def PostQuestion(request):
    serializer = serializers.QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) # pyright: ignore[reportUndefinedVariable]
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # pyright: ignore[reportUndefinedVariable]

# @api_view(['GET'])
# def GetQuestion(request):
#     result =models.Question.objects.all()
#     serializer = serializers.QuestionSerializer (result, many=True)
#     return Response(serializer.data)