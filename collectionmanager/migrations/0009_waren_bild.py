# Generated by Django 5.0.4 on 2024-04-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionmanager', '0008_regale_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='waren',
            name='bild',
            field=models.ImageField(default='something', upload_to='ware_bilder/'),
            preserve_default=False,
        ),
    ]