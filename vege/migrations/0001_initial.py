# Generated by Django 5.0.4 on 2024-07-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(default='', max_length=100)),
                ('receipe_description', models.TextField(default='')),
                ('receipe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
