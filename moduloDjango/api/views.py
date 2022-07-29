from rest_framework.generics import ListAPIView
from api.models import *
from api.serializers import *
# Create your views here.
'''
    def get(self, request):
        serializer=AlumnoSerializer()
        print(serializer.data)
        return Response(serializer.data)
'''

class GetAlumno(ListAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
class GetAula(ListAPIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class GetCxmxpxa(ListAPIView):
    queryset = Cxmxpxa.objects.all()
    serializer_class = CxmxpxaSerializer

class GetCurso(ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class GetMateria(ListAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer 

class GetProfesorA(ListAPIView):
    queryset = ProfesorA.objects.all()
    serializer_class = ProfesorASerializer

class GetPresencia(ListAPIView):
    queryset = Presencia.objects.all()
    serializer_class = PresenciaSerializer

class GetRelated(ListAPIView):
    queryset = Presencia.objects.all()
    serializer_class = RelatedSerializer