# Generated by Django 4.2.4 on 2023-09-20 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TiendaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(default='productos/default.jpg', upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(default='Sin marca', max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.CharField(default='Sin modelo', max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='talle',
            field=models.CharField(default='Sin Talle', max_length=16),
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=255)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaApp.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('codigo_postal', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
