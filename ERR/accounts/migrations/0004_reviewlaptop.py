# Generated by Django 3.2.16 on 2023-03-17 15:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laptops', '0009_laptop_byte_type_for_ram'),
        ('accounts', '0003_delete_reviewlaptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewLaptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5, 'Sorry not a valid rating!'), django.core.validators.MaxValueValidator(5, 'Sorry not a valid rating!')])),
                ('comment', models.TextField()),
                ('time_field', models.TimeField(auto_now=True)),
                ('date_field', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptops.laptop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
