# Generated by Django 2.2.2 on 2019-06-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone_1', models.CharField(max_length=13)),
                ('telefone_2', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=80, null=True)),
                ('bairro', models.CharField(max_length=30, null=True)),
                ('estado', models.CharField(max_length=30, null=True)),
                ('municipio', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Contato')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Endereco')),
            ],
        ),
    ]