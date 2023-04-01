# Generated by Django 3.2.16 on 2023-03-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0008_alter_laptop_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='byte_type_for_ram',
            field=models.CharField(choices=[('TB', 'TB'), ('GB', 'GB'), ('MB', 'MB')], default='GB', max_length=3),
        ),
    ]
