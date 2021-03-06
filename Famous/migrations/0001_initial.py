# Generated by Django 3.1.6 on 2021-02-10 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humanname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('day', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('extend', models.FloatField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Famous.field')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Famous.human')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Famous.task')),
            ],
        ),
    ]
