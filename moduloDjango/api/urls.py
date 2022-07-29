from django.conf.urls import url
from api import views 

urlpatterns = [
    url('alumno/', views.GetAlumno.as_view()),
    url('aula/', views.GetAula.as_view()),
    url('curso/', views.GetCurso.as_view()),
    url('materia/', views.GetMateria.as_view()),
    url('profesora/', views.GetProfesorA.as_view()),
    url('presencia/', views.GetPresencia.as_view()),
    url('cxmxpxa/', views.GetCxmxpxa.as_view()),
    url('related/', views.GetRelated.as_view()),

]