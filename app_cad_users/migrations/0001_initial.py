# Generated by Django 4.2.5 on 2023-09-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
