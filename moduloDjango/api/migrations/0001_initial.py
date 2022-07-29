# Generated by Django 3.2.13 on 2022-07-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('legajo', models.CharField(db_column='Legajo', max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=50, null=True)),
                ('idcurso', models.IntegerField(db_column='IdCurso')),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('idaula', models.IntegerField(db_column='IdAula', primary_key=True, serialize=False)),
                ('numcamara', models.IntegerField(blank=True, db_column='NumCamara', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.IntegerField(db_column='IdCurso', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cxmxpxa',
            fields=[
                ('idcmpa', models.IntegerField(db_column='IdCMPA', primary_key=True, serialize=False)),
                ('bloquedia', models.CharField(blank=True, db_column='BloqueDia', max_length=3, null=True)),
                ('idaula', models.ForeignKey(db_column='IdAula', on_delete=django.db.models.deletion.DO_NOTHING, to='api.aula')),
                ('idcurso', models.ForeignKey(blank=True, db_column='IdCurso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idmateria', models.IntegerField(db_column='IdMateria', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volume', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfesorA',
            fields=[
                ('idprofesor', models.IntegerField(db_column='IdProfesor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presencia',
            fields=[
                ('idpresencia', models.IntegerField(db_column='IdPresencia', primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, db_column='Fecha', null=True)),
                ('tiempo', models.TimeField(blank=True, db_column='Tiempo', null=True)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=10, null=True)),
                ('idcmpa', models.ForeignKey(blank=True, db_column='IdCMPA', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.cxmxpxa')),
                ('legajoalumno', models.ForeignKey(blank=True, db_column='LegajoAlumno', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.alumno')),
            ],
        ),
        migrations.AddField(
            model_name='cxmxpxa',
            name='idmateria',
            field=models.ForeignKey(blank=True, db_column='IdMateria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.materia'),
        ),
        migrations.AddField(
            model_name='cxmxpxa',
            name='idprofesor',
            field=models.ForeignKey(blank=True, db_column='IdProfesor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.profesora'),
        ),
    ]