# Generated by Django 3.2.2 on 2021-05-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_producto_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='product_calidad',
            field=models.IntegerField(choices=[(1, 'Muy Malo'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Excelente')], default=0),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='product_calificacion',
            field=models.IntegerField(choices=[(1, 'Muy Malo'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Excelente')], default=0),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='product_precio',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='product_precioTamano',
            field=models.IntegerField(choices=[(1, 'Muy Malo'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Excelente')], default=0),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='product_tiempoUso',
            field=models.IntegerField(choices=[(1, 'Muy Malo'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Excelente')], default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='product_image',
            field=models.ImageField(default='post/pic01.jpg', upload_to='post/%y/%m/%d'),
        ),
    ]
