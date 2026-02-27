from rest_framework import serializers
from . import models

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'
class AutreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Autre
        fields = '__all__'
class PasHadithSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PasHadith
        fields = '__all__'
class TroisTestamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TroisTestament
        fields = '__all__'
class LaPriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaPriere
        fields = '__all__'
class LeJeunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeJeun
        fields = '__all__'
class LeHadjSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeHadj
        fields = '__all__'
class LaZakatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaZakat
        fields = '__all__'
class GrandSujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GrandSujet
        fields = '__all__'
class QuestionReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionReponse
        fields = '__all__'
class FrereSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Frere
        fields = '__all__'
class AvisCommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvisCommentaire
        fields = '__all__'
class LaSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaSource
        fields = '__all__'
class PrecheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Preche
        fields = '__all__'