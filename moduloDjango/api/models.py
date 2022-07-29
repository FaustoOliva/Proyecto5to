# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models
from django.utils import timezone


class Alumno(models.Model):
    legajo = models.CharField(db_column='Legajo', primary_key=True, max_length=50 )  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50 , blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.

    

    def __str__(self):
        return(self.legajo)


class Aula(models.Model):
    idaula = models.IntegerField(db_column='IdAula', primary_key=True)  # Field name made lowercase.
    numcamara = models.IntegerField(db_column='NumCamara', blank=True, null=True)  # Field name made lowercase.

   

    def __str__(self):
        return f'{self.idaula}'

class Curso(models.Model):
    idcurso = models.IntegerField(db_column='IdCurso', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50 , blank=True, null=True)  # Field name made lowercase.

   

    def __str__(self):
        return(self.nombre)

class Cxmxpxa(models.Model):
    idcmpa = models.IntegerField(db_column='IdCMPA', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso', blank=True, null=True)  # Field name made lowercase.
    idmateria = models.ForeignKey('Materia', models.DO_NOTHING, db_column='IdMateria', blank=True, null=True)  # Field name made lowercase.
    bloquedia = models.CharField(db_column='BloqueDia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idaula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='IdAula')  # Field name made lowercase.
    idprofesor = models.ForeignKey('ProfesorA', models.DO_NOTHING, db_column='IdProfesor', blank=True, null=True)  # Field name made lowercase.

   

    def __str__(self):
        return f'{self.idcmpa}'

class Materia(models.Model):
    idmateria = models.IntegerField(db_column='IdMateria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

   

    def __str__(self):
        return(self.nombre)

class Presencia(models.Model):
    idpresencia = models.IntegerField(db_column='IdPresencia', primary_key=True)  # Field name made lowercase.
    legajoalumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='LegajoAlumno', blank=True, null=True)  # Field name made lowercase.
    idcmpa = models.ForeignKey(Cxmxpxa, models.DO_NOTHING, db_column='IdCMPA', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    tiempo = models.TimeField(db_column='Tiempo', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def was_published_recently(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)

   

    def __str__(self):
        return f'{self.idpresencia}'


class ProfesorA(models.Model):
    idprofesor = models.IntegerField(db_column='IdProfesor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

