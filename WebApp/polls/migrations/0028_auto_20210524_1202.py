# Generated by Django 3.2.2 on 2021-05-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_alter_encuesta_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='serial',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
