# Generated by Django 4.2.2 on 2023-06-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('descr', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('sort_descr', models.CharField(max_length=500)),
            ],
        ),
    ]
