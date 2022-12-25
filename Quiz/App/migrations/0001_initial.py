# Generated by Django 4.0.6 on 2022-11-04 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cource', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.IntegerField()),
                ('standard', models.CharField(max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': ' Students',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('correctAns', models.CharField(max_length=100)),
                ('A', models.CharField(max_length=100)),
                ('B', models.CharField(max_length=100)),
                ('C', models.CharField(blank=True, max_length=100)),
                ('D', models.CharField(blank=True, max_length=100)),
                ('userAns', models.CharField(blank=True, max_length=100)),
                ('coucre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cource')),
            ],
        ),
        migrations.AddField(
            model_name='cource',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.student'),
        ),
    ]
