# Generated by Django 4.2.11 on 2024-04-03 19:53

from django.db import migrations, models
import my_holiday.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles/photos', validators=[my_holiday.accounts.validators.validate_photo_size], verbose_name='Profile Photo'),
        ),
    ]
