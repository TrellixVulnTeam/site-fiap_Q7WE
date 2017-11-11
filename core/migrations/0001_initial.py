# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(db_column='RA', unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=120)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=80, null=True)),
                ('celular', models.CharField(db_column='Celular', max_length=11)),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=2)),
            ],
            options={
                'db_table': 'Aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivoquestoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1)),
                ('arquivo', models.CharField(db_column='Arquivo', max_length=500, unique=True)),
            ],
            options={
                'db_table': 'ArquivoQuestoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivorespostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1)),
                ('ra_aluno', models.IntegerField(db_column='RA_Aluno')),
                ('arquivo', models.CharField(db_column='Arquivo', max_length=500, unique=True)),
            ],
            options={
                'db_table': 'ArquivoRespostas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoreCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField()),
                ('professor', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('ativo', models.BooleanField()),
                ('descricao', models.TextField()),
            ],
            options={
                'db_table': 'core_curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(db_column='Sigla', max_length=5, unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cursoturma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
            ],
            options={
                'db_table': 'CursoTurma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=240, unique=True)),
                ('carga_horario', models.SmallIntegerField(db_column='Carga_Horario')),
                ('teoria', models.DecimalField(db_column='Teoria', decimal_places=0, max_digits=3)),
                ('pratica', models.DecimalField(db_column='Pratica', decimal_places=0, max_digits=3)),
                ('ementa', models.TextField(db_column='Ementa')),
                ('competencias', models.TextField(db_column='Competencias')),
                ('habilidades', models.TextField(db_column='Habilidades')),
                ('conteudo', models.TextField(db_column='Conteudo')),
                ('bibliografia_basica', models.TextField(db_column='Bibliografia_Basica')),
                ('bibliografia_complementar', models.TextField(db_column='Bibliografia_Complementar')),
            ],
            options={
                'db_table': 'Disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gradecurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField(db_column='Ano')),
                ('semestre', models.CharField(db_column='Semestre', max_length=1, unique=True)),
            ],
            options={
                'db_table': 'GradeCurricular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1, unique=True)),
            ],
            options={
                'db_table': 'Matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('ano_grade', models.SmallIntegerField(db_column='Ano_Grade')),
                ('numero', models.SmallIntegerField(db_column='Numero', unique=True)),
            ],
            options={
                'db_table': 'Periodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periododisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('ano_grade', models.SmallIntegerField(db_column='Ano_Grade')),
                ('semestre_grade', models.CharField(db_column='Semestre_Grade', max_length=1)),
                ('numero_periodo', models.SmallIntegerField(db_column='Numero_Periodo', unique=True)),
            ],
            options={
                'db_table': 'PeriodoDisciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(db_column='RA', unique=True)),
                ('apelido', models.CharField(db_column='Apelido', max_length=30, unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=120)),
                ('email', models.CharField(db_column='Email', max_length=80)),
                ('celular', models.CharField(db_column='Celular', max_length=11)),
            ],
            options={
                'db_table': 'Professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_discplina', models.CharField(db_column='Nome_Discplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('numero', models.IntegerField(db_column='Numero', unique=True)),
                ('data_limite_entrega', models.CharField(db_column='Data_Limite_Entrega', max_length=10)),
                ('descricao', models.TextField(blank=True, db_column='Descricao', null=True)),
                ('dia_publicacao', models.CharField(db_column='Dia_Publicacao', max_length=10)),
            ],
            options={
                'db_table': 'Questoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('numero_questao', models.IntegerField(db_column='Numero_Questao', unique=True)),
                ('ra_aluno', models.IntegerField(db_column='RA_Aluno', unique=True)),
                ('data_avaliacao', models.CharField(db_column='Data_Avaliacao', max_length=10)),
                ('nota', models.DecimalField(db_column='Nota', decimal_places=2, max_digits=4)),
                ('avaliacao', models.TextField(blank=True, db_column='Avaliacao', null=True)),
                ('descricao', models.TextField(blank=True, db_column='Descricao', null=True)),
                ('data_de_envio', models.CharField(db_column='Data_de_Envio', max_length=10)),
            ],
            options={
                'db_table': 'Respostas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('idturma', models.CharField(max_length=1, unique=True)),
                ('turno', models.CharField(db_column='Turno', max_length=15)),
            ],
            options={
                'db_table': 'Turma',
                'managed': False,
            },
        ),
    ]
