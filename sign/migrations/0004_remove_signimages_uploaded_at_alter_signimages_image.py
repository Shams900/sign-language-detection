# Generated by Django 4.2.1 on 2023-05-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_alter_signimages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signimages',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='signimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]