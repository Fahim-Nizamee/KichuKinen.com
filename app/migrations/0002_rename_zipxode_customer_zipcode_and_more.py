# Generated by Django 4.0.2 on 2022-02-16 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zipxode',
            new_name='zipcode',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='derscription',
            new_name='description',
        ),
    ]
