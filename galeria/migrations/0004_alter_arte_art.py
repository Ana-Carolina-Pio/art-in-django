# Generated by Django 5.0.4 on 2024-04-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_arte_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='art',
            field=models.ImageField(blank=True, null=True, upload_to='galeria/'),
        ),
    ]
