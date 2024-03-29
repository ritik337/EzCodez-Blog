# Generated by Django 5.0.1 on 2024-01-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/blog_image/')),
                ('tittle', models.CharField(max_length=24)),
                ('desc', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/blog_image/')),
                ('tittle', models.CharField(max_length=24)),
                ('githublink', models.CharField(max_length=800)),
                ('goggledrivelink', models.CharField(max_length=800)),
                ('zipfilelink', models.CharField(max_length=800)),
                ('filelink', models.CharField(max_length=800)),
            ],
        ),
    ]
