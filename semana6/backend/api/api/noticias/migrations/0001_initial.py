# Generated by Django 3.1.3 on 2020-11-14 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Fonte',
                'verbose_name_plural': 'Fontes',
            },
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField(blank=True)),
                ('resumo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('data_publicacao', models.DateField(default='2020-11-14')),
                ('fonte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.fonte')),
            ],
            options={
                'verbose_name': 'Artigo',
                'verbose_name_plural': 'Artigos',
            },
        ),
    ]
