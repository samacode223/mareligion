from django.db import models

# Create your models here.
class PasHadith(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class TroisTestament(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class LaPriere(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class LeJeun(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class LaZakat(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class LeHadj(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class QuestionReponse(models.Model):
    nom=models.CharField(max_length=100)
    question=models.CharField(max_length=500)
    priorite=models.IntegerField()
    reponse=models.TextField()
    def __str__(self):
        return self.question
class AvisCommentaire(models.Model):
    nom=models.CharField(max_length=100)
    numero=models.CharField(max_length=15)
    commentaire=models.CharField(max_length=500)
    def __str__(self):
        return self.nom
class Question(models.Model):
    nom=models.CharField(max_length=100)
    numero=models.CharField(max_length=15)
    question=models.CharField(max_length=500)
    def __str__(self):
        return self.question
class GrandSujet(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class Frere(models.Model):
    titre=models.CharField(max_length=500)
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class LaSource(models.Model):
    titre=models.CharField(max_length=500)
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class Autre(models.Model):
    titre=models.CharField(max_length=500)
    priorite=models.IntegerField()
    contenu=models.TextField()
    def __str__(self):
        return self.titre
class Preche(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='audios/')
    date_upload = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre