# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-28 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliquota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
            options={
                'verbose_name': 'Alíquota',
                'verbose_name_plural': 'Alíquotas',
            },
        ),
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(blank=True, max_length=50, null=True)),
                ('cheiro', models.CharField(blank=True, max_length=50, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClasseQuimica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Composto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positivo', models.BooleanField()),
                ('notas', models.TextField(blank=True, null=True)),
                ('percentual_de_pureza', models.FloatField(blank=True, null=True)),
                ('notas_sobre_pureza', models.TextField(blank=True, null=True)),
                ('quantidade', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('solvente', models.CharField(blank=True, max_length=50, null=True)),
                ('mw', models.FloatField(blank=True, null=True)),
                ('formula', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_comum', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_IUPAC', models.CharField(blank=True, max_length=50, null=True)),
                ('classe_quimica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.ClasseQuimica')),
            ],
        ),
        migrations.CreateModel(
            name='Eluente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('polar', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('common', models.CharField(blank=True, help_text='Nome popular desta espécie de planta, ex.: pitangueira', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Espécie',
            },
        ),
        migrations.CreateModel(
            name='Especime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('data_da_coleta', models.DateTimeField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('altitude', models.IntegerField(blank=True, null=True)),
                ('solo', models.CharField(blank=True, max_length=200, null=True)),
                ('vegetacao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Vegetação')),
                ('altura', models.FloatField(blank=True, null=True)),
                ('diametro', models.FloatField(blank=True, null=True, verbose_name='Diâmetro')),
                ('notas', models.TextField(blank=True, null=True)),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Especie', verbose_name='Espécie')),
            ],
            options={
                'verbose_name': 'Espécime',
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Família',
            },
        ),
        migrations.CreateModel(
            name='Fracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eluente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Eluente')),
            ],
            options={
                'verbose_name': 'Fração',
                'verbose_name_plural': 'Frações',
            },
        ),
        migrations.CreateModel(
            name='Fracionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliquota', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Aliquota')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Familia')),
            ],
            options={
                'verbose_name': 'Gênero',
            },
        ),
        migrations.CreateModel(
            name='OrgaoDePlanta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgao', models.CharField(max_length=100, verbose_name='Órgão')),
            ],
            options={
                'verbose_name': 'Órgão de Planta',
            },
        ),
        migrations.CreateModel(
            name='Sequenciamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data do Sequenciamento Genético')),
                ('arquivo_fasta', models.CharField(max_length=1000)),
                ('aliquota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Aliquota')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeAliquota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Alíquota',
                'verbose_name_plural': 'Tipos de Alíquota',
            },
        ),
        migrations.CreateModel(
            name='TipoDeFracionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Fracionamento',
                'verbose_name_plural': 'Tipos de Fracionamento',
            },
        ),
        migrations.AddField(
            model_name='fracionamento',
            name='tipo_de_fracionamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.TipoDeFracionamento'),
        ),
        migrations.AddField(
            model_name='fracao',
            name='fracionamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Fracionamento'),
        ),
        migrations.AddField(
            model_name='especie',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Genero'),
        ),
        migrations.AddField(
            model_name='composto',
            name='fracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Fracao'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Especime'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='orgao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.OrgaoDePlanta'),
        ),
        migrations.AddField(
            model_name='aliquota',
            name='amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.Amostra'),
        ),
        migrations.AddField(
            model_name='aliquota',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobureau.TipoDeAliquota'),
        ),
    ]
