# Generated by Django 4.2.6 on 2023-10-06 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0006_categoria_remove_carrito_fecha_creacion_itemcarrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TiendaApp.categoria'),
        ),
    ]