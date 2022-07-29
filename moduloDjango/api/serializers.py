# Ayudan a convertir los tipos complejos de datos en 
# datos primitivos que entienda Python
from rest_framework import serializers
from .models import *

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CxmxpxaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cxmxpxa
        fields = '__all__' 

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__' 

class PresenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presencia
        fields = '__all__' 

class ProfesorASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorA
        fields = '__all__'


class RelatedSerializer(serializers.ModelSerializer):
    legajoalumno = AlumnoSerializer()

    class Meta:
        model = Presencia
        fields = '__all__'