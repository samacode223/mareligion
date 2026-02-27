from django.urls import path
from . import views

urlpatterns=[
    path("",views.GetIndex),
    path("pashadith/",views.GetPasHadith),
    path("troistestaments/",views.GetTroisTestament),
    path("lapriere/",views.GetLaPriere),
    path("lejeun/",views.GetLeJeun),
    path("lazakat/",views.GetLaZakat),
    path("lehadj/",views.GetLeHadj),
    path("grandsujet/",views.GetGrandSujet),
    path("questionreponse/",views.GetQuestionReponse),
    path("frere/",views.GetFrere),
    path("aviscommentaire/",views.GetAvisCommentaire),
    path("autre/",views.GetAutre),
    path("preche/",views.GetPreche),
    path("lasource",views.GetLaSoure),

    path("postaviscommentaire/",views.PostAvisCommentaire),
    path("postquestion/",views.PostQuestion),
]