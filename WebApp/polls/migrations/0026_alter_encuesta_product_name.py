# Generated by Django 3.2.2 on 2021-05-24 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20210524_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.producto'),
        ),
    ]
