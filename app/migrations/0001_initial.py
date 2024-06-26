# Generated by Django 5.0.6 on 2024-06-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('linkedID', models.IntegerField(null=True)),
                ('linkprecedence', models.CharField(default='primary', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
